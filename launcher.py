import winreg
from PyQt5.QtGui import QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PyQt5.QtCore import Qt, QSize
import sys
import os
import subprocess
import json

def _runprogram(program):
    with open("launcher_data.json", "r") as r:
        fil = json.load(r)
        try:
            fil[program] += 1
        except:
            fil[program] = 1
    with open("launcher_data.json", "w") as w:
        w.write(json.dumps(fil, indent=4))

    subprocess.Popen(["start", program], shell=True)

def reorder(buttons, layout):
    buttonY = 35
    if layout == "A - Z":
        for button in buttons:
            button.move(0, buttonY)
            buttonY += 30
    elif layout == "Z - A":
        for button in buttons[::-1]:
            button.move(0, buttonY)
            buttonY += 30
    elif layout == "Least Used":
        with open("launcher_data.json", "r") as r:
            fil = json.load(r)
            order = {k: v for k, v in sorted(fil.items(), key=lambda item: item[1])}
            

def launcher(win, vbox):
    """The launcher. Has its own gui.

    Args:
        win - A PyQt5.QtWidgets.QMainWindow window (self, which would actually be a QMainWindow anyways, if you're using an object-oriented approach)
    """
    aKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths")
    combo = QComboBox()
    combo.addItem("A - Z")
    combo.addItem("Z - A")
    combo.addItem("Least Used")
    vbox.addWidget(combo)
    buttonY = 0
    buttons = []
    for x in range(10000):
        try:
            a = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths" + "\\" + winreg.EnumKey(aKey, x))
            button = QtWidgets.QPushButton(winreg.EnumKey(aKey, x))
            text = button.text()
            button.move(0, buttonY)
            button.clicked.connect(lambda ch, text=text: _runprogram(text))
            vbox.addWidget(button)
            buttons.append(button)

            buttonY += 30
        except FileNotFoundError:
            continue
        except OSError:
            break
    combo.activated[str].connect(lambda text: reorder(buttons, text))

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        launcher(self, self.vbox)

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Launcher")

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.scroll = QScrollArea()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
