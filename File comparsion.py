import csv
import os

# Paneb kõik ülesanded uus.txt failis järjendisse uus ja kõik ülesanded
# vana.txt failis järjendisse vana, võrdleb kõiki vana ja uue järjendi
# elemente ning eemaldab uuest kõik ülesanded mis vanas juba olemas.
# Loob uue vana.txt faili ning paneb kogu järgijäänud uus järjendi sisu sinna


CURR_DIR = os.path.dirname(os.path.realpath(__file__))

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
