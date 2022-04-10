import json
import sqlite3


# Ler o arquivo JSON
with open("dotaHeroes.json", encoding='utf-8') as heroesJSON:
    heroes = json.load(heroesJSON)


# Conecta com o BD
conexao = sqlite3.connect('dota2heroes.db')
cursor = conexao.cursor()


# Função para criar a tabela  HEROES
def CreateTable():
    comandoCreate = f'CREATE TABLE IF NOT EXISTS HEROES (' \
              f'id INTEGER NOT NULL PRIMARY KEY,' \
              f'name TEXT NOT NULL,' \
              f'attribute TEXT,' \
              f'attack TEXT,' \
              f'abilities STRING)'
    print(comandoCreate)
    cursor.execute(comandoCreate)


def Heroes():
    for i in heroes:
        id = 1
        print(i['top10heroes'])
        for top10heroes in i['top10heroes']:
            # Tratar a string de powers
            chars = "[]"
            abilities = str(top10heroes["abilities"])
            for char in chars:
                abilities = abilities.replace(char, '')
            insert = f'INSERT INTO heroes (id, name, attribute, attack, abilities) ' \
                     f'VALUES ("{id}", "{top10heroes["name"]}", "{top10heroes["attribute"]}", ' \
                     f'"{top10heroes["attack"]}", "{abilities}")'
            print(insert)
            cursor.execute(insert)
            id += 1
        conexao.commit()


# Função para fazer uma query e imprimir os dados na tela
def Selecionar():
    select = "SELECT * FROM heroes"
    cursor.execute(select)
    dados = cursor.fetchall()
    for dado in dados:
        print(dado)
Selecionar()
