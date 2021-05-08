#######################################################################
#
# extracteur de donées de cindie pour l'exercice 4.2. de la liste ou sur le site web la Question 2
#
##########################################################################

import sqlite3
conn = sqlite3.connect('Base.sqlite',check_same_thread=False)
cursor= conn.cursor()

##4.2.##

# Total de vaches par famille

def TotalDeVachesDansFamille():
  '''
  pre:/
  post: renvoie un dictionnaire avec le nombre(value) total de vaches par famille(key)
  '''
  familles={}
  for id_famille in cursor.execute("SELECT id FROM familles"):
    count=0
    for vache,famille in cursor.execute("SELECT id, famille_id FROM animaux "):
      if famille == id_famille:
        count += 1
        familles[famille]=count
  return familles

# Le nombre de vaches mortes prématurément par famille

def TotalDeVachesMortesParFamille():
  '''
  pre:/
  post: renvoie un dictionnaire avec le nombre(value) de vaches mortes par famille(key)
  '''
  familles = {}
  for id_famille in cursor.execute("SELECT id FROM familles"):
    count = 0
    for vache,famille in cursor.execute("SELECT id, famille_id FROM animaux WHERE decede= 1 "):
      if famille == id_famille:
        count += 1
        familles[famille] = count
  return familles

# Nombre de vaches vivantes par famille

def TotalDeVachesVivantesParFamille():
  '''
  pre:/
  post: renvoie un dictionnaire avec le nombre(value) de vaches vivantes par famille(key)
  '''
  VachesVivantes={}
  for famille in TotalDeVachesDansFamille().keys():
    VachesVivantes[famille]= int(TotalDeVachesDansFamille().values()) - int(TotalDeVachesMortesParFamille().values())
  return VachesVivantes
conn.commit()
conn.close()

