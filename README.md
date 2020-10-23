Programm koosneb praegu neljast alaprogrammist:
<ul>
<li>GUI.py</li>
<li>Std to file.py</li>
<li>File comparison.py</li>
<li>File to Gcal.py</li>
</ul>

<h3>GUI.py</h3>
Lihtne kasutajaliides mis on loodud PyQt5 mooduliga. Programm salvestab ka sisestatud info faili andmed.txt, et teisel kasutamisel enam andmeid sisestama ei peaks.

Selle failiga käivad kaasas taust.png ja eye.png kasutajaliidese ilustreerimiseks.

To do:
<ol>
<li>Lisada märge kui programm on lõpetanud töö</li>
</ol>

<h3>Std to file.py</h3>
Web-Scraping programm mis kasutab Beautiful Soup 4 ja requests moodulit, et saada stuudiumist ülesanded ning kirjutada need faili uus.txt. Ainuke programmi jupp mis seni ei tööta. Ei tööta, sest stuudiumi sisselogimislehel on javascripti kontroll mis ei lase ilma javascripti scripti execute-imata lehele sisse logida.

To do:
<ol>
<li>Leida viis kuidas programm saaks Javascripti execute-ida: 
<ul>
<li>Selenium - liiga keeruline nii lihtsa asja jaoks? Iga kasutaja peaks webdriveri endale alla laadima ja selle tööle saama</li>
<li>Scrapy - pole veel proovinud, võiks uurida</li>
<li>Html_requests - proovisin, tunudb et ei tööta, sest stuudiumi lehel render()-it kasutades leht ei refreshi nii et leht ei saa vist arugi et javascripti üritati execute- ida</li>
</ul>
</li>
<li>Lugeda ülesanded otse järjendisse mitte faili kirjutada</li>
</ol>

<h3>File comparison.py</h3>
Programm mis loeb uus.txt failist ülesanded listi ning võrdleb seda vana.txt faili ülesannetega ehk ülesannetega mis on Google Calendari juba üles laetud. Eemaldab uute ülesannete järjendist kõik mis olid juba olemas ning kirjutab kõik alles jäänud vana.txt faili.

<h3>File to Gcal.py</h3>
Kasutab Google Calendar API-d, et teha vana.txt failist loetud ülesanded üritusteks sinu google kalendris. Calendar API tegeleb sisse logimisega ise.
