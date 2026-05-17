"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

import sys
from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyCompany", "WidgetInteractionApp")

        l = QtWidgets.QVBoxLayout()

        self.lcd_modes = {
            "dec": QtWidgets.QLCDNumber.Mode.Dec,
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
        }

        self.dial = QtWidgets.QDial()
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.onValueChanged)
        self.dial.installEventFilter(self)

        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.setMinimumHeight(60)
        self.lcd.setDigitCount(10)

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.onValueChanged)

        self.cb = QtWidgets.QComboBox()
        self.cb.addItems(list(self.lcd_modes.keys()))
        self.cb.currentTextChanged.connect(self.onModeChanged)

        l.addWidget(self.dial)
        l.addWidget(self.lcd)
        l.addWidget(self.slider)
        l.addWidget(self.cb)
        self.setLayout(l)

        self.loadSettings()

    def onValueChanged(self, value):
        self.dial.blockSignals(True)
        self.slider.blockSignals(True)

        self.dial.setValue(value)
        self.slider.setValue(value)
        self.lcd.display(value)

        self.dial.blockSignals(False)
        self.slider.blockSignals(False)

    def onModeChanged(self, mode):
        self.lcd.setMode(self.lcd_modes[mode])
        self.lcd.display(self.dial.value())

    def eventFilter(self, watched, event):
        if watched == self.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Minus:
                new_value = self.dial.value() - 1
                self.dial.setValue(new_value)
                print(f"Клавиатура (-): Новое значение = {self.dial.value()}")
                return True
            elif event.key() == QtCore.Qt.Key.Key_Plus:
                new_value = self.dial.value() + 1
                self.dial.setValue(new_value)
                print(f"Клавиатура (+): Новое значение = {self.dial.value()}")
                return True

        return super().eventFilter(watched, event)

    def loadSettings(self):
        saved_mode = self.settings.value("lcd_mode", "dec")
        saved_value = int(self.settings.value("lcd_value", 0))

        self.cb.setCurrentText(saved_mode)
        self.lcd.setMode(self.lcd_modes[saved_mode])

        self.onValueChanged(saved_value)

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.settings.setValue("lcd_mode", self.cb.currentText())
        self.settings.setValue("lcd_value", self.dial.value())
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
