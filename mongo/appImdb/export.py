from __main__ import *
import pandas as pd
from pandas.io import json


#TODO aggiungere controllo per actor
def myActors(id):
  frames = [(dfa.loc[dfa['1'] == id]),  (dfa.loc[dfa['2'] == id]), (dfa.loc[dfa['3'] == id]), (dfa.loc[dfa['4'] == id])]
  result = pd.concat(frames)
  result.pop("1")
  result.pop("2")
  result.pop("3")
  result.pop("4")
  return(result.to_json(orient = 'records'))

def mySplit(array):
  array = array.split(',')
  str=""
  lenght= len(array)
  for i in range(lenght) :
    str += f'"{array[i]}"'
    if i<lenght-1:
     str+=", "   
  return(str)  

#dfm = pd.read_csv('/home/tydragon/Documents/GitHub/ty-microservices/mongo/film.tsv', sep='\t')
dfm = pd.read_csv('mongo/data/film.tsv', sep='\t')
#print(dfm.index)

#dfa = pd.read_csv('C:/Users/timot/Documents/GitHub/ty-microservices/mongo/data/actors.tsv', sep='\t')
dfa = pd.read_csv('mongo/data/actors.tsv', sep='\t')
#print(dfa.index)
#separa i 4 attori in 4 colonne separate
dfa[['1','2','3','4']] =  dfa.titles.str.split(',',expand = True)
dfa.pop('titles')
dfa.pop('primaryProfession')
dfa.pop('nconst')

#dfm.iloc[0, 2] riga, colonna

actorsForImport=[]

for x in range(25):
  jsontest= json.dumps(f'{{"Title": "{dfm.iloc[x, 2]}", "Start year": {dfm.iloc[x, 5]}, "genres": [{ mySplit(dfm.iloc[x, 8])} ], "actors": {myActors(dfm.iloc[x, 0])}}}')  
  filmJson= json.loads(jsontest)
  #print(filmJson)
  actorsForImport.append(filmJson)

#print(actorsForImport)


