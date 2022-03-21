#!/usr/bin/pyton3
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text = QLabel('Hello!')
        label = QLabel('Name')
        self.name_input = QLineEdit()

        self.button = QPushButton('set name')
        self.button.clicked.connect(self.alterName)
        self.button.setAutoDefault(True)
        self.name_input.returnPressed.connect(self.button.click)


        h = QHBoxLayout()
        h.addWidget(label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addStretch(1)
        v.addWidget(self.text)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)
        self.setWindowTitle('Layout')
        self.show()

    def alterName(self):
        input = self.name_input.text()
        self.text.setText('Hello, ' + input + '!\nLook at the window title.')
        self.setWindowTitle(input + "'s Window")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
