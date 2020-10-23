from bs4 import BeautifulSoup
import requests
import csv
import os

# Kasutajapõhised on:
# 1. Kautajanimi (Stuudium)
# 2. Salasõna (Stuudium)
# 3. Stuudiumi url (Sisselogitult)
# 4. Ülesannete faili nimi ja aukoht(path)

# Stuudiumi kasutajanimi ja salasõna - 1, 2
payload = {
    'data[User][username]': 'leonard ladva',
    'data[User][password]': 'username'
}

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

# request mooduliga veebilehe vaatamine
with requests.Session() as s:
    # Ülesannete faili avamine - 4
    with open(f'{CURR_DIR}/uus.txt', 'w+') as file:
        writer = csv.writer(file, delimiter='|')
        # Stuudiumi esileht kuhu sisestada sisse logimiseks vajalik info
        p = s.post('https://tamme.ope.ee/auth/', data=payload)
        # Sisselogitud stuudiumi leht - 3
        r = s.get('https://tamme.ope.ee/s/1590').text
        # Stuudiumi lehe protseseerimine BeautifulSoup mooduliga
        soup = BeautifulSoup(r, "lxml")
        # Kõikide ülesannete nimekiri
        print(r)
        alltasks = []

        # Leiab kõik div elemendid klassiga 'todo_container' ehk ülesanded
        for a in soup.find_all('div', class_='todo_container'):
            # Leiab kõik ülesanded mis on juba tehtuks märgitud ja eemaldab
            for b in soup.find_all('div', class_='is_marked'):
                b.extract()
            # Leiab kõik ülesanded mis on minevikus ja eemaldab
            for c in soup.find_all('div', class_='is_past'):
                c.extract()

            # Lisab ülesanded mis pole tehtud ega minevkus ülesannete nimekirja
            alltasks.append(a)
        # Vaatab läbi kõik ülesanded nimekirjas
        print(alltasks)
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
