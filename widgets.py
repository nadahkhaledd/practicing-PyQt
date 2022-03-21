#!/usr/bin/pyton3
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('Name')
        name_input = QLineEdit()
        button = QPushButton('set name')

        h = QHBoxLayout()
        h.addStretch(1)
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        v.addWidget(button)


        self.setLayout(v)
        self.setWindowTitle('Layout')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
