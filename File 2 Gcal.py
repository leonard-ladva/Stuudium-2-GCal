from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import csv
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
CURR_DIR = os.path.dirname(os.path.realpath(__file__))


def main():
    creds = None
    kalender = ''
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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
        with open('token.pickle', 'wb') as token:
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


if __name__ == '__main__':
    main()
