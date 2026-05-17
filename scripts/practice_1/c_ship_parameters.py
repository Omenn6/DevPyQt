import sys
from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QLabel, QFormLayout, QVBoxLayout


class ShipParametersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Параметры корабля")
        self.setFixedSize(380, 280)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }
            QGroupBox {
                font-weight: bold;
                border: 1px solid #555555;
                margin-top: 10px;
                padding: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
        """)

        main_layout = QVBoxLayout()

        group_box = QGroupBox("Параметры корабля")
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        val_temp = QLabel("22 C")
        val_temp.setStyleSheet("color: #FFB300; border: 1px solid #555555; padding: 2px 10px;")

        val_leak = QLabel("Отсутствует")
        val_leak.setStyleSheet("color: #4CAF50; border: 1px solid #555555; padding: 2px 10px;")

        val_tank1 = QLabel("Норма")
        val_tank1.setStyleSheet("color: #4CAF50; border: 1px solid #555555; padding: 2px 10px;")

        val_tank2 = QLabel("Норма")
        val_tank2.setStyleSheet("color: #4CAF50; border: 1px solid #555555; padding: 2px 10px;")

        val_tank3 = QLabel("Норма")
        val_tank3.setStyleSheet("color: #4CAF50; border: 1px solid #555555; padding: 2px 10px;")

        form_layout.addRow(QLabel("Температура на борту"), val_temp)
        form_layout.addRow(QLabel("Разгерметизация"), val_leak)
        form_layout.addRow(QLabel("Бак №1"), val_tank1)
        form_layout.addRow(QLabel("Бак №2"), val_tank2)
        form_layout.addRow(QLabel("Бак №3"), val_tank3)

        group_box.setLayout(form_layout)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShipParametersWindow()
    window.show()
    sys.exit(app.exec())
