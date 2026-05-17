import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QListWidget,
                               QRadioButton, QPushButton, QVBoxLayout, QButtonGroup)


class BookShopWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Книжный магазин")
        self.setFixedSize(450, 520)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                color: #9C27B0;
                font-weight: bold;
                font-size: 16px;
                margin-top: 10px;
                margin-bottom: 5px;
            }
            QListWidget {
                background-color: #2A2A2A;
                border: 1px solid #444444;
                padding: 5px;
                border-radius: 4px;
            }
            QListWidget::item {
                padding: 8px;
            }
            QListWidget::item:selected {
                background-color: #444444;
                color: #FFFFFF;
            }
            QRadioButton {
                padding: 4px;
            }
            QPushButton {
                background-color: #3A3A3A;
                border: 1px solid #555555;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
                margin-top: 15px;
            }
            QPushButton:hover {
                background-color: #4A4A4A;
            }
            QPushButton:pressed {
                background-color: #252525;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        label_books = QLabel("Выберите книгу")
        self.list_books = QListWidget()
        self.list_books.addItems([
            "Гарри Поттер и узник Азкабана Джоан Роулинг",
            "Благословение небожителей. Том 3 Мосян Тунсю",
            "Унесенные ветром Маргарет Митчелл"
        ])

        label_payment = QLabel("Выберите способ оплаты")

        self.radio_card = QRadioButton("По карте")
        self.radio_qr = QRadioButton("По QR")
        self.radio_cash = QRadioButton("Наличными")

        self.payment_group = QButtonGroup()
        self.payment_group.addButton(self.radio_card)
        self.payment_group.addButton(self.radio_qr)
        self.payment_group.addButton(self.radio_cash)
        self.radio_card.setChecked(True)

        self.btn_pay = QPushButton("Оплатить")

        layout.addWidget(label_books)
        layout.addWidget(self.list_books)
        layout.addSpacing(10)
        layout.addWidget(label_payment)
        layout.addWidget(self.radio_card)
        layout.addWidget(self.radio_qr)
        layout.addWidget(self.radio_cash)
        layout.addWidget(self.btn_pay)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookShopWindow()
    window.show()
    sys.exit(app.exec())
