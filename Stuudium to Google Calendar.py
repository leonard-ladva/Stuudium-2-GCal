from __future__ import print_function
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys
import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CURR_DIR = os.path.dirname(os.path.realpath(__file__))


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stuudium to Google Calendar")

        self.setFixedSize(500, 300)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

        taust = f'{CURR_DIR}/taust.png'
        # Background image
        self.taust = QtWidgets.QLabel(self)
        self.taust.setPixmap(QPixmap(taust))
        self.taust.setGeometry(0, 0, 500, 300)

        # Stuudium login
        self.label1 = QtWidgets.QLabel('Stuudiumi login', self)
        self.label1.setFont(QFont('Arial', 24))
        self.label1.setGeometry(20, 160, 300, 30)
        self.label1.setStyleSheet('color:black')

        # Username
        self.label2 = QtWidgets.QLabel('Kasutajanimi', self)
        self.label2.setFont(QFont('Arial', 17))
        self.label2.setGeometry(50, 200, 300, 30)
        self.label2.setStyleSheet('color:black')

        # Password
        self.label3 = QtWidgets.QLabel('Salasõna', self)
        self.label3.setFont(QFont('Arial', 17))
        self.label3.setGeometry(50, 230, 300, 30)
        self.label3.setStyleSheet('color:black')

        # Field Username
        self.sisend1 = QtWidgets.QLineEdit(self)
        self.sisend1.setGeometry(180, 207, 150, 20)
        self.sisend1.setStyleSheet(
            'background-color: white;border: 1px solid gray; color: black')

        # Field Password
        self.sisend2 = QtWidgets.QLineEdit(self)
        self.sisend2.setGeometry(180, 235, 150, 20)
        self.sisend2.setEchoMode(self.sisend2.Password)
        self.sisend2.setStyleSheet(
            'background-color:white; border: 1px solid gray; color: black')

        silm = f'{CURR_DIR}/eye.png'
        # Button näita salasõna
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(325, 230, 65, 30)
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.show_password)
        self.button1.setIcon(QIcon(silm))

        # Button Start
        self.button3 = QtWidgets.QPushButton('Start', self)
        self.button3.setGeometry(410, 250, 70, 30)
        self.button3.setStyleSheet('color:black')
        self.button3.clicked.connect(self.start)

        # Username
        self.label4 = QtWidgets.QLabel('Tehtud!', self)
        self.label4.setFont(QFont('Arial', 17))
        self.label4.setGeometry(415, 220, 60, 30)
        self.label4.setStyleSheet('color:green')
        self.label4.setHidden(True)
        self.show()

        try:
            andmed = open(f'{CURR_DIR}/andmed.txt')
            andmelugeja = csv.reader(andmed, delimiter='|')
            for rida in andmelugeja:
                self.sisend1.setText(rida[0])
                self.sisend2.setText(rida[1])
            andmed.close()
        except IOError:
            print('Pole salvestatud andmeid')

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
        andme = [username, password]
        andmekirjutaja.writerow(andme)
        andmed.close()

        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)

        driver.get('https://tamme.ope.ee/auth')
        driver.find_element_by_name('data[User][username]').send_keys(username)
        driver.find_element_by_name('data[User][password]').send_keys(password)
        driver.find_element_by_xpath(
            '//*[@id="main_login_form"]/input[1]').click()
        time.sleep(1)
        page_source = driver.page_source
        driver.quit()
# Stuudium to File
        # Ülesannete faili avamine - 4
        with open(f'{CURR_DIR}/uus.txt', 'w+') as file:
            writer = csv.writer(file, delimiter='|')
            # Stuudiumi lehe protseseerimine BeautifulSoup mooduliga
            soup = BeautifulSoup(page_source, "lxml")
            # Kõikide ülesannete nimekiri
            alltasks = []

            # Leiab kõik ülesanded mis on juba tehtuks märgitud ja eemaldab
            for b in soup.find_all('div', class_='is_marked'):
                b.decompose()
            # Leiab kõik div elemendid klassiga 'todo_container' ehk ülesanded
            for a in soup.find_all('div', class_='todo_container'):
                alltasks.append(a)
            # Vaatab läbi kõik ülesanded nimekirjas
            for task in alltasks:
                # Saab kuupäeva imelikus formaadis

                d = task.get('data-date')

                # Muudab kuupäeva formaadi ümber
                kuupaev = str(d[0: 4] + '-' + d[-4:-2] + '-' + d[-2:])
                # Saab tunni nime
                tund = task.find('a', class_='subject_name').text
                # Saab tunni ulesande
                ulesanne = task.find('span', class_='todo_content').text

                # Kirjutab kuupäva, nime ja sisu faili
                writer.writerow([kuupaev, tund, ulesanne])
# File comparison
        uus = []
        vana = []
        try:
            uusfail = open(f'{CURR_DIR}/uus.txt')
            vanafail = open(f'{CURR_DIR}/vana.txt')

            vana_reader = csv.reader(vanafail, delimiter='|')
            uus_reader = csv.reader(uusfail, delimiter='|')

            for u in uus_reader:
                uus.append(u)
            for v in vana_reader:
                vana.append(v)

            # for index, uusul in enumerate(uus):
            #     for vanaul in vana:
            #         if uusul[2] == vanaul[2]:
            #             del uus[index]
            # : sulgudes tähendab, et tsükkel kasutab järjendi uus koopiat
            for uusul in uus[:]:
                if uusul in vana:
                    uus.remove(uusul)

            uusfail.close()
            vanafail.close()

        except IOError:
            uusfail = open(f'{CURR_DIR}/uus.txt')
            uus_reader = csv.reader(uusfail, delimiter='|')
            for u in uus_reader:
                uus.append(u)

        finally:
            vanafail = open(f'{CURR_DIR}/vana.txt', 'w+')
            csvwriter = csv.writer(vanafail, delimiter='|')
            csvwriter.writerows(uus)
            vanafail.close()

# File to Gcal
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None
        kalender = ''
        # The file token.pickle stores the user's access and refresh tokens,
        # and is created automatically when the authorization flow completes
        # for the first time.
        if os.path.exists(f'{CURR_DIR}/token.pickle'):
            with open(f'{CURR_DIR}/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'{CURR_DIR}/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'{CURR_DIR}/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        page_token = None
        while True:
            calendar_list = service.calendarList().list(
                pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                if calendar_list_entry['summary'] == 'Kodutööd':
                    kalender = calendar_list_entry['id']
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

        if kalender == '':
            calendar = {
                'summary': 'Kodutööd',
                'timeZone': 'Europe/Helsinki',
            }
            created_calendar = service.calendars().insert(
                body=calendar).execute()
            kalender = created_calendar['id']

        file = open(f'{CURR_DIR}/vana.txt')
        csv_reader = csv.reader(file, delimiter='|')
        for row in csv_reader:
            kuupaevnr = row[0]
            tund = row[1]
            ulesanne = row[2]
            event = {
                'summary': tund,
                'description': ulesanne,
                'start': {
                    'date': kuupaevnr,
                    'timeZone': 'Europe/Helsinki',
                },
                'end': {
                    'date': kuupaevnr,
                    'timeZone': 'Europe/Helsinki',
                },
            }
            event = service.events().insert(
                calendarId=kalender, body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))

        vanafail = open(f'{CURR_DIR}/vana.txt', 'a')
        csvwriter = csv.writer(vanafail, delimiter='|')
        csvwriter.writerows(vana)
        vanafail.close()

        self.label4.setHidden(False)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
