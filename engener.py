from PyQt6 import QtCore, QtGui, QtWidgets
import os
import sys


class EngineerWindow(object):
    def setupUi(self, engener):
        engener.setObjectName("engener")

        # Центрируем окно при открытии
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        engener.resize(791, 609)
        engener.move(
            (screen_geometry.width() - engener.width()) // 2,
            (screen_geometry.height() - engener.height()) // 2
        )
        icon_path = os.path.join(os.path.dirname(__file__), "images", "гор.PNG")
        if os.path.exists(icon_path):
            engener.setWindowIcon(QtGui.QIcon(icon_path))

        # Главный виджет с вертикальной компоновкой
        central_widget = QtWidgets.QWidget(engener)
        engener.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Фоновое изображение
        self.background_label = QtWidgets.QLabel(central_widget)
        self.background_label.setScaledContents(True)
        background_path = os.path.join(os.path.dirname(__file__), "images", "фон диплома.jpg")
        self.background_label.setPixmap(QtGui.QPixmap(background_path))
        self.background_label.lower()  # Отправляем на задний план

        # Header Frame
        self.frame_header = QtWidgets.QFrame()
        self.frame_header.setMinimumHeight(60)
        self.frame_header.setStyleSheet("""
            QFrame {
                background-color: rgba(149, 149, 149, 65);
                border-radius: 15px;
                border: 2px solid #3c3c3c;
            }
        """)

        header_layout = QtWidgets.QHBoxLayout(self.frame_header)
        header_layout.setContentsMargins(10, 5, 10, 5)

        self.label_icon = QtWidgets.QLabel()
        self.label_icon.setPixmap(QtGui.QPixmap("images/free-icon-programmer-13518032.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setFixedSize(41, 41)

        self.label_title = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(6, 6, 6);")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(self.label_icon)
        header_layout.addWidget(self.label_title, 1)  # Растягиваем по ширине

        # Main Content Frame
        self.frame_main = QtWidgets.QFrame()
        self.frame_main.setStyleSheet("""
            QFrame {
                background-color: rgba(149, 149, 149, 0.85);
                border-radius: 15px;
                border: 2px solid #3c3c3c;
            }
        """)

        main_content_layout = QtWidgets.QHBoxLayout(self.frame_main)
        main_content_layout.setContentsMargins(10, 10, 10, 10)
        main_content_layout.setSpacing(10)

        # Sidebar Frame
        self.frame_sidebar = QtWidgets.QFrame()
        self.frame_sidebar.setMinimumWidth(200)
        self.frame_sidebar.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                border: 1px solid #3c3c3c;
            }
        """)

        sidebar_layout = QtWidgets.QVBoxLayout(self.frame_sidebar)
        sidebar_layout.setSpacing(8)  # Уменьшаем расстояние между элементами
        sidebar_layout.setContentsMargins(10, 10, 10, 10)  # Уменьшаем отступы

        self.label_templates = QtWidgets.QLabel("Шаблоны зданий")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.label_templates.setFont(font)
        self.label_templates.setStyleSheet("color: rgb(6, 6, 6);")

        self.listWidget_template = QtWidgets.QListWidget()
        self.listWidget_template.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid #3c3c3c;
                border-radius: 8px;
                padding: 3px;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #D3D3D3;
            }
            QListWidget::item:hover {
                background-color: #E6F3FA;
            }
            QListWidget::item:selected {
                background-color: #008080;
                color: white;
            }
        """)

        # Кнопки сайдбара
        button_style = """
            QPushButton {
                background: #000086;
                color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 11px;
                border: 1px solid #6ab0de;
                padding: 5px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #006666;
            }
            QPushButton:pressed {
                background-color: #004d4d;
            }
        """

        self.pushButton_template = QtWidgets.QPushButton("Создать/Посмотреть чертеж")
        self.pushButton_template.setStyleSheet(button_style)
        self.pushButton_template.setIcon(QtGui.QIcon("images/free-icon-pen-13944019.png"))

        self.pushButton_new_temp = QtWidgets.QPushButton("Создать новый шаблон")
        self.pushButton_new_temp.setStyleSheet(button_style)
        self.pushButton_new_temp.setIcon(QtGui.QIcon("images/free-icon-blueprint-1624169.png"))

        self.pushButton__3d = QtWidgets.QPushButton("Просмотр 3D-модели")
        self.pushButton__3d.setStyleSheet(button_style)
        self.pushButton__3d.setIcon(QtGui.QIcon("images/free-icon-3d-model-17456294.png"))

        self.pushButton_close = QtWidgets.QPushButton("Завершить проект")
        self.pushButton_close.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                background-color: #8B0000;
                color: white;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #CD5C5C;
            }
            QPushButton:pressed {
                background-color: #6B0000;
            }
        """)
        self.pushButton_close.setIcon(QtGui.QIcon("images/free-icon-completed-form-14458832.png"))

        # Добавляем элементы в сайдбар с компактным расположением
        sidebar_layout.addWidget(self.label_templates)
        sidebar_layout.addWidget(self.listWidget_template)
        sidebar_layout.addWidget(self.pushButton_template)
        sidebar_layout.addWidget(self.pushButton_new_temp)
        sidebar_layout.addWidget(self.pushButton__3d)
        sidebar_layout.addSpacing(2)  # Уменьшенное расстояние перед кнопкой закрытия
        sidebar_layout.addWidget(self.pushButton_close)

        # Content Frame
        self.frame_content = QtWidgets.QFrame()
        self.frame_content.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                border: 1px solid #3c3c3c;
            }
        """)

        content_layout = QtWidgets.QVBoxLayout(self.frame_content)
        content_layout.setContentsMargins(10, 10, 10, 10)

        self.label_drawing_title = QtWidgets.QLabel("2D-чертеж")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.label_drawing_title.setFont(font)
        self.label_drawing_title.setStyleSheet("color: rgb(6, 6, 6);")

        self.label_drawing = QtWidgets.QLabel()
        self.label_drawing.setStyleSheet("""
            background-color: white;
            border: 1px solid #3c3c3c;
            border-radius: 8px;
        """)
        self.label_drawing.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(self.label_drawing_title)
        content_layout.addWidget(self.label_drawing, 1)  # Растягиваем по высоте

        # Добавляем сайдбар и контент в основную область
        main_content_layout.addWidget(self.frame_sidebar)
        main_content_layout.addWidget(self.frame_content, 1)  # Растягиваем по ширине

        # Добавляем header и main в главный layout
        main_layout.addWidget(self.frame_header)
        main_layout.addWidget(self.frame_main, 1)  # Растягиваем по высоте

        # Обработчик изменения размера окна
        engener.resizeEvent = self.resizeEvent

        self.retranslateUi(engener)
        QtCore.QMetaObject.connectSlotsByName(engener)

    def resizeEvent(self, event):
        """Обработчик изменения размера окна"""
        # Обновляем размер фонового изображения
        self.background_label.setGeometry(
            0, 0,
            event.size().width(),
            event.size().height()
        )
        event.accept()

    def retranslateUi(self, engener):
        _translate = QtCore.QCoreApplication.translate
        engener.setWindowTitle(_translate("engener", "Инженерный модуль - ООО \"ГОР-СТРОЙ\""))
        self.label_title.setText(_translate("engener", "ООО \"ГОР-СТРОЙ\" - Инженерный модуль"))
        self.label_templates.setText(_translate("engener", "Шаблоны зданий"))
        self.pushButton_template.setText(_translate("engener", "Создать/Посмотреть чертеж"))
        self.pushButton_template.setShortcut(_translate("engener", "Backspace"))
        self.pushButton_new_temp.setText(_translate("engener", "Создать новый шаблон"))
        self.pushButton__3d.setText(_translate("engener", "Просмотр 3D-модели"))
        self.pushButton_close.setText(_translate("engener", "Завершить проект"))
        self.label_drawing_title.setText(_translate("engener", "2D-чертеж"))


