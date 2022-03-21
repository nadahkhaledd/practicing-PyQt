#!/usr/bin/pyton3

import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import *

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('main.qml'))

    window = engine.rootObjects()[0]
    window.show()
    sys.exit(app.exec_())
    
