"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import sys
from PySide6 import QtWidgets

from b_systeminfo_widget import SystemInfoWindow
from c_weatherapi_widget import WeatherWindow

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Панель мониторинга")
        self.resize(450, 350)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        self.tabs = QtWidgets.QTabWidget()

        self.system_widget = SystemInfoWindow()
        self.weather_widget = WeatherWindow()

        self.tabs.addTab(self.system_widget, "Мониторинг системы")
        self.tabs.addTab(self.weather_widget, "Погода")

        main_layout.addWidget(self.tabs)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec())
