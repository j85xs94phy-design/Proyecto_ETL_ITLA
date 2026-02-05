import pandas as pd
import mysql.connector

def run():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Wailedlizar223",
        database="analisis_opiniones"
    )
    cursor = conn.cursor()

    df = pd.read_csv("data/clientes.csv")
    df.drop_duplicates(inplace=True)

    sql = """
     INSERT IGNORE INTO clientes (IdCliente, Nombre, Email)
     VALUES (%s, %s, %s)
     """


    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdCliente"],
            fila["Nombre"],
            fila["Email"]
        ))

    conn.commit()
    conn.close()
    print("✔ Clientes cargados")
