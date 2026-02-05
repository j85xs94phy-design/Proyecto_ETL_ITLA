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

    df = pd.read_csv("data/fuentes.csv")
    df.drop_duplicates(inplace=True)

    sql = """
    INSERT  IGNORE INTO fuentes (IdFuente, TipoFuente, FechaCarga)
    VALUES (%s, %s, %s)
    """

    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdFuente"],
            fila["TipoFuente"],
            fila["FechaCarga"]
        ))

    conn.commit()
    conn.close()
    print("✔ Fuentes cargadas")
