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

    df = pd.read_csv("data/social_comments.csv")
    df.drop_duplicates(inplace=True)
           # Eliminamos filas con valores nulos en columnas críticas
    df = df.dropna(subset=[
    "IdComment",
    "IdCliente",
    "IdProducto",
    "Fuente",
    "Fecha",
    "Comentario"
    ])


    sql = """
    INSERT IGNORE INTO social_comments
    (IdComment,IdCliente,IdProducto,Fuente,Fecha,Comentario)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdComment"],
            fila["IdCliente"],
            fila["IdProducto"],
            fila["Fuente"],
            fila["Fecha"],
            fila["Comentario"]
        ))

    conn.commit()
    conn.close()
    print("✔ Comentarios sociales cargados")
