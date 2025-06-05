import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
import MySQLdb
from templates import Templates_Form

conn = MySQLdb.connect("localhost", "root", "root", "gor_stroy", charset="utf8mb4")
cursor = conn.cursor()


class Template_Window(QMainWindow):
    def __init__(self, engineer_window=None):
        super().__init__()
        self.ui = Templates_Form()
        self.ui.setupUi(self)
        self.engineer_window = engineer_window
        self.load_material()
        self.ui.pushButton_save_new_temp.clicked.connect(self.save_template)

    def load_material(self):
        self.ui.comboBox_material.addItem("Выберите материал", None)
        cursor.execute("SELECT id, name FROM Material")
        materials = cursor.fetchall()
        for mat in materials:
            self.ui.comboBox_material.addItem(mat[1], mat[0])

    def save_template(self):
        try:
            name = self.ui.lineEdit_name_temp.text()
            width = self.ui.lineEdit_width_temp_2.text()
            height = self.ui.lineEdit_heigth_temp_3.text()
            depth = self.ui.lineEdit_depth_temp_4.text()
            material_id = self.ui.comboBox_material.currentData()
            walls = self.ui.lineEdit_type_wall.text()
            roof = self.ui.lineEdit_roof.text()
            snow_load = self.ui.lineEdit_snow.text()
            wind_load = self.ui.lineEdit_windy.text()
            fire_class = self.ui.lineEdit_fire.text()
            wall_thickness = self.ui.wall_thickness.text()
            foundation_height = self.ui.foundation_height.text()
            foundation_thickness = self.ui.foundation_thickness.text()

            fields = [name, width, height, depth, walls, roof, snow_load, wind_load,
                      fire_class, wall_thickness, foundation_height, foundation_thickness]
            if not all(fields) or material_id is None:
                QMessageBox.warning(self, "Ошибка", "Заполните все поля и выберите материал!")
                return

            errors = []
            if not self.check_width(width): errors.append("Ширина должна быть 3000-10000 мм")
            if not self.check_height(height): errors.append("Высота должна быть 2500-8000 мм")
            if not self.check_depth(depth): errors.append("Глубина должна быть 2000-7000 мм")
            if not self.check_snow_load(snow_load): errors.append("Снеговая нагрузка 100-500 кг/м²")
            if not self.check_wind_load(wind_load): errors.append("Ветровая нагрузка 50-300 кг/м²")
            if not self.check_fire_class(fire_class): errors.append("Класс пожаробезопасности 1-5")
            if not self.check_wall_thickness(wall_thickness): errors.append("Толщина стен 150-300 мм")
            if not self.check_foundation_height(foundation_height): errors.append("Высота фундамента 300-600 мм")
            if not self.check_foundation_thickness(foundation_thickness): errors.append("Толщина фундамента 200-400 мм")

            if errors:
                QMessageBox.warning(self, "Ошибка", "\n".join(errors))
                return

            json_data = json.dumps({
                "width": int(width),
                "height": int(height),
                "depth": int(depth),
                "walls": walls,
                "roof": roof,
                "snow_load": float(snow_load),
                "wind_load": float(wind_load),
                "fire_class": fire_class,
                "wall_thickness": int(wall_thickness),
                "foundation_height": int(foundation_height),
                "foundation_thickness": int(foundation_thickness)
            }, ensure_ascii=False)

            cursor.execute("""
                INSERT INTO Templates (name, json_data, created_at, material_id)
                VALUES (%s, %s, NOW(), %s)
            """, (name, json_data, material_id))
            conn.commit()

            QMessageBox.information(self, "Успех", "Шаблон создан!")

            if self.engineer_window:
                self.engineer_window.update_templates_list(force_reload=True)

            self.close()

        except MySQLdb.Error as e:
            conn.rollback()
            QMessageBox.critical(self, "Ошибка БД", f"Ошибка: {e}")

    # Методы валидации
    def check_width(self, value):
        try:
            return 3000 <= int(value) <= 10000
        except:
            return False

    def check_height(self, value):
        try:
            return 2500 <= int(value) <= 8000
        except:
            return False

    def check_depth(self, value):
        try:
            return 2000 <= int(value) <= 7000
        except:
            return False

    def check_snow_load(self, value):
        try:
            return 100 <= float(value) <= 500
        except:
            return False

    def check_wind_load(self, value):
        try:
            return 50 <= float(value) <= 300
        except:
            return False

    def check_fire_class(self, value):
        return value in ["1", "2", "3", "4", "5"]

    def check_wall_thickness(self, value):
        try:
            return 150 <= int(value) <= 300
        except:
            return False

    def check_foundation_height(self, value):
        try:
            return 300 <= int(value) <= 600
        except:
            return False

    def check_foundation_thickness(self, value):
        try:
            return 200 <= int(value) <= 400
        except:
            return False