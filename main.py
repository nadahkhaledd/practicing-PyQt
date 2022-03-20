#!/usr/bin/pyton3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Page(QWidget):
    def __init__(self, parent = None):
        super(Page, self).__init__(parent)
        label = QLabel('first label')
        layout = QVBoxLayout()
        layout.addWidget(label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('first Qt App')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Page()
    window.show()
    sys.exit(app.exec())



