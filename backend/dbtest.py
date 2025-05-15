import sqlite3

# Connexion à la base
conn = sqlite3.connect("instance/lobby.db")
cursor = conn.cursor()

# Lister toutes les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables dans la base :", tables)

# Pour chaque table, afficher les 5 premières lignes
for table in tables:
    table_name = table[0]
    print(f"\nContenu de la table {table_name} :")
    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Erreur en lisant {table_name} : {e}")

conn.close()
