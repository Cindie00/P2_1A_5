####################################################################@
#
# Extracteur de données de Kyllian pour l'exercice 3.1. ou sur le site web la Question 3
#
#####################################################################
import sqlite3
baseDeDonnees = sqlite3.connect('Base.sqlite')
cursor= baseDeDonnees.cursor()

# Total de veaux mort-nés par mois

def totalveauxmortnes():
    '''
    pre:/
    post: renvoie un dictionnaire avec le nombre de veaux morts-nés par mois
    '''
    nombre_mort_nes={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,}
    for ligne in cursor.execute("SELECT animaux_id, animaux.mort_ne, velages.date from animaux INNER JOIN velages ON animaux.id = velages.id WHERE animaux.mort_ne <>'8';"):
        nombre_mort_nes[ligne[2][3:5]]+=1
    return render_templates('graphiques/kyllian.html', data=nombre_mort_nes)


conn.commit()

