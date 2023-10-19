import pandas as pd

df = pd.read_csv(r"C:Listaetl.csv")
user_ids = df['UserID'].tolist()

print("Lista de UserID:")
for user_id in user_ids:
    print(user_id)


nomes = df['UserID'].tolist()
nomes_ordenados = sorted(nomes)


print("\nLista de nomes em ordem alfabética:")
for i, nome in enumerate(nomes_ordenados, start=1):
    print(f"{i} - {nome}")