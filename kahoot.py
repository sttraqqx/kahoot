from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

def win():
    victory_win = QMessageBox()
    victory_win.setText('win')
    victory_win.exec_()

def lose():
    lose_win = QMessageBox()
    lose_win.setText('lose')
    lose_win.exec_()


app = QApplication([])

main_window = QWidget()


bt1 = QRadioButton("26 серпня 1995")
bt2 = QRadioButton("28 серпня 1990")
bt3 = QRadioButton("24 серпня 1991")
bt4 = QRadioButton("22 серпня 1999")

question = QLabel("Коли Україна стала незалежною?")

layout = QVBoxLayout()
layoutH1 = QHBoxLayout() 
layoutH2 = QHBoxLayout() 
layoutH3 = QHBoxLayout() 

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(bt1, alignment = Qt.AlignCenter)
layoutH2.addWidget(bt2, alignment = Qt.AlignCenter)
layoutH3.addWidget(bt3, alignment = Qt.AlignCenter)
layoutH3.addWidget(bt4, alignment = Qt.AlignCenter)

layout.addLayout(layoutH1)
layout.addLayout(layoutH2)
layout.addLayout(layoutH3)
main_window.setLayout(layout)

bt1.clicked.connect(lose) 
bt2.clicked.connect(lose) 
bt3.clicked.connect(win) 
bt4.clicked.connect(lose) 

main_window.show()
app.exec_()

