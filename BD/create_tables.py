import sqlite3

def crear_tablas():
    # Conectarse a la base de datos SQLite
    conexion_SQLite = sqlite3.connect('data_base.db')  # Reemplaza 'nombre_basededatos.db' con el nombre de tu base de datos SQLite
    cursor = conexion_SQLite.cursor()

    # Consulta SQL para crear la tabla word_doc
    consulta_word_doc = """
    CREATE TABLE IF NOT EXISTS word_doc (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      word TEXT NOT NULL,
      doc INTEGER NOT NULL
    );
    """
    cursor.execute(consulta_word_doc)

    # Consulta SQL para crear la tabla page_rank
    consulta_page_rank = """
    CREATE TABLE IF NOT EXISTS page_rank (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      id_doc INTEGER NOT NULL,
      rank DECIMAL(2,4) NOT NULL
    );
    """
    cursor.execute(consulta_page_rank)

    # Confirmar los cambios y cerrar la conexión
    conexion_SQLite.commit()
    conexion_SQLite.close()

# Llamar a la función para crear las tablas
crear_tablas()