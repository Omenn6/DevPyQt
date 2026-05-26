import sys
import os
from datetime import datetime
from PySide6 import QtCore, QtWidgets


class ScanWorker(QtCore.QThread):
    progress_changed = QtCore.Signal(int, int)
    scan_finished = QtCore.Signal(int, int)
    log_message = QtCore.Signal(str)
    error_occurred = QtCore.Signal(str)

    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self._is_running = True

    def run(self) -> None:
        file_count = 0
        total_size = 0
        all_files = []

        self.log_message.emit(f"Старт сканирования директории: {self.folder_path}")

        try:
            for root, dirs, files in os.walk(self.folder_path):
                if not self._is_running:
                    return
                for file in files:
                    all_files.append(os.path.join(root, file))
        except Exception as e:
            self.error_occurred.emit(f"Ошибка доступа к папке: {str(e)}")
            return

        total_files = len(all_files)
        if total_files == 0:
            self.scan_finished.emit(0, 0)
            return

        for idx, file_path in enumerate(all_files, 1):
            if not self._is_running:
                self.log_message.emit("Сканирование отменено пользователем.")
                return

            try:
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)
                    file_count += 1
            except Exception:
                continue

            if idx % 10 == 0 or idx == total_files:
                self.progress_changed.emit(idx, total_files)
                QtCore.QThread.msleep(5)

        self.scan_finished.emit(file_count, total_size)

    def stop(self):
        self._is_running = False


class FolderScannerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Зачетная работа — Сканер папки")
        self.resize(550, 400)

        self.start_time = None
        self.worker = None

        self.initUi()

    def initUi(self) -> None:
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)

        path_layout = QtWidgets.QHBoxLayout()
        self.path_edit = QtWidgets.QLineEdit()
        self.path_edit.setPlaceholderText("Выберите папку для сканирования...")
        self.path_edit.setReadOnly(True)

        self.select_btn = QtWidgets.QPushButton("Обзор...")
        self.select_btn.clicked.connect(self.choose_folder)

        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(self.select_btn)
        main_layout.addLayout(path_layout)

        self.scan_btn = QtWidgets.QPushButton("Начать сканирование")
        self.scan_btn.setStyleSheet("font-weight: bold; height: 30px;")
        self.scan_btn.clicked.connect(self.start_scanning)
        main_layout.addWidget(self.scan_btn)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        self.log_edit = QtWidgets.QPlainTextEdit()
        self.log_edit.setReadOnly(True)
        main_layout.addWidget(self.log_edit)

        self.stats_label = QtWidgets.QLabel("Статистика: папка не выбрана")
        self.stats_label.setStyleSheet("font-size: 12px; color: #2c3e50;")
        main_layout.addWidget(self.stats_label)

    def choose_folder(self) -> None:
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            self.path_edit.setText(folder)
            self.stats_label.setText("Папка готова к сканированию")
            self.progress_bar.setValue(0)

    def start_scanning(self) -> None:
        folder_path = self.path_edit.text()
        if not folder_path or not os.path.exists(folder_path):
            QtWidgets.QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите корректную папку!")
            return

        self.start_time = datetime.now()

        self.scan_btn.setEnabled(False)
        self.select_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        self.log_edit.clear()

        self.worker = ScanWorker(folder_path)

        self.worker.progress_changed.connect(self.slot_update_progress)
        self.worker.scan_finished.connect(self.slot_scan_finished)
        self.worker.log_message.connect(lambda msg: self.log_edit.appendPlainText(msg))
        self.worker.error_occurred.connect(lambda err: QtWidgets.QMessageBox.critical(self, "Ошибка", err))

        self.worker.start()

    @QtCore.Slot(int, int)
    def slot_update_progress(self, current: int, total: int) -> None:
        self.progress_bar.setMaximum(total)
        self.progress_bar.setValue(current)
        self.stats_label.setText(f"Обработано файлов: {current} из {total}")

    @QtCore.Slot(int, int)
    def slot_scan_finished(self, file_count: int, total_size_bytes: int) -> None:
        end_time = datetime.now()

        size_in_mb = total_size_bytes / (1024 * 1024)

        self.stats_label.setText(
            f"Успешно завершено! Файлов: {file_count} | Общий размер: {size_in_mb:.2f} MB"
        )

        log_info = (
            f"\n--- ЛОГ ОПЕРАЦИИ ---\n"
            f"Время начала: {self.start_time.strftime('%H:%M:%S')}\n"
            f"Время завершения: {end_time.strftime('%H:%M:%S')}\n"
            f"Путь к папке: {self.path_edit.text()}\n"
            f"Результат: Найдено файлов: {file_count}, Размер: {size_in_mb:.2f} МБ\n"
        )
        self.log_edit.appendPlainText(log_info)

        self.scan_btn.setEnabled(True)
        self.select_btn.setEnabled(True)

    def closeEvent(self, event) -> None:
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.quit()
            self.worker.wait()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FolderScannerApp()
    window.show()
    sys.exit(app.exec())
