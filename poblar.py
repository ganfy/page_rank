import sqlite3


def connectionBD():
    conexion = sqlite3.connect('data_base.db') 
    return conexion


def insertar_word_doc(word, doc):
    conexion_sqlite = connectionBD()
    cursor = conexion_sqlite.cursor()
    cursor.execute("INSERT INTO word_doc (word, doc) VALUES (?, ?)", (word, doc))
    conexion_sqlite.commit()
    conexion_sqlite.close()


def insertar_page_rank(id_doc, rank):
    conexion_sqlite = connectionBD()
    cursor = conexion_sqlite.cursor()
    cursor.execute("INSERT INTO page_rank (id_doc, rank) VALUES (?, ?)", (id_doc, rank))
    conexion_sqlite.commit()
    conexion_sqlite.close()


with open('archivo_inverted_index.txt', 'r') as archivo_word_doc:
    lineas_word_doc = archivo_word_doc.readlines()
    for linea in lineas_word_doc:
        palabra, documento = linea.strip().split('\t')
        insertar_word_doc(palabra, documento)


with open('archivo_page_rank.txt', 'r') as archivo_page_rank:
    lineas_page_rank = archivo_page_rank.readlines()
    for linea in lineas_page_rank:
        id_doc, rank = linea.strip().split('\t')
        insertar_page_rank(id_doc, rank)
