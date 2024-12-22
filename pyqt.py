from PyQt5.QtCore import Qt

from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Raja Agus")

but = QPushButton('Generate')
text = QLabel('Raja Agus')
winner = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(but, alignment=Qt.AlignCenter)
my_win.setLayout(line)

def show_winner():
    number = randint(0,3)
    winner.setText(str(number))
    text.setText('Pemenang:')

my_win.show()
but.clicked.connect(show_winner)
app.exec_()
