import sqlite3
    
def listar_ativos():
        conn = sqlite3.connect("ativos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ativos")
        return cursor.fetchall()

def adionar_ativo(nome, tipo, status):
        conn = sqlite3.connect("ativos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ativos (nome, tipo, status)VALUE (?, ?, ?)", (nome, tipo, status) )
        conn.commit()
        conn.close()
        