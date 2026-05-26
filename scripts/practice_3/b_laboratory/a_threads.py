""" Модуль, в котором содержатся потоки Qt """
import time
import psutil
import requests  # Важно для работы погоды!
from PySide6 import QtCore

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent(interval=None)
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    # Сигнал для передачи словаря с данными погоды в интерфейс
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = True  # Меняем None на True, чтобы цикл работал

    def setDelay(self, delay) -> None:
        """ Метод для установки времени задержки обновления сайта """
        self.__delay = delay

    def run(self) -> None:
        """ Метод с бесконечным циклом запросов в фоновом потоке """
        while self.__status:
            try:
                # Делаем реальный запрос к сайту погоды
                response = requests.get(self.__api_url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    # Отправляем данные в интерфейс
                    self.weatherInfoReceived.emit(data)
            except Exception as e:
                print(f"Ошибка сети: {e}")

            # Засыпаем на указанное время (чтобы не вешать процессор)
            time.sleep(self.__delay)

    def stop(self) -> None:
        """ Метод для остановки цикла """
        self.__status = False