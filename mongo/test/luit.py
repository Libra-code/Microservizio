import pandas as pd
df = pd.read_csv('/home/tydragon/Documents/GitHub/ty-microservices/mongo/film.tsv', sep='\t')
print(df.to_json())
file = open("luit.json", "w") 
file.write(df.to_json())
file.close() 