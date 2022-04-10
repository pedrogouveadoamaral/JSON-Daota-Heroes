import json
import sqlite3
import pandas as pd

# Conecta com o BD
conexao = sqlite3.connect('dota2Heroes.db')
cursor = conexao.cursor()


select = "SELECT * FROM heroes"
cursor.execute(select)
dados = cursor.fetchall()

df = pd.DataFrame(dados).rename(columns={0: "id", 1: "name", 2: "attribute", 3: "attack", 4: "abilities"})
dataJson = df.to_json(orient='records', force_ascii=False)
print(dataJson)
toJson = json.loads(dataJson)
print(json.dumps(toJson, indent=4))

json_object = json.dumps(toJson, indent=4)
with open("heroesDota2.json", "w") as outfile:
     outfile.write(json_object)
