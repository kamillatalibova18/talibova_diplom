import sys
import os
import json
import subprocess
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import MySQLdb
from engener import EngineerWindow
from template_code import Template_Window

FREECAD_PATH = r'C:\Users\Professional\Desktop\FreeCAD 1.0\bin\freecad.exe'


class EngineerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.conn = MySQLdb.connect(
            host="localhost",
            user="root",
            password="root",
            database="gor_stroy",
            charset="utf8mb4"
        )
        self.cursor = self.conn.cursor()

        self.ui = EngineerWindow()
        self.ui.setupUi(self)

        self.ui.pushButton__3d.clicked.connect(self.on_view_3d_model)
        self.ui.pushButton_new_temp.clicked.connect(self.new_temp)
        self.ui.pushButton_template.clicked.connect(self.on_draw_2d_template)
        self.ui.pushButton_close.clicked.connect(self.close_project)

        self.update_templates_list()

    def close_project(self):
        selected_item = self.ui.listWidget_template.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите шаблон!")
            return

        template_id = selected_item.data(Qt.ItemDataRole.UserRole)
        template_name = selected_item.text()
        employee_id = 1  # При необходимости — использовать текущего пользователя

        safe_name = template_name.replace(' ', '_')

        try:
            # Получаем id чертежа
            self.cursor.execute("""
                SELECT id FROM Drawings 
                WHERE file_path LIKE %s 
                ORDER BY id DESC LIMIT 1
            """, (f"%{safe_name}.png",))
            row = self.cursor.fetchone()
            if not row:
                raise Exception("Чертеж не найден для шаблона.")
            id_drawing = row[0]

            # Получаем id 3D модели
            self.cursor.execute("""
                SELECT id FROM 3d_model 
                WHERE file_path LIKE %s 
                ORDER BY id DESC LIMIT 1
            """, (f"%{safe_name}.FCStd",))
            row = self.cursor.fetchone()
            if not row:
                raise Exception("3D модель не найдена для шаблона.")
            id_model = row[0]

            # Добавление проекта
            self.cursor.execute("""
                INSERT INTO Projects (name, employee_id, status, created_at, updated_at, id_drawing, id_model)
                VALUES (%s, %s, 'активный', CURDATE(), CURDATE(), %s, %s)
            """, (template_name, employee_id, id_drawing, id_model))

            # Удаление шаблона
            self.cursor.execute("DELETE FROM Templates WHERE id = %s", (template_id,))
            self.conn.commit()

            self.ui.listWidget_template.takeItem(self.ui.listWidget_template.row(selected_item))

            QMessageBox.information(
                self,
                "Проект завершён",
                "Проект успешно завершен. Вся нужная информация передана делопроизводителю для оформления документации."
            )

        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Ошибка", f"Не удалось завершить проект: {str(e)}")

    def update_templates_list(self, force_reload=False):
        self.ui.listWidget_template.clear()
        try:
            if force_reload:
                self.conn.commit()

            self.cursor.execute("SELECT id, name FROM Templates")
            templates = self.cursor.fetchall()

            for template_id, name in templates:
                item = QListWidgetItem(name)
                item.setData(Qt.ItemDataRole.UserRole, template_id)
                self.ui.listWidget_template.addItem(item)

        except MySQLdb.Error as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки: {e}")

    def new_temp(self):
        self.template_window = Template_Window(engineer_window=self)
        self.template_window.show()

    def on_draw_2d_template(self):
        selected_item = self.ui.listWidget_template.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите шаблон!")
            return

        try:
            template_id = selected_item.data(Qt.ItemDataRole.UserRole)
            image_path = self.build_2d_drawing_matplotlib(template_id)
            pixmap = QtGui.QPixmap(image_path)
            self.ui.label_drawing.setPixmap(pixmap.scaled(
                self.ui.label_drawing.size(),
                QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                QtCore.Qt.TransformationMode.SmoothTransformation
            ))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def build_2d_drawing_matplotlib(self, template_id):
        self.cursor.execute("SELECT name, json_data FROM Templates WHERE id = %s", (template_id,))
        row = self.cursor.fetchone()
        if not row:
            raise ValueError("Шаблон не найден")

        template_name, json_data = row
        data = json.loads(json_data)
        width = float(data.get("width", 6000))
        depth = float(data.get("depth", 7000))
        wall_thickness = float(data.get("wall_thickness", 200))
        foundation_thickness = float(data.get("foundation_thickness", 200))

        drawings_dir = os.path.join(os.getcwd(), "drawings")
        os.makedirs(drawings_dir, exist_ok=True)

        image_path = os.path.join(drawings_dir, f"{template_name}.png")

        # Если чертёж уже существует, не создаём и не сохраняем его повторно
        if os.path.exists(image_path):
            return image_path

        fig, ax = plt.subplots(figsize=(10, 8))
        ax.add_patch(Rectangle((0, 0), width, depth, linewidth=1.5, edgecolor='black', facecolor='lightgrey'))
        inner_width = width - 2 * wall_thickness
        inner_depth = depth - 2 * wall_thickness
        ax.add_patch(Rectangle((wall_thickness, wall_thickness), inner_width, inner_depth,
                               linewidth=1.5, edgecolor='black', facecolor='white'))

        ax.annotate(f"{int(width)} мм", (width / 2, -100), (width / 2, -300),
                    arrowprops=dict(arrowstyle='<->'), ha='center', fontsize=10)
        ax.annotate(f"{int(depth)} мм", (-100, depth / 2), (-300, depth / 2),
                    arrowprops=dict(arrowstyle='<->'), va='center', rotation=90, fontsize=10)
        ax.annotate(f"Толщина стен: {int(wall_thickness)} мм", (width + 100, depth - 100), fontsize=10)
        ax.annotate(f"Толщина фундамента: {int(foundation_thickness)} мм", (width + 100, depth - 300), fontsize=10)

        ax.set_xlim(-400, width + 400)
        ax.set_ylim(-400, depth + 400)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()
        plt.savefig(image_path, dpi=150)
        plt.close()

        try:
            self.cursor.execute(
                "INSERT INTO Drawings (file_path, created_at) VALUES (%s, CURDATE())",
                (image_path,)
            )
            self.conn.commit()
        except MySQLdb.IntegrityError:
            # Возможно, уже есть запись — пропускаем
            self.conn.rollback()
        except MySQLdb.Error as e:
            self.conn.rollback()
            raise Exception(f"Ошибка сохранения чертежа: {str(e)}")

        return image_path

    def on_view_3d_model(self):
        selected_item = self.ui.listWidget_template.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите шаблон!")
            return

        try:
            template_id = selected_item.data(Qt.ItemDataRole.UserRole)
            self.build_house(template_id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def build_house(self, template_id):
        self.cursor.execute("SELECT json_data, name FROM Templates WHERE id = %s", (template_id,))
        row = self.cursor.fetchone()
        if not row:
            raise ValueError("Шаблон не найден")

        data = json.loads(row[0])
        template_name = row[1].replace(" ", "_")

        data.setdefault("foundation_height", 300)
        data.setdefault("foundation_thickness", 200)
        data.setdefault("wall_thickness", 200)

        os.makedirs("3d_model", exist_ok=True)
        output_file = os.path.join("3d_model", f"{template_name}.FCStd")

        # Если файл уже существует — не пересоздаём
        if os.path.exists(output_file):
            subprocess.run([FREECAD_PATH, output_file], check=True)
            return

        script = self.generate_freecad_script(data, output_file)
        script_path = os.path.abspath(f"freecad_script_{template_id}.py")

        with open(script_path, "w", encoding="utf-8") as f:
            f.write(script)

        subprocess.run([FREECAD_PATH, script_path], check=True)
        # Сохраняем в БД
        try:
            self.cursor.execute(
                "INSERT INTO 3d_model (file_path, created_at) VALUES (%s, CURDATE())",
                (os.path.abspath(output_file),)
            )
            self.conn.commit()
        except MySQLdb.Error as e:
            self.conn.rollback()
            raise Exception(f"Ошибка сохранения 3D-модели в базу данных: {str(e)}")

    def generate_freecad_script(self, data, output_file):
        width = float(data.get("width", 6000))
        depth = float(data.get("depth", 7000))
        height = float(data.get("height", 3000))
        foundation_height = float(data.get("foundation_height", 300))
        wall_thickness = float(data.get("wall_thickness", 200))
        roof_type = data.get("roof", "двускатная")

        script = f"""
import FreeCAD, Part

doc = FreeCAD.newDocument('House')
foundation = Part.makeBox({width}, {depth}, {foundation_height})
foundation_obj = doc.addObject("Part::Feature", "Foundation")
foundation_obj.Shape = foundation

outer_wall = Part.makeBox({width}, {depth}, {height})
inner_wall = Part.makeBox(
    {width}-2*{wall_thickness}, 
    {depth}-2*{wall_thickness}, 
    {height}-{foundation_height}
)
inner_wall.translate(FreeCAD.Vector({wall_thickness}, {wall_thickness}, {foundation_height}))
walls = outer_wall.cut(inner_wall)
walls_obj = doc.addObject("Part::Feature", "Walls")
walls_obj.Shape = walls
"""

        if roof_type == "двускатная":
            script += f"""
points = [FreeCAD.Vector(0,0,0), FreeCAD.Vector({width}/2,0,{height}/2), FreeCAD.Vector({width},0,0)]
roof = Part.Face(Part.makePolygon(points)).extrude(FreeCAD.Vector(0,{depth},0))
"""
        elif roof_type == "односкатная":
            script += f"""
points = [FreeCAD.Vector(0,0,0), FreeCAD.Vector({width},0,{height}/2), FreeCAD.Vector({width},0,0)]
roof = Part.Face(Part.makePolygon(points)).extrude(FreeCAD.Vector(0,{depth},0))
"""
        else:
            script += f"roof = Part.makeBox({width}, {depth}, 100)\n"

        script += f"""
roof_obj = doc.addObject("Part::Feature", "Roof")
roof_obj.Shape = roof
roof_obj.Placement.Base = FreeCAD.Vector(0,0,{height})

doc.recompute()
doc.saveAs(r"{output_file}")
"""
        return script


