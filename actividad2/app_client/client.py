import socket
import random, datetime
from time import sleep

messages_dict = ["Hola", "Sistemas", "Mensaje de prueba", "Funciona!", "Saludos", "Distribuidos",
                "Bienvenido", "Mensaje hacia el servidor", "Mensaje de prueba", "Enviado", "Adiós",
                "INF343", "Sockets", "Enviando mensaje al headnode", "Funciona?", "exit"]

positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
probs = [0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.066, 0.01]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("headnode", 10000)) # Esto debería depender de la IP del server.

while True:
    message = messages_dict[random.choices(positions, probs)[0]]
    client.send(("client | " + message).encode())
    server_answer = client.recv(2048).decode()
    print(server_answer)
    date_now = datetime.datetime.now()
    with open("registro_cliente.txt", "a+") as file:
        file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + server_answer + "\n")
    if message == "exit":
        print("Se ha cerrado con éxito la conexión.")
        client.send(("close").encode())
        break
client.close()
