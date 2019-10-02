import socket, threading, struct, os
from _thread import *
import random, datetime
from time import sleep

print("Servidor iniciado.")
print("Esperando consultas por parte del cliente...\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("", 10000))

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
            print("Se ha perdido la conexión con el cliente.\n")
            break
    c.close()

connections = []
addresses = []

while True:
    server.listen(5)
    sock, address = server.accept()

    if len(connections) <= 3:
        start_new_thread(threaded, (sock,))
        connections.append(sock)
        if len(connections) <= 3:
            addresses.append("datanode" + str(len(connections)))
            print("Se ha creado satisfactoriamente un datanode.\n")
        elif len(connections) == 4:
            addresses.append("client")
            print("Se ha establecido conexión con el cliente.\n")

            while True:
                sleep(5)
                for i in addresses[0:3]:
                    with open("heartbeat_server.txt", "a+") as file:
                        response = os.system("ping -c 1 " + i)
                        date_now = datetime.datetime.now()
                        if response == 0:
                            file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> El " + i + " aun está activo.\n")
                        else:
                            file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> El " + i + " se encuentra inactivo.\n")
    else:
        print("El servidor no soporta más conexiones.\n")
