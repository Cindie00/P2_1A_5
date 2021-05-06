##############################
#
# Fichier main.py du Projet 2 du Groupe 1A_5
# Après avoir suivi les instructions afin d'installer flask,
# il vous suffit de lancer le programme
#
################################################
#
#   ATTENTION: nous avons eu des soucis avec notre base de donnés comme expliqué dans le read me.
#              Ceci est la version non fonctionelle du site.
#              Si vous souhaitez voir a quoi notre site aurait pu ressembler aller voir le projet_visualisation.
#              si vous arriviez a trouver des petites erreurs et a nous aider a faire fonctionner notre site ca serait top!
#
####################################################################################################################


###  Les imports
#
#

from extractorkyllian import *
from extractormax import *
from extractorcindie import *
from extractorchong import *
from flask import Flask, render_template

#
#Lancement de Flask
#
app = Flask(__name__, template_folder='templates')
app.debug = True

#
#Route vers la page principale du site
#

@app.route("/LaFermeDes3Chenes")
def principal():
    '''
    pre:/
    post: relie les valeurs extraites des extractor.py à une valeur
          qui sera associée aux graphes dans le fichier interfacefinale2.html
    '''
    #MAX
    PourcentageParCycle= Pourcentages() # [40, 50, 10, 47, 80, 2, 49, 56, 57, 13, 50, 56, 67, 15, 67, 22, 44, 66, 88, 56, 8, 4, 10, 50, 60, 5, 6, 8]

    #CINDIE
    mortes =  list(TotalDeVachesMortesParFamille().values()) #[41,50,5,20,40,80,50,18,34,45,150]
    vivantes=  list(TotalDeVachesVivantesParFamille().values()) #[160,305,200,100,120,300,79,179,150,230,20]
    familles= list(TotalDeVachesVivantesParFamille().keys()) #['famille1','famille2','famille3','famille4','famille5','famille6','famille7','famille8','famille9','famille10','famille11']

    #KYLLIAN
    deces= list(totalveauxmortnes().values())  #[40,50,10,47,30,2,49,56,57,13,50,10]

    #CHONG
    #VelageX =['1986','1990','1998','2000','2001','2002','2007', '2010','2019','2020']
    #VelageS = [10,30,40,20,50,15,18,60,70,12]

    for a in Annee:
        for i in range(1, 8):
            if i == 1:
                VelageX.append("{}: {}er velage(s)".format(a, i))
            else:
                VelageX.append("{}: {}eme velage(s)".format(a, i))
    VelageS = []
    for a in Annee:
        for i in range(1, 8):
            VelageS.append(velage[a][i])

    return render_template('interfacefinale2.html', PourcentageVelagePleineLune=PourcentageParCycle, m=mortes, v=vivantes,f=familles, n=deces, VelageX=VelageX, VelageS=VelageS)


#lance le site web

if __name__ == '__main__':
    app.run()
