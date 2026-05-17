"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущий основной монитор
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

import sys
from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        self.setWindowTitle("Проверка состояния окна")
        self.setMinimumSize(400, 300)
        self.resize(600, 500)

        main_layout = QtWidgets.QVBoxLayout(self)

        move_group = QtWidgets.QGroupBox("Перемещение окна")
        move_layout = QtWidgets.QHBoxLayout(move_group)

        move_layout.addWidget(QtWidgets.QLabel("X:"))
        self.spinX = QtWidgets.QSpinBox()
        self.spinX.setRange(0, 5000)
        move_layout.addWidget(self.spinX)

        move_layout.addWidget(QtWidgets.QLabel("Y:"))
        self.spinY = QtWidgets.QSpinBox()
        self.spinY.setRange(0, 5000)
        move_layout.addWidget(self.spinY)

        self.btnMove = QtWidgets.QPushButton("Переместить")
        move_layout.addWidget(self.btnMove)
        main_layout.addWidget(move_group)

        self.btnGetParams = QtWidgets.QPushButton("Получить параметры экрана")
        main_layout.addWidget(self.btnGetParams)

        main_layout.addWidget(QtWidgets.QLabel("Лог параметров экрана:"))
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        main_layout.addWidget(self.plainTextEdit)

        self.spinX.setValue(self.pos().x())
        self.spinY.setValue(self.pos().y())

    def initSignals(self) -> None:
        self.btnMove.clicked.connect(self.moveWindowByCoords)
        self.btnGetParams.clicked.connect(self.showScreenParams)

    def moveWindowByCoords(self) -> None:
        x = self.spinX.value()
        y = self.spinY.value()
        self.move(x, y)

    def getCurrentTimeStr(self) -> str:
        return QtCore.QDateTime.currentDateTime().toString("HH:mm:ss")

    def showScreenParams(self) -> None:
        app_instance = QtWidgets.QApplication.instance()
        screens = app_instance.screens()
        primary_screen = app_instance.primaryScreen()
        current_screen = self.screen()

        time_str = self.getCurrentTimeStr()

        state_list = []
        if self.isMinimized(): state_list.append("Свернуто")
        if self.isMaximized(): state_list.append("Развернуто")
        if self.isActiveWindow(): state_list.append("Активно")
        if self.isVisible(): state_list.append("Отображено")
        state_str = ", ".join(state_list) if state_list else "Нет состояния"

        info = (
            f"[{time_str}] --- Параметры системы ---\n"
            f" Кол-во экранов: {len(screens)}\n"
            f" Текущий основной монитор: {primary_screen.name()}\n"
            f" Разрешение текущего экрана: {current_screen.geometry().width()}x{current_screen.geometry().height()}\n"
            f" На каком экране окно находится: {current_screen.name()}\n"
            f" Размеры окна: {self.width()}x{self.height()}\n"
            f" Минимальные размеры окна: {self.minimumWidth()}x{self.minimumHeight()}\n"
            f" Текущее положение (координаты): X: {self.pos().x()}, Y: {self.pos().y()}\n"
            f" Координаты центра приложения: X: {self.geometry().center().x()}, Y: {self.geometry().center().y()}\n"
            f" Отслеживание состояния окна: {state_str}\n"
            f"{'-' * 40}\n"
        )
        self.plainTextEdit.appendPlainText(info)


    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        time_str = self.getCurrentTimeStr()
        old_pos = event.oldPos()
        new_pos = event.pos()
        print(
            f"[{time_str}] Перемещение окна -> Старая позиция: ({old_pos.x()}, {old_pos.y()}), Новая позиция: ({new_pos.x()}, {new_pos.y()})")

        self.spinX.setValue(new_pos.x())
        self.spinY.setValue(new_pos.y())
        super().moveEvent(event)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        time_str = self.getCurrentTimeStr()
        new_size = event.size()
        print(f"[{time_str}] Изменение размера окна -> Новый размер: {new_size.width()}x{new_size.height()}")
        super().resizeEvent(event)

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() in [QtCore.QEvent.Type.WindowStateChange, QtCore.QEvent.Type.ActivationChange]:
            time_str = self.getCurrentTimeStr()
            print(f"[{time_str}] Изменилось состояние окна (активность/сворачивание)")
        super().changeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
