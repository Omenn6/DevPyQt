import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QLineEdit, QPushButton, QFormLayout, QVBoxLayout)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Авторизация")
        self.setFixedSize(400, 150)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #333333;
                border: 1px solid #555555;
                padding: 4px;
                border-radius: 3px;
                color: white;
            }
            QPushButton {
                background-color: #444444;
                border: 1px solid #666666;
                padding: 6px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QPushButton:pressed {
                background-color: #2A2A2A;
            }
        """)

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.label_login = QLabel("Login")
        self.input_login = QLineEdit()

        self.label_password = QLabel("Password")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # Скрываем ввод пароля

        self.btn_submit = QPushButton("Войти")

        form_layout.addRow(self.label_login, self.input_login)
        form_layout.addRow(self.label_password, self.input_password)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.btn_submit)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
