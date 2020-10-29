<h2>Stuudium to Google Calendar.py on lihtne püütonis kirjutatud GUI programm, mis leiab Stuudiumist kõik ülesanded(mis pole tehtuks märgitud) ning lisab need eraldi üritustena Google Kalendrisse.</h2>

<h3>Kuidas Kasutada</h3>
<h4>1. PIP installitud</h4>
  Sul peab olema PIP installitud, et sa saaksid installida kõiki vajalike püütoni mooduleid.
<a href='https://www.makeuseof.com/tag/install-pip-for-python/'>Siit lingilt</a> leiad kuidas installida PIP Windowsil, Macil ja Linuxil.
<h4>2. Google Calendar API sisse lülitatud</h4>
  Sul peab olema Google Calendar API sisse lülitatud selle Google'i konto peal kuhu sa tahad, et üritused tekiksid
<a href='https://developers.google.com/calendar/quickstart/python'>Siit lingilt</a> leiad nupu 'Enable Google Calendar API', enne selle vajutamist ole kindel, et oled õiges kontos.
<ol>
  <li> Vajuta 'Enable Google Calendar API'</li>
  <li> Vajuta 'Start' </li>
  <li> Vajuta 'Create' </li>
  <li> Vajuta 'Download Client Configuration</li>
  <li> Võid lehe sulgeda </li>
  <li> Tõsta alla laetud 'credentials.json' fail samasse kausta kus on programmi fail </li>
</ol>
<h4>3. Moodulid</h4>
  Programm kasutab järgnevaid Püütoni mooduleid, mis on vaja eraldi alla laadida:
  <ul>
  <li>PyQt5</li>
  <li>Selenium</li>
  <li>Beautiful Soup 4</li>
  <li>google-api-python-client </li>
  <li>google-auth-httplib2 </li>
  <li>google-auth-oauthlib</li>
 </ul>
 Kui sul on PIP installitud siis ava Terminal või cmd ja kopeeri sinna järgnev kood: <code>pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib PyQt5 Selenium bs4</code> ning vajuta enter.
  
</ul>
<h4>4. Chrome ja ChromeDriver</h4>
  Sul peab olema installitud <a href='https://www.google.com/chrome/'>Google Chrome brauser</a> ja <a href='https://chromedriver.chromium.org/downloads'>ChromeDriver</a>. Chromedriver-it on kõige lihtsam installida package manager-iga. Macil ja Linuxil installi <a href"https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/">Homebrew</a>, peale installimist ava terminali aken ja sisesta <code>brew cask install chromedriver</code>. Windowsil installi <a href"https://www.kenst.com/2019/02/installing-chromedriver-on-windows/">Chocolatey</a>, peale installimist ava cmd ja sisesta <code>choco install chromedriver</code>.

<h4>5. Thonnyga avamisel</h4>
 <li>Ava Thonny</li>
 <li>Vajuta "Tools"</li>
 <li>Vajuta "Options" Tools menüüst</li>
 <li>Vajuta "Interpreter"</li>
 <li>Vali nimekirjast "Alternative Python 3 Interpreter or environment"</li>
 <li>Nimekirjast, mis tekkis vali "Python 3", kui python 3 on mitu, siis vali üks ning katseta, kas programm töötab, kui ei, vali teine</li>
 
 <h3> Failid </h3>
Programmiga käivad kaasas kaks pilti: eye.png ja taust.png, need on GUI illustreerimiseks, lae need alla ja aseta samasse kasuta kus programmi fail.

 <h3> Trello </h3>
https://trello.com/b/DEG1ZsOM/proge
