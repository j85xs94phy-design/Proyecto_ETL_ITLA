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

    df = pd.read_csv("data/opiniones.csv")
    df.drop_duplicates(inplace=True)

    sql = """
    INSERT IGNORE INTO opiniones_encuestas
    (IdOpinion, IdCliente, IdProducto, Fecha, Comentario,
     Clasificacion, PuntajeSatisfaccion, Fuente)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, fila in df.iterrows():
        cursor.execute(sql, (
            fila["IdOpinion"],
            fila["IdCliente"],
            fila["IdProducto"],
            fila["Fecha"],
            fila["Comentario"],
            fila["Clasificación"],
            fila["PuntajeSatisfacción"],
            fila["Fuente"]
        ))

    conn.commit()
    conn.close()
    print("✔ Opiniones encuestas cargadas")
