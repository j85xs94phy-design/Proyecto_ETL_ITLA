import etl_clientes
import etl_productos
import etl_fuente_datos
import etl_resenas
import etl_opiniones
import etl_comentarios

def main():
    """
    Función principal del proyecto ETL.
    Ejecuta todos los procesos de carga en el orden correcto
    para evitar errores de claves foráneas y dependencias.
    """

    print("Iniciando proceso ETL...\n")

    # ---------------------------------------------
    # Carga de datos maestros
    # ---------------------------------------------
    etl_clientes.run()
    print("✓ Clientes cargados")

    etl_productos.run()
    print("✓ Productos cargados")

    etl_fuente_datos.run()
    print("✓ Fuentes de datos cargadas")

    # ---------------------------------------------
    # Carga de datos transaccionales
    # ---------------------------------------------
    etl_resenas.run()
    print("✓ Reseñas web cargadas")

    etl_opiniones.run()
    print("✓ Opiniones de encuestas cargadas")

    etl_comentarios.run()
    print("✓ Comentarios sociales cargados")

    print("\n🔥 ETL COMPLETADO SIN ERRORES")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
