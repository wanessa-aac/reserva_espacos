import sqlite3

#Função para inserir uma nova reserva no banco de dados
def reservar(nome, bloco, apartamento, local, data):
    connection = sqlite3.connect('reservas.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO reservas (nome, bloco, apartamento, local, data) VALUES (?, ?, ?, ?, ?)",
              (nome, bloco, apartamento, local, data))
    connection.commit()
    connection.close()

# Função para exibir as reservas em uma nova janela
def get_reservas():
    connection = sqlite3.connect('reservas.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    connection.close()
    return reservas
    



