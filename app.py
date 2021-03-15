from flask import Flask
from flask import render_template
from core.marvel import liste_perso

app = Flask(__name__)

@app.route('/')
def main():
    perso = liste_perso()
    return render_template('index.html', titre='Mon Site', nom='Ilano El Clandestino', perso=perso)

@app.route('/coucou/')
def coucou():
    return 'Coucou !'

if __name__ == '__main__':
    app.run(debug=True)
