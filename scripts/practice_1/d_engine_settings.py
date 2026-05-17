import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QSlider, QLabel, QHBoxLayout, QVBoxLayout


class EngineSettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Управление двигателями")
        self.resize(700, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;
                color: #FFFFFF;
                font-family: Arial;
                font-size: 13px;
            }
            QGroupBox {
                font-weight: bold;
                border: 1px solid #555555;
                margin-top: 15px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QSlider::groove:vertical {
                background: #444444;
                width: 4px;
                border-radius: 2px;
            }
            QSlider::handle:vertical {
                background: #FFFFFF;
                border: 1px solid #777777;
                height: 14px;
                width: 14px;
                margin: 0 -5px;
                border-radius: 7px;
            }
            QSlider::handle:vertical:hover {
                background: #DDDDDD;
            }
        """)

        main_layout = QVBoxLayout()

        group_box = QGroupBox("Управление основными двигателями")
        group_layout = QHBoxLayout()
        group_layout.setContentsMargins(20, 20, 20, 20)
        group_layout.setSpacing(30)

        def create_engine_control(label_text):
            v_layout = QVBoxLayout()
            v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            slider = QSlider(Qt.Orientation.Vertical)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(50)
            slider.setMinimumHeight(150)

            label = QLabel(label_text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            v_layout.addWidget(slider)
            v_layout.addSpacing(10)
            v_layout.addWidget(label)
            return v_layout

        for i in range(1, 5):
            group_layout.addLayout(create_engine_control(f"Двигатель №{i}"))

        group_layout.addSpacing(20)

        group_layout.addLayout(create_engine_control("Общая тяга"))

        group_box.setLayout(group_layout)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EngineSettingsWindow()
    window.show()
    sys.exit(app.exec())
