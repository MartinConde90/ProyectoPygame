import pygame
import sqlite3

BASE_DATOS = "Ranking.db"

def conexion(self):
    conn = sqlite3.connect('Ranking.db')

def insertar_tarea(self):
   
    query = 'INSERT INTO Ranking (Jugador, Puntuación) VALUES (?, ?)' #"los interrogantes son los valores de titulo etc"
    cursor.execute(query,(self.jugador, self.puntuacion))
    conn.commit()
    
       
    
    conn.close()

    query = "SELECT Jugador, Puntuación FROM Ranking order by point desc"
    filas = cursor.execute(query)
    for fila in filas:
        #fila es una tupla
        fila[0] #jugador
        fila[1] #puntuacion
        print(fila)

        #dbQuery para que en vez de una tupla, cree un diccionario, lo hicimos en flask 

def consulta(self):
    cursor = conn.cursor() #"es la herramienta que usamos para comunicarnos"
    query = "SELECT Jugador, Puntuación FROM Ranking order by point desc" #insertamos una tareas y escribimos la consulta que queremos
    filas = cursor.execute(query) #"en vez de query podriamos haber puesto la consulta directamente"
    for fila in filas:
        print(fila)


