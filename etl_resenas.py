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

    df = pd.read_csv("data/resenas.csv")
    df.drop_duplicates(inplace=True)

    sql = """
    INSERT IGNORE INTO resenas_web
    (IdReview, IdCliente, IdProducto, Fecha, Comentario, Rating)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdReview"],
            fila["IdCliente"],
            fila["IdProducto"],
            fila["Fecha"],
            fila["Comentario"],
            fila["Rating"]
        ))

    conn.commit()
    conn.close()
    print("✔ Reseñas web cargadas")
