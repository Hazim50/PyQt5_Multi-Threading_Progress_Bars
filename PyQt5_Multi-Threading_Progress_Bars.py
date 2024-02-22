from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import time

class ThreadClass(QThread):
    any_signal = pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        cnt = 0
        while self.is_running:
            cnt += 1
            if cnt == 99:
                cnt = 0
            time.sleep(0.02)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        self.terminate()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thread Deneme")
        self.setGeometry(100, 100, 467, 191)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.pushButton = QPushButton("start1", self.centralwidget)
        self.pushButton.setGeometry(70, 30, 75, 23)
        self.pushButton.clicked.connect(self.start_worker_1)

        self.pushButton_2 = QPushButton("start2", self.centralwidget)
        self.pushButton_2.setGeometry(70, 60, 75, 23)
        self.pushButton_2.clicked.connect(self.start_worker_2)

        self.pushButton_3 = QPushButton("start3", self.centralwidget)
        self.pushButton_3.setGeometry(70, 90, 75, 23)
        self.pushButton_3.clicked.connect(self.start_worker_3)

        self.pushButton_4 = QPushButton("stop1", self.centralwidget)
        self.pushButton_4.setGeometry(150, 30, 75, 23)
        self.pushButton_4.clicked.connect(self.stop_worker_1)

        self.pushButton_5 = QPushButton("stop2", self.centralwidget)
        self.pushButton_5.setGeometry(150, 60, 75, 23)
        self.pushButton_5.clicked.connect(self.stop_worker_2)

        self.pushButton_6 = QPushButton("stop3", self.centralwidget)
        self.pushButton_6.setGeometry(150, 90, 75, 23)
        self.pushButton_6.clicked.connect(self.stop_worker_3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(240, 30, 118, 23)

        self.progressBar_2 = QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(240, 60, 118, 23)

        self.progressBar_3 = QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(240, 90, 118, 23)

        self.threads = {}

    def start_worker_1(self):
        self.threads[1] = ThreadClass(parent=None, index=1)
        self.threads[1].start()
        self.threads[1].any_signal.connect(self.my_function)
        self.pushButton.setEnabled(False)

    def start_worker_2(self):
        self.threads[2] = ThreadClass(parent=None, index=2)
        self.threads[2].start()
        self.threads[2].any_signal.connect(self.my_function)
        self.pushButton_2.setEnabled(False)

    def start_worker_3(self):
        self.threads[3] = ThreadClass(parent=None, index=3)
        self.threads[3].start()
        self.threads[3].any_signal.connect(self.my_function)
        self.pushButton_3.setEnabled(False)

    def stop_worker_1(self):
        self.threads[1].stop()
        self.pushButton.setEnabled(True)

    def stop_worker_2(self):
        self.threads[2].stop()
        self.pushButton_2.setEnabled(True)

    def stop_worker_3(self):
        self.threads[3].stop()
        self.pushButton_3.setEnabled(True)

    def my_function(self, counter):
        cnt = counter
        index = self.sender().index
        if index == 1:
            self.progressBar.setValue(cnt)
        if index == 2:
            self.progressBar_2.setValue(cnt)
        if index == 3:
            self.progressBar_3.setValue(cnt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
