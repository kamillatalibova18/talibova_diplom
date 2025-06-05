import sys
import MySQLdb
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from auth import Auth_Form


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conn = MySQLdb.connect("localhost", "root", "root", "gor_stroy", charset="utf8mb4")
        self.cursor = self.conn.cursor()

        self.ui = Auth_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_auth.clicked.connect(self.auth)

    def auth(self):
        login = self.ui.lineEdit_log.text()
        password = self.ui.lineEdit_pass.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            self.cursor.execute("""
                SELECT role FROM Employee 
                WHERE login = %s AND password = %s
            """, (login, password))

            result = self.cursor.fetchone()

            if result:
                role = result[0]
                self.hide()  # Скрываем окно авторизации вместо закрытия

                if role == "инженер":
                    from engineer_logic import EngineerApp
                    self.engineer_app = EngineerApp()
                    self.engineer_app.show()
                elif role == "делопроизводитель":
                    from clerk_cod import Clerk_Window
                    self.clerk_app = Clerk_Window()
                    self.clerk_app.show()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")

        except MySQLdb.Error as e:
            QMessageBox.critical(self, "Ошибка БД", f"Ошибка подключения к БД: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())