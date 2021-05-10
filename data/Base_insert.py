import sqlite3
conn= sqlite3.connect('Base.sqlite')
cursor= conn.cursor()

data=['insert_animaux.sql', 'insert_animaux_types.sql', 'insert_animaux_velages.sql', 'insert_complications.sql', 'insert_familles.sql', 'insert_types.sql', 'insert_velages.sql', 'insert_velages_complications.sql']

for file in data:
    file=open(file,"r")
    for line in file.readlines():
        line=str(line)
        cursor.execute(line)

conn.commit()
conn.close()
