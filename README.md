# Stuudium-2-GCal
Stuudium-2-GCal adds all undone tasks in Stuudium as events in Google Calendar
<img width="612" alt="Screenshot 2023-11-29 at 14 33 07" src="https://github.com/leonard-ladva/Stuudium-2-GCal/assets/65786723/ff46fca3-d670-4c79-b8a8-04cf7eb94f89">

## This repo is not updated anymore, most likely it will not function as intended
[Stuudium](https://www.stuudium.com) is an Estonian eSchool platform.

## Requirements
1. Python 3.0+
2. PIP (package installer for python)
	[Install Pip For Python](https://www.makeuseof.com/tag/install-pip-for-python/)
3. Google Calendar API Enabled and credentials file downloaded
	Google Calendar API needs to be enabled for the account where you want the events.
	1. Navigate to [Enable Google Calendar API](https://developers.google.com/calendar/quickstart/python)
	2. Click `Enable Google Calendar API`
	3. Click `Start`
	4. Click `Create`
	5. Click `Download Client Configuration`
	6. Move `credentials.json` to the program folder
4. Google Chrome Browser
	[Google Chrome browser](https://www.google.com/chrome/)
5. Chrome Driver
	[MacOs](https://www.kenst.com/installing-chromedriver-on-mac-osx/)
	[Windows](https://www.kenst.com/installing-chromedriver-on-windows/)
## Installation
1. Clone this repo
2. Run `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib PyQt5 Selenium bs4` to install all required python modules
