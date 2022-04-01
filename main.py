import json
from datetime import datetime
import sqlite3

database = "sqlite.db"
conn = sqlite3.connect(database)
cur = conn.cursor()
def formata_dados(arquivo):
	with open(arquivo) as file:
		dados_do_arquivo = file.read()
		#print(dados_do_arquivo)

	dados_do_arquivo = dados_do_arquivo.split("\n")
	dado_formatado = []
	for dado in dados_do_arquivo:
		dado = dado.strip("{ }").strip(" ").split(",")
		dado[1] = dado[1] + dado[2] + dado[3]
		del(dado[2])
		del(dado[2])
		
		dado = {dado[i].strip("' '").strip('" "'):dado[i+1].strip("' '").strip('" "') for i in range(0, len(dado), 2)}
		dado_formatado.append(dado)
	return dado_formatado

def apto_ao_bd(arquivo):
	dados = formata_dados(arquivo)
	b = 0
	for i in range(len(dados)-1):
		dif = datetime.strptime(dados[i+1]["dateTime"], "%Y-%m-%dT%H%M%S") - datetime.strptime(dados[i]["dateTime"], "%Y-%m-%dT%H%M%S")
		dif = dif.total_seconds()/60
		if dif!=15.0:
			b = b+1
			print(f"{dados[i]} apresenta diferença maior que 15 minutos de {dados[i+1]}")
			print(f"Arquivo '{arquivo}' apresenta irregularidades nos horários ")
		if b!=0:	
			return False
	return True
	

def posta_no_bd(arquivo):
	if apto_ao_bd(arquivo):
		id_us = arquivo[-5]
		nome_usina = "Usina "+id_us

		
		dados = formata_dados(arquivo)
		for dado in dados:
			value = dado["value"]
			data = dado["dateTime"].replace("-","").replace("T","/")
			cur.execute(f'INSERT INTO medicoes ( id_usina,data_hora ,geracao,nome_usina) VALUES ("{id_us}", "{data}", "{float(value)}", "{nome_usina}");')
			conn.commit()

posta_no_bd("dados_geracao_usina1.txt")
posta_no_bd("dados_geracao_usina2.txt")
posta_no_bd("dados_geracao_usina3.txt")
conn.close()