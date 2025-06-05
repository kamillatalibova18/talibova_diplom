from PyQt6 import QtCore, QtGui, QtWidgets
import os
import sys


class Clerk_Form(object):
    def setupUi(self, clerk):
        clerk.setObjectName("clerk")

        # Центрируем окно при открытии
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        clerk.resize(900, 650)
        clerk.move(
            (screen_geometry.width() - clerk.width()) // 2,
            (screen_geometry.height() - clerk.height()) // 2
        )
        # В начале метода setupUi, после центрирования окна
        icon_path = os.path.join(os.path.dirname(__file__), "images", "гор.PNG")
        if os.path.exists(icon_path):
            clerk.setWindowIcon(QtGui.QIcon(icon_path))

        # Главный виджет с вертикальной компоновкой
        central_widget = QtWidgets.QWidget(clerk)
        clerk.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

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
                background-color: rgba(149, 149, 149, 0.85);
                border-radius: 15px;
                border: 2px solid #3c3c3c;
            }
        """)

        header_layout = QtWidgets.QHBoxLayout(self.frame_header)
        header_layout.setContentsMargins(10, 5, 10, 5)

        self.label_icon = QtWidgets.QLabel()
        icon_path = os.path.join(os.path.dirname(__file__), "images", "Person_Holding_Up_A_Document-1024.webp")
        self.label_icon.setPixmap(QtGui.QPixmap(icon_path))
        self.label_icon.setScaledContents(True)
        self.label_icon.setFixedSize(41, 41)

        self.label_title = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(self.label_icon)
        header_layout.addWidget(self.label_title, 1)  # Растягиваем по ширине

        # Main Content Frame
        self.frame_main = QtWidgets.QFrame()
        self.frame_main.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)

        main_content_layout = QtWidgets.QHBoxLayout(self.frame_main)
        main_content_layout.setContentsMargins(0, 0, 0, 0)
        main_content_layout.setSpacing(10)

        # Левая панель (проекты)
        self.frame_left = QtWidgets.QFrame()
        self.frame_left.setMinimumWidth(250)
        self.frame_left.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                border: 1px solid #3c3c3c;
            }
        """)

        left_layout = QtWidgets.QVBoxLayout(self.frame_left)
        left_layout.setContentsMargins(10, 10, 10, 10)
        left_layout.setSpacing(10)

        self.label_projects = QtWidgets.QLabel("Список проектов")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_projects.setFont(font)
        self.label_projects.setStyleSheet("color: rgb(6, 6, 6);")

        self.lineEdit_search_project = QtWidgets.QLineEdit()
        self.lineEdit_search_project.setStyleSheet("""
            QLineEdit {
                border-radius: 5px;
                padding: 3px;
                border: 1px solid #ccc;
            }
        """)

        self.comboBox_filter_project = QtWidgets.QComboBox()
        self.comboBox_filter_project.setStyleSheet("""
            QComboBox {
                border-radius: 5px;
                padding: 3px;
                border: 1px solid #ccc;
            }
        """)

        self.listWidget_project = QtWidgets.QListWidget()
        self.listWidget_project.setStyleSheet("""
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

        # Кнопки левой панели
        button_style = """
            QPushButton {
                border-radius: 6px;
                font-size: 11px;
                min-height: 40px;
            }
        """

        self.pushButton_open_project = QtWidgets.QPushButton("📂 Открыть проект")
        self.pushButton_open_project.setStyleSheet(button_style + """
            QPushButton {
                background: #000086;
                color: rgb(255, 255, 255);
                border: 1px solid #6ab0de;
            }
        """)

        self.pushButton_archive_project = QtWidgets.QPushButton("📦 Архивировать проект")
        self.pushButton_archive_project.setStyleSheet(button_style + """
            QPushButton {
                background: #f0d8b0;
                color: #5c4a32;
            }
        """)

        self.pushButton_refresh = QtWidgets.QPushButton("🔄 Обновить список")
        self.pushButton_refresh.setStyleSheet(button_style + """
            QPushButton {
                background: #e0e0e0;
                color: #333;
            }
        """)

        # Добавляем элементы в левую панель
        left_layout.addWidget(self.label_projects)
        left_layout.addWidget(self.lineEdit_search_project)
        left_layout.addWidget(self.comboBox_filter_project)
        left_layout.addWidget(self.listWidget_project, 1)  # Растягиваем по высоте
        left_layout.addWidget(self.pushButton_open_project)
        left_layout.addWidget(self.pushButton_archive_project)
        left_layout.addWidget(self.pushButton_refresh)

        # Правая панель (документы и превью)
        self.frame_right = QtWidgets.QFrame()
        self.frame_right.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)

        right_layout = QtWidgets.QVBoxLayout(self.frame_right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        # Верхняя правая панель (документы)
        self.frame_documents = QtWidgets.QFrame()
        self.frame_documents.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                border: 1px solid #3c3c3c;
            }
        """)

        documents_layout = QtWidgets.QVBoxLayout(self.frame_documents)
        documents_layout.setContentsMargins(20, 20, 20, 20)
        documents_layout.setSpacing(10)

        self.label_documents = QtWidgets.QLabel("ДОКУМЕНТАЦИЯ")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_documents.setFont(font)
        self.label_documents.setStyleSheet("color: #2a506d;")

        self.lineEdit_search_document = QtWidgets.QLineEdit()
        self.lineEdit_search_document.setStyleSheet("""
            QLineEdit {
                border-radius: 5px;
                padding: 3px;
                border: 1px solid #ccc;
            }
        """)

        self.listWidget_document = QtWidgets.QListWidget()
        self.listWidget_document.setStyleSheet("""
            QListWidget {
                border-radius: 6px;
                background-color: white;
                border: 1px solid #3c3c3c;
            }
        """)

        # Кнопки документов
        self.buttons_row1 = QtWidgets.QHBoxLayout()
        self.pushButton_create_doc = QtWidgets.QPushButton("📄 Создать новый документ")
        self.pushButton_export = QtWidgets.QPushButton("📤 Экспорт документов")

        self.pushButton_create_doc.setStyleSheet("""
            QPushButton {
                background: #008000;
                color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 11px;
                min-height: 30px;
            }
        """)

        self.pushButton_export.setStyleSheet("""
            QPushButton {
                background: #000086;
                color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 11px;
                min-height: 30px;
                border: 1px solid #6ab0de;
            }
        """)

        self.buttons_row1.addWidget(self.pushButton_create_doc)
        self.buttons_row1.addWidget(self.pushButton_export)

        self.buttons_row2 = QtWidgets.QHBoxLayout()
        self.pushButton_preview = QtWidgets.QPushButton("👁️ Предпросмотр документа")
        self.pushButton_delete_doc = QtWidgets.QPushButton("🗑️ Удалить документ")

        self.pushButton_preview.setStyleSheet("""
            QPushButton {
                background: #5c9cc4;
                color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 11px;
                min-height: 30px;
            }
        """)

        self.pushButton_delete_doc.setStyleSheet("""
            QPushButton {
                background: #cc0000;
                color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 11px;
                min-height: 30px;
            }
        """)

        self.buttons_row2.addWidget(self.pushButton_preview)
        self.buttons_row2.addWidget(self.pushButton_delete_doc)

        # Статус проекта
        self.status_row = QtWidgets.QHBoxLayout()
        self.label_status_project = QtWidgets.QLabel("Статус: не выбран")
        self.label_data_change_project = QtWidgets.QLabel("Обновлено: --.--.----")

        for label in [self.label_status_project, self.label_data_change_project]:
            label.setStyleSheet("""
                color: #5c9cc4;
                font-size: 10px;
            """)
            self.status_row.addWidget(label)

        # Добавляем элементы в панель документов
        documents_layout.addWidget(self.label_documents)
        documents_layout.addWidget(self.lineEdit_search_document)
        documents_layout.addWidget(self.listWidget_document, 1)  # Растягиваем по высоте
        documents_layout.addLayout(self.buttons_row1)
        documents_layout.addLayout(self.buttons_row2)
        documents_layout.addLayout(self.status_row)

        # Нижняя правая панель (превью)
        self.frame_preview = QtWidgets.QFrame()
        self.frame_preview.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                border: 1px solid #3c3c3c;
            }
        """)

        preview_layout = QtWidgets.QVBoxLayout(self.frame_preview)
        preview_layout.setContentsMargins(20, 20, 20, 20)
        preview_layout.setSpacing(10)

        self.label_preview = QtWidgets.QLabel("ПРЕДПРОСМОТР ДОКУМЕНТА")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_preview.setFont(font)
        self.label_preview.setStyleSheet("color: #2a506d;")

        self.textBrowser_preview = QtWidgets.QTextBrowser()
        self.textBrowser_preview.setStyleSheet("""
            QTextBrowser {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        preview_layout.addWidget(self.label_preview)
        preview_layout.addWidget(self.textBrowser_preview, 1)  # Растягиваем по высоте

        # Добавляем панели в правую часть
        right_layout.addWidget(self.frame_documents, 1)  # Растягиваем по высоте
        right_layout.addWidget(self.frame_preview)

        # Добавляем левую и правую панели в основную область
        main_content_layout.addWidget(self.frame_left)
        main_content_layout.addWidget(self.frame_right, 1)  # Растягиваем по ширине

        # Добавляем header и main в главный layout
        main_layout.addWidget(self.frame_header)
        main_layout.addWidget(self.frame_main, 1)  # Растягиваем по высоте

        # Обработчик изменения размера окна
        clerk.resizeEvent = self.resizeEvent

        self.retranslateUi(clerk)
        QtCore.QMetaObject.connectSlotsByName(clerk)

    def resizeEvent(self, event):
        """Обработчик изменения размера окна"""
        # Обновляем размер фонового изображения
        self.background_label.setGeometry(
            0, 0,
            event.size().width(),
            event.size().height()
        )
        event.accept()

    def retranslateUi(self, clerk):
        _translate = QtCore.QCoreApplication.translate
        clerk.setWindowTitle(_translate("clerk", "Гор-Строй: Делопроизводство"))
        self.label_title.setText(_translate("clerk", "ООО \"ГОР-СТРОЙ\""))
        self.label_projects.setText(_translate("clerk", "Список проектов"))
        self.lineEdit_search_project.setPlaceholderText(_translate("clerk", "Поиск проекта..."))
        self.comboBox_filter_project.addItem(_translate("clerk", "Все проекты"))
        self.comboBox_filter_project.addItem(_translate("clerk", "Активные"))
        self.comboBox_filter_project.addItem(_translate("clerk", "Архивные"))
        self.label_documents.setText(_translate("clerk", "ДОКУМЕНТАЦИЯ"))
        self.lineEdit_search_document.setPlaceholderText(_translate("clerk", "Поиск документа..."))
        self.label_preview.setText(_translate("clerk", "ПРЕДПРОСМОТР ДОКУМЕНТА"))
        self.label_status_project.setText(_translate("clerk", "Статус: не выбран"))
        self.label_data_change_project.setText(_translate("clerk", "Обновлено: --.--.----"))