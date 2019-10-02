import socket, threading, struct
from _thread import *
import random, datetime

# Traspaso de mensajes cliente -> headnode -> datanode
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("", 5000))

print("Servidor iniciado.")
print("Esperando consultas por parte del cliente...\n")

def threaded(c):
    while True:
        data = c.recv(2048).decode().split(" | ")
        if data[0] == 'client':
            node = random.randint(0, 2)
            connection = connections[node]
            connection.send((str(node) + " | " + data[1]).encode())
        elif data[0] == 'datanode':
            date_now = datetime.datetime.now()
            connections[3].send(("Su mensaje '" + data[1].split("'")[1] +"' ha sido registrado en el datanode " + str(data[1].split(" ")[2]) + ".").encode())
            with open("registro_server.txt", "a+") as file:
                file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + data[1] + "\n")
        elif data[0] == "close":
            del connections[-1]
            break
    c.close()

connections = []

while True:
    server.listen(5)
    sock, address = server.accept()

    if len(connections) <= 3:
        start_new_thread(threaded, (sock,))
        if len(connections) < 3:
            print("Se ha creado satisfactoriamente un datanode.\n")
        elif len(connections) == 3:
            print("Se ha establecido conexión con el cliente.\n")
        connections.append(sock)
    else:
        print("El servidor no soporta más conexiones.\n")
