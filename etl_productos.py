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

    df = pd.read_csv("data/productos.csv")
    df.drop_duplicates(inplace=True)

    sql = """
    INSERT IGNORE INTO productos (IdProducto, Nombre, Categoria)
    VALUES (%s, %s, %s)
    """

    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdProducto"],
            fila["Nombre"],
            fila["Categoria"]
        ))

    conn.commit()
    conn.close()
    print("✔ Productos cargados")
