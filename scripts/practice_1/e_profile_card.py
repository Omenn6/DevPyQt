import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout


class ProfileCardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Карточка профиля")
        self.setFixedSize(450, 180)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                font-weight: bold;
                min-width: 80px;
            }
            QLineEdit {
                background-color: #2A2A2A;
                border: 1px solid #444444;
                padding: 6px;
                border-radius: 2px;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border: 1px solid #666666;
            }
        """)

        layout = QFormLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        self.input_last_name = QLineEdit()
        self.input_last_name.setPlaceholderText("Введите вашу фамилию")

        self.input_first_name = QLineEdit()
        self.input_first_name.setPlaceholderText("Введите ваше имя")

        self.input_middle_name = QLineEdit()
        self.input_middle_name.setPlaceholderText("Введите ваше отчество")

        self.input_phone = QLineEdit()
        self.input_phone.setPlaceholderText("Введите ваш телефон")

        layout.addRow("Фамилия", self.input_last_name)
        layout.addRow("Имя", self.input_first_name)
        layout.addRow("Отчество", self.input_middle_name)
        layout.addRow("Телефон", self.input_phone)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileCardWindow()
    window.show()
    sys.exit(app.exec())
