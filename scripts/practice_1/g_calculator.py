import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                               QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout)


class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(500, 320)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                font-weight: bold;
            }
            QLineEdit {
                background-color: #2A2A2A;
                border: 1px solid #444444;
                padding: 8px;
                border-radius: 4px;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #3A3A3A;
                border: 1px solid #555555;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #4A4A4A;
            }
            QPushButton:pressed {
                background-color: #252525;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        self.input_first = QLineEdit()
        self.input_first.setPlaceholderText("Введите первое число")

        self.input_second = QLineEdit()
        self.input_second.setPlaceholderText("Введите второе число")

        form_layout.addRow("Первое число:", self.input_first)
        form_layout.addRow("Второе число:", self.input_second)
        main_layout.addLayout(form_layout)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)

        self.btn_add = QPushButton("+")
        self.btn_sub = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_div = QPushButton("/")

        buttons_layout.addWidget(self.btn_add)
        buttons_layout.addWidget(self.btn_sub)
        buttons_layout.addWidget(self.btn_mul)
        buttons_layout.addWidget(self.btn_div)
        main_layout.addLayout(buttons_layout)

        self.label_result = QLabel("0")
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_result.setStyleSheet("""
            color: #4CAF50; 
            font-size: 48px; 
            font-weight: bold;
            margin-top: 15px;
        """)
        main_layout.addWidget(self.label_result)

        self.setLayout(main_layout)

        self.btn_add.clicked.connect(lambda: self.calculate("+"))
        self.btn_sub.clicked.connect(lambda: self.calculate("-"))
        self.btn_mul.clicked.connect(lambda: self.calculate("*"))
        self.btn_div.clicked.connect(lambda: self.calculate("/"))

    def calculate(self, operation):
        try:
            num1 = float(self.input_first.text().replace(",", "."))
            num2 = float(self.input_second.text().replace(",", "."))
        except ValueError:
            self.label_result.setText("Ошибка")
            self.label_result.setStyleSheet("color: #F44336; font-size: 32px; font-weight: bold; margin-top: 15px;")
            return

        self.label_result.setStyleSheet("color: #4CAF50; font-size: 48px; font-weight: bold; margin-top: 15px;")

        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                self.label_result.setText("div/0")
                self.label_result.setStyleSheet("color: #F44336; font-size: 32px; font-weight: bold; margin-top: 15px;")
                return
            res = num1 / num2

        if res.is_integer():
            self.label_result.setText(str(int(res)))
        else:
            self.label_result.setText(f"{res:.4f}".rstrip('0').rstrip('.'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
