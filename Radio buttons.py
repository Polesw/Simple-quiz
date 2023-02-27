from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton, QRadioButton, QHBoxLayout
from random import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Radio buttons')
main_win.resize(400,200)

def check_function():
    if rb1.isChecked():
        l1.setText("Correct")
        
    else:
        l1.setText("wrong")
    rb1.hide()
    rb2.hide()
    rb3.hide()
    rb4.hide()


l1 = QLabel("What is a man's best friend.")
rb1 = QRadioButton("Dog")
rb2 = QRadioButton("Cat")
rb3 = QRadioButton("Elephant")
rb4 = QRadioButton("Frog")
layout= QVBoxLayout()
hl1 = QHBoxLayout()
hl2 = QHBoxLayout()
pb = QPushButton("Submit")


layout.addWidget(l1)

hl1.addWidget(rb1)
hl1.addWidget(rb2)
hl2.addWidget(rb3)
hl2.addWidget(rb4)

pb.clicked.connect(check_function)
layout.addLayout(hl1)
layout.addLayout(hl2)
layout.addWidget(pb)
main_win.setLayout(layout)
main_win.show()
app.exec_()