"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import sys
from PySide6 import QtWidgets, QtCore
from a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Мониторинг Системы")
        self.resize(350, 180)

        self.initUi()

        self.sys_thread = SystemInfo()

        self.sys_thread.delay = self.delay_spin.value()

        self.sys_thread.systemInfoReceived.connect(self.update_info)

        self.sys_thread.start()

    def initUi(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        delay_layout = QtWidgets.QHBoxLayout()
        delay_label = QtWidgets.QLabel("Задержка обновления (сек):")
        self.delay_spin = QtWidgets.QSpinBox()
        self.delay_spin.setRange(1, 60)
        self.delay_spin.setValue(1)

        self.delay_spin.valueChanged.connect(self.change_delay)

        delay_layout.addWidget(delay_label)
        delay_layout.addWidget(self.delay_spin)
        layout.addLayout(delay_layout)

        self.cpu_label = QtWidgets.QLabel("Загрузка CPU: 0%")
        self.cpu_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.cpu_label)

        self.ram_label = QtWidgets.QLabel("Загрузка RAM: 0%")
        self.ram_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.ram_label)

    def update_info(self, data: list) -> None:
        cpu_value, ram_value = data
        self.cpu_label.setText(f"Загрузка CPU: {cpu_value}%")
        self.ram_label.setText(f"Загрузка RAM: {ram_value}%")

    def change_delay(self, value: int) -> None:
        if hasattr(self, 'sys_thread'):
            self.sys_thread.delay = value

    def closeEvent(self, event: QtCore.QEvent) -> None:
        self.sys_thread.quit()
        self.sys_thread.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SystemInfoWindow()
    window.show()
    sys.exit(app.exec())
