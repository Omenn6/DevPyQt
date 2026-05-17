import sys
import random
from PySide6 import QtWidgets, QtCore

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация интерфейса
        :return: None
        """

        # comboBox -----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Элемент 1")
        self.comboBox.addItem("Элемент 2")
        self.comboBox.addItems(["Элемент 3", "Элемент 4", "Элемент 5"])
        self.comboBox.insertItem(0, "")

        self.pushButtonComboBox = QtWidgets.QPushButton("Получить данные")

        layoutComboBox = QtWidgets.QHBoxLayout()
        layoutComboBox.addWidget(self.comboBox)
        layoutComboBox.addWidget(self.pushButtonComboBox)

        # lineEdit -----------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите текст")

        self.pushButtonLineEdit = QtWidgets.QPushButton("Получить данные")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEdit)
        layoutLineEdit.addWidget(self.pushButtonLineEdit)

        # textEdit -----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setPlaceholderText("Введите текст")

        self.pushButtonTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutTextEdit = QtWidgets.QHBoxLayout()
        layoutTextEdit.addWidget(self.textEdit)
        layoutTextEdit.addWidget(self.pushButtonTextEdit)

        # plainTextEdit ------------------------------------------------------
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText("Введите текст")

        self.pushButtonPlainTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutPlainTextEdit = QtWidgets.QHBoxLayout()
        layoutPlainTextEdit.addWidget(self.plainTextEdit)
        layoutPlainTextEdit.addWidget(self.pushButtonPlainTextEdit)

        # spinBox ------------------------------------------------------------
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(random.randint(-50, 50))

        self.pushButtonSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutSpinBox = QtWidgets.QHBoxLayout()
        layoutSpinBox.addWidget(self.spinBox)
        layoutSpinBox.addWidget(self.pushButtonSpinBox)

        # doubleSpinBox ------------------------------------------------------
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setValue(random.randint(-50, 50))

        self.pushButtonDoubleSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutDoubleSpinBox = QtWidgets.QHBoxLayout()
        layoutDoubleSpinBox.addWidget(self.doubleSpinBox)
        layoutDoubleSpinBox.addWidget(self.pushButtonDoubleSpinBox)

        # timeEdit -----------------------------------------------------------
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime().addSecs(random.randint(-10000, 10000)))

        self.pushButtonTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutTimeEdit = QtWidgets.QHBoxLayout()
        layoutTimeEdit.addWidget(self.timeEdit)
        layoutTimeEdit.addWidget(self.pushButtonTimeEdit)

        # dateTimeEdit -------------------------------------------------------
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addDays(random.randint(-10, 10)))

        self.pushButtonDateTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutDateTimeEdit = QtWidgets.QHBoxLayout()
        layoutDateTimeEdit.addWidget(self.dateTimeEdit)
        layoutDateTimeEdit.addWidget(self.pushButtonDateTimeEdit)

        # plainTextEditLog ---------------------------------------------------
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        self.pushButtonClearLog = QtWidgets.QPushButton("Очистить лог")

        layoutLog = QtWidgets.QHBoxLayout()
        layoutLog.addWidget(self.plainTextEditLog)
        layoutLog.addWidget(self.pushButtonClearLog)

        # main layout

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutComboBox)
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutTextEdit)
        layoutMain.addLayout(layoutPlainTextEdit)
        layoutMain.addLayout(layoutSpinBox)
        layoutMain.addLayout(layoutDoubleSpinBox)
        layoutMain.addLayout(layoutTimeEdit)
        layoutMain.addLayout(layoutDateTimeEdit)
        layoutMain.addLayout(layoutLog)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """

        self.pushButtonComboBox.clicked.connect(self.onPushButtonComboBoxClicked)
        self.pushButtonLineEdit.clicked.connect(self.onPushButtonLineEditClicked)
        self.pushButtonTextEdit.clicked.connect(self.onPushButtonTextEditClicked)
        self.pushButtonPlainTextEdit.clicked.connect(self.onPushButtonPlainTextEditClicked)
        self.pushButtonSpinBox.clicked.connect(self.onPushButtonSpinBoxClicked)
        self.pushButtonDoubleSpinBox.clicked.connect(self.onPushButtonDoubleSpinBoxClicked)
        self.pushButtonTimeEdit.clicked.connect(self.onPushButtonTimeEditClicked)
        self.pushButtonDateTimeEdit.clicked.connect(self.onPushButtonDateTimeEditClicked)
        self.pushButtonClearLog.clicked.connect(self.onPushButtonClearLogClicked)

        self.comboBox.currentTextChanged.connect(self.onComboBoxChanged)
        self.spinBox.valueChanged.connect(self.onSpinBoxChanged)
        self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeEditChanged)

    # slots --------------------------------------------------------------
    def onPushButtonLineEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка LineEdit: {self.lineEdit.text()}")

    def onPushButtonComboBoxClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка ComboBox: {self.comboBox.currentText()}")

    def onPushButtonTextEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка TextEdit: {self.textEdit.toPlainText()}")

    def onPushButtonPlainTextEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка PlainTextEdit: {self.plainTextEdit.toPlainText()}")

    def onPushButtonSpinBoxClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка SpinBox: {self.spinBox.value()}")

    def onPushButtonDoubleSpinBoxClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка DoubleSpinBox: {self.doubleSpinBox.value()}")

    def onPushButtonTimeEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(f"Кнопка TimeEdit: {self.timeEdit.time().toString('HH:mm:ss')}")

    def onPushButtonDateTimeEditClicked(self) -> None:
        self.plainTextEditLog.appendPlainText(
            f"Кнопка DateTimeEdit: {self.dateTimeEdit.dateTime().toString('dd.MM.yyyy HH:mm:ss')}")

    def onPushButtonClearLogClicked(self) -> None:
        self.plainTextEditLog.clear()

    def onComboBoxChanged(self, text: str) -> None:
        self.plainTextEditLog.appendPlainText(f"Смена элемента ComboBox: {text}")

    def onSpinBoxChanged(self, value: int) -> None:
        self.plainTextEditLog.appendPlainText(f"Смена значения SpinBox: {value}")

    def onDateTimeEditChanged(self, datetime: QtCore.QDateTime) -> None:
        self.plainTextEditLog.appendPlainText(f"Смена даты/времени: {datetime.toString('dd.MM.yyyy HH:mm:ss')}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
