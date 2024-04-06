import sqlite3
import pandas as pd

con = sqlite3.connect('agenda.db') #conexao com o banco

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS CONTATO"+
            " (nome varchar(100), endereco varchar(100), telefone varchar(20))")

resultado = cur.execute("insert into CONTATO (nome,endereco,telefone)values"+
                        "('Victoria', 'benassi@gmail.com', '11930290205')")
con.commit()

con.close()