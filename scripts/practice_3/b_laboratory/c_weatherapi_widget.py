"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import sys
from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler


class WeatherWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Мониторинг Погоды")
        self.resize(400, 250)

        self.weather_thread = None

        self.initUi()

    def initUi(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        coords_layout = QtWidgets.QHBoxLayout()

        self.lat_spin = QtWidgets.QDoubleSpinBox()
        self.lat_spin.setRange(-90.0, 90.0)
        self.lat_spin.setValue(55.75)
        self.lat_spin.setPrefix("Широта: ")

        self.lon_spin = QtWidgets.QDoubleSpinBox()
        self.lon_spin.setRange(-180.0, 180.0)
        self.lon_spin.setValue(37.62)
        self.lon_spin.setPrefix("Долгота: ")

        coords_layout.addWidget(self.lat_spin)
        coords_layout.addWidget(self.lon_spin)
        layout.addLayout(coords_layout)

        delay_layout = QtWidgets.QHBoxLayout()
        delay_label = QtWidgets.QLabel("Задержка обновления (сек):")
        self.delay_spin = QtWidgets.QSpinBox()
        self.delay_spin.setRange(1, 3600)
        self.delay_spin.setValue(10)
        delay_layout.addWidget(delay_label)
        delay_layout.addWidget(self.delay_spin)
        layout.addLayout(delay_layout)

        self.start_button = QtWidgets.QPushButton("Запустить мониторинг")
        self.start_button.clicked.connect(self.toggle_monitoring)
        layout.addWidget(self.start_button)

        self.weather_label = QtWidgets.QLabel("Данные не получены. Нажмите кнопку запуска.")
        self.weather_label.setWordWrap(True)
        self.weather_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(self.weather_label)

    def toggle_monitoring(self) -> None:
        if self.weather_thread is None or not self.weather_thread.isRunning():
            lat = self.lat_spin.value()
            lon = self.lon_spin.value()

            self.weather_thread = WeatherHandler(lat=lat, lon=lon)
            self.weather_thread.setDelay(self.delay_spin.value())
            self.weather_thread.weatherInfoReceived.connect(self.update_weather_info)

            self.weather_thread.start()

            self.set_inputs_enabled(False)
            self.start_button.setText("Остановить мониторинг")
        else:
            self.weather_thread.stop()
            self.weather_thread.quit()
            self.weather_thread.wait()

            self.set_inputs_enabled(True)
            self.start_button.setText("Запустить мониторинг")

    def set_inputs_enabled(self, enabled: bool) -> None:
        self.lat_spin.setEnabled(enabled)
        self.lon_spin.setEnabled(enabled)
        self.delay_spin.setEnabled(enabled)

    def update_weather_info(self, data: dict) -> None:
        current_weather = data.get("current_weather", {})
        temperature = current_weather.get("temperature", "Н/Д")
        windspeed = current_weather.get("windspeed", "Н/Д")

        info_text = (
            f"=== ТЕКУЩАЯ ПОГОДА ===\n"
            f"Температура: {temperature}°C\n"
            f"Скорость ветра: {windspeed} км/ч"
        )
        self.weather_label.setText(info_text)

    def closeEvent(self, event: QtCore.QEvent) -> None:
        if self.weather_thread and self.weather_thread.isRunning():
            self.weather_thread.stop()
            self.weather_thread.quit()
            self.weather_thread.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WeatherWindow()
    window.show()
    sys.exit(app.exec())
