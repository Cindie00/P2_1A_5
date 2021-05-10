#############################
#
# Extracteur de donnés de Chong de l'exercice 2. ce qui équivaut à la Question 4 sur le site
#
#########################################################################################################@

import sqlite3
conn = sqlite3.connect('Base.sqlite')
cursor= conn.cursor()
    data=list(cursor.execute("SELECT mere_id, date FROM velages"))
    
def Velage():
    '''
    pre:/
    post: renvoie un dictionnaire avec le nombre de velages par année
    '''
    dico={}
    annee={}
    for x in data:       # on crée 2 dictionnaires avec le nombre de velages par années
        if dico.get(x[0],None) == None:
            dico[x[0]]=1
        else:
            dico[x[0]]+=1
        if annee.get(x[1][-4:],None) == None:
            annee[x[1][-4:]]={dico[x[0]]:1}
        
        else:
            if annee[x[1][-4:]].get(dico[x[0]],None) == None:
                annee[x[1][-4:]][dico[x[0]]]=1
            else:
                annee[x[1][-4:]][dico[x[0]]]+=1

    for a in annee:        #on récupère les donnés pour chaque année
        for i in range(1,8):
            if annee[a].get(i,None) == None:
                annee[a][i]=0
        
     return annee #on renvoie le dictionnaire avec les données du nombre de velages par an


conn.commit()

