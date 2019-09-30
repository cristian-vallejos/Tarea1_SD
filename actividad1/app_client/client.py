import socket
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000)) # Esto debería depender de la IP del server.
file = open("respuestas.txt", "a+")

while True:
    message = input("Ingrese el mensaje a enviar (pulse ENTER para cerrar el cliente): ")
    if message == "":
        break
    else:
        client.send(message.encode())
        server_answer = client.recv(4096)
        date_now = datetime.datetime.now()
        print(server_answer.decode())
        file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + server_answer.decode() + "\n")
file.close()
client.close()
