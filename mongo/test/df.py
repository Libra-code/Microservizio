import pandas as pd
from pandas.io import json

dfa = pd.read_csv('C:/Users/timot/Documents/GitHub/ty-microservices/mongo/data/actors.tsv', sep='\t')
print(dfa.index)
dfa[['1','2','3','4']] =  dfa.titles.str.split(',',expand = True)
dfa.pop('titles')
dfa.pop('primaryProfession')
dfa.pop('nconst')

id = "tt0000001"

frames = [(dfa.loc[dfa['1'] == id]),  (dfa.loc[dfa['2'] == id]), (dfa.loc[dfa['3'] == id]), (dfa.loc[dfa['4'] == id])]
result = pd.concat(frames)
#print(result)
result.pop("1")
result.pop("2")
result.pop("3")
result.pop("4")
print(result.to_json(orient = 'records'))
