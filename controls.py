#!/usr/bin/pyton3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('Hi, there! push a button')
        okButton = QPushButton('ok')
        cancelButton = QPushButton('cancel')

        horizontal = QHBoxLayout()
        horizontal.addStretch(1)

        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addStretch(1)

        vertical.addWidget(label)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)
        self.setWindowTitle('Layout')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
