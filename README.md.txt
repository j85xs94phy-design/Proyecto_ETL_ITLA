# Sistema de Análisis de Opiniones de Clientes

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** utilizando **Python y MySQL** con el objetivo de analizar opiniones de clientes provenientes de distintas fuentes, como encuestas, reseñas web y redes sociales.  
El sistema permite centralizar la información, garantizar la integridad de los datos y facilitar su análisis posterior.

---

## Tecnologías utilizadas

- **Python** – Lenguaje principal del proyecto
- **Pandas** – Lectura y procesamiento de archivos CSV
- **MySQL** – Sistema de gestión de bases de datos relacional
- **MySQL Workbench** – Diseño del modelo entidad–relación y administración de la base de datos

---

## Estructura del proyecto

- `data/`  
  Contiene los archivos **CSV** utilizados como fuente de datos.

- `etl_*.py`  
  Scripts ETL independientes para cada entidad del sistema  
  (clientes, productos, fuentes, opiniones, reseñas y comentarios sociales).

- `main.py`  
  Archivo principal que **orquesta la ejecución del pipeline ETL completo**  
  en el orden correcto para evitar errores de claves foráneas.

---

## Flujo del proceso ETL

El pipeline sigue las siguientes etapas:

1. **Extracción**  
   Lectura de los datos desde archivos CSV utilizando Pandas.

2. **Transformación**  
   - Eliminación de registros duplicados  
   - Limpieza de valores nulos en columnas críticas  
   - Preparación de los datos para su inserción en la base de datos

3. **Carga**  
   Inserción de los datos en una **base de datos relacional MySQL**,  
   manteniendo la integridad referencial mediante claves primarias y foráneas.

---

## Ejecución del proyecto

Para ejecutar el proceso ETL completo, utilice el siguiente comando:

```bash
python main.py
