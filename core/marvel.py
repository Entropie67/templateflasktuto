
# https://docs.python.org/3/library/sqlite3.html

import sqlite3
from pprint import pprint

def liste_perso():
    connexion = sqlite3.connect('core/marvel.db')
    curseur = connexion.cursor()
    curseur.execute('''SELECT * FROM personnage ORDER BY puissance DESC''')
    personnes = curseur.fetchall()
    curseur.execute('''PRAGMA table_info(personnage)''')
    noms_champs = curseur.fetchall()
    perso = [dict(zip([t[1] for t in noms_champs], p)) for p in personnes]
    print(perso)
    for p in perso:
        print(f"{p['nom']} dit {p['surnom']} possède une puissance égale : {p['puissance']}")
    return perso

def power_up(id, power):
    connexion = sqlite3.connect('core/marvel.db')
    curseur = connexion.cursor()
    # https://sql.sh/cours/update
    sql = f'''UPDATE personnage 
        SET puissance = {power}
        WHERE idpersonnage = {id}'''
    curseur.execute(sql)
    connexion.commit()


