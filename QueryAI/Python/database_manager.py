import sqlite3
import os

documents_path = os.path.join(os.path.expanduser("~"), "Documents")

folder_name = "QueryAI"

folder_path = os.path.join(documents_path, folder_name)

os.makedirs(folder_path, exist_ok=True)

db_path = os.path.join(folder_path, "appdata.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    description TEXT
)
""")

cursor.executemany("INSERT INTO appdata (subject, description) VALUES (?,?)",[
    ("Compra de frutas", "(descrição de teste) As frutas devem ser compradas no mercado x. Vermelhas ou amarelas"),
    ("Compra de pão", "Os pães devem ser comprados na padaria x. 6 francês e 6 de milho."),
    ("Anotação de jogo de sobrevivência", "A sobrevivência deve ser realista mas deve oferecer mecanicas as quais o jogador pode se aperfeiçoar"),
    ("Aplicativo QueryAI/Este aplicativo", "Este aplicativo foi feito para facilitar a organização de ideias e promover sua recuperação de forma mais rápida. Útil para quando se tem muitas notas"),
    ("Atividades físicas/exercícios físicos", "As atividades físicas devem ser feitas todos os dias, preferencialmente pela manhã, após o café da manhã.")
])

conn.commit()
conn.close()

print("Database 'appdata' was successfully created!")