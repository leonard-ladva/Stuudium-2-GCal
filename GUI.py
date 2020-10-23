from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5 import QtCore
import sys
import os
import csv

CURR_DIR = os.path.dirname(os.path.realpath(__file__))


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stuudium to Google Calendar")

        self.setFixedSize(600, 400)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

        taust = f'{CURR_DIR}/taust.png'
        # Background image
        self.taust = QtWidgets.QLabel(self)
        self.taust.setPixmap(QPixmap(taust))
        self.taust.setGeometry(0, 0, 600, 400)

        # Stuudium login
        self.label1 = QtWidgets.QLabel('Stuudiumi login', self)
        self.label1.setFont(QFont('Arial', 24))
        self.label1.setGeometry(20, 170, 300, 30)
        self.label1.setStyleSheet('color:black')

        # Username
        self.label2 = QtWidgets.QLabel('Kasutajanimi', self)
        self.label2.setFont(QFont('Arial', 17))
        self.label2.setGeometry(50, 210, 300, 30)
        self.label2.setStyleSheet('color:black')

        # Password
        self.label3 = QtWidgets.QLabel('Salasõna', self)
        self.label3.setFont(QFont('Arial', 17))
        self.label3.setGeometry(50, 240, 300, 30)
        self.label3.setStyleSheet('color:black')

        # Stuudiumi URL
        self.label4 = QtWidgets.QLabel('Stuudiumi URL', self)
        self.label4.setFont(QFont('Arial', 17))
        self.label4.setGeometry(50, 270, 300, 30)
        self.label4.setStyleSheet('color:black')

        # Stuudiumi URL seletus
        self.label5 = QtWidgets.QLabel(
            'Logi stuudiumisse sisse ja kopeeri aadressiribalt URL', self)
        self.label5.setFont(QFont('Arial', 11))
        self.label5.setGeometry(55, 290, 300, 30)
        self.label5.setStyleSheet('color:black')

        # Google login
        self.label8 = QtWidgets.QLabel('Google login', self)
        self.label8.setFont(QFont('Arial', 24))
        self.label8.setGeometry(400, 170, 300, 30)
        self.label8.setStyleSheet('color:black')

        # Google link
        self.label9 = QtWidgets.QLabel(self)
        self.label9.setGeometry(400, 210, 200, 20)
        self.label9.setText(
            '< a href="https://developers.google.com/calendar/quickstart/python"> Vajuta siia < /a >')
        self.label9.setOpenExternalLinks(True)
        self.label9.setStyleSheet('color:black')

        # Google seletus
        self.label10 = QtWidgets.QLabel('ja avanenud lehel', self)
        self.label10.setGeometry(465, 210, 200, 20)
        self.label10.setStyleSheet('color:black')
        self.label11 = QtWidgets.QLabel('täida ära esimesed 2 sammu', self)
        self.label11.setGeometry(400, 230, 200, 20)
        self.label11.setStyleSheet('color:black')
        self.label12 = QtWidgets.QLabel('ning credentials.json fail aseta', self)
        self.label12.setGeometry(400, 250, 200, 20)
        self.label12.setStyleSheet('color:black')
        self.label13 = QtWidgets.QLabel('samasse kausta kus on', self)
        self.label13.setGeometry(400, 270, 200, 20)
        self.label13.setStyleSheet('color:black')
        self.label14 = QtWidgets.QLabel('programm', self)
        self.label14.setGeometry(400, 290, 200, 20)
        self.label14.setStyleSheet('color:black')

        # Field Username
        self.sisend1 = QtWidgets.QLineEdit(self)
        self.sisend1.setGeometry(180, 217, 150, 20)
        self.sisend1.setStyleSheet('background-color: white;border: 1px solid gray; color: black')

        # Field Password
        self.sisend2 = QtWidgets.QLineEdit(self)
        self.sisend2.setGeometry(180, 245, 150, 20)
        self.sisend2.setEchoMode(self.sisend2.Password)
        self.sisend2.setStyleSheet('background-color:white; border: 1px solid gray; color: black')

        # Field URl
        self.sisend3 = QtWidgets.QLineEdit(self)
        self.sisend3.setGeometry(180, 275, 205, 20)
        self.sisend3.setStyleSheet('background-color:white; border: 1px solid gray; color: black')

        silm = f'{CURR_DIR}/eye.png'
        # Button näita salasõna
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(325, 240, 65, 30)
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.show_password)
        self.button1.setIcon(QIcon(silm))

        # Button Start
        self.button3 = QtWidgets.QPushButton('Start', self)
        self.button3.setGeometry(490, 350, 70, 30)
        self.button3.setStyleSheet('color:black')
        self.button3.clicked.connect(self.start)

        self.show()

        try:
            andmed = open(f'{CURR_DIR}/andmed.txt')
            andmelugeja = csv.reader(andmed, delimiter='|')
            for rida in andmelugeja:
                self.sisend1.setText(rida[0])
                self.sisend2.setText(rida[1])
                self.sisend3.setText(rida[2])
            andmed.close()
        except IOError:
            print('no file')

    def show_password(self):
        if self.button1.isChecked():
            self.sisend2.setEchoMode(self.sisend2.Normal)
        else:
            self.sisend2.setEchoMode(self.sisend2.Password)

    def start(self):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        andmed = open(f'{CURR_DIR}/andmed.txt', 'w+')
        andmekirjutaja = csv.writer(andmed, delimiter='|')
        username = self.sisend1.text()
        password = self.sisend2.text()
        url = self.sisend3.text()
        andme = [username, password, url]
        print(andme)
        andmekirjutaja.writerow(andme)
        andmed.close()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
