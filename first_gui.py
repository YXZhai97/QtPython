from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
import sys


def window():

    # set up the app at the first place
    app=QApplication([])

    # set up window
    win=QMainWindow()
    # set the window geometry
    # the position and width and length of the window
    win.setGeometry(600, 400, 800, 500 )

    # reset the window size and move the position
    # win.resize(400,400)
    # win.move(500,500

    win.setWindowTitle("Tech with Tim!")

    # add a label on window
    label = QtWidgets.QLabel(win)
    label.setText("Enter Data")
    label.move(30,30)

    # text editer
    textEdit=QPlainTextEdit(win)
    textEdit.setPlaceholderText("Please Enter the data")
    textEdit.move(30,60)
    textEdit.resize(200,400)

    # button
    button=QPushButton("Data Analyze", win)
    button.move(250,60)
    button.resize(120,30)
    button.clicked.connect(handle_analyze)

    win.show()

    # wait for the user input and interaction, dead loop
    app.exec_()

# button connection
def handle_analyze():
    info=textExit.

window()

