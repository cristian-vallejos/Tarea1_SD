import socket
import datetime
from time import sleep

print('CLIENTE INICIADO')
client_file_name = 'respuestas.txt'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))  # Esto debería depender de la IP del server.
file = open(client_file_name, "a+")
for i in range(3):
    message = f"Mensaje {i}"
    client.send(message.encode())
    server_answer = client.recv(4096)
    date_now = datetime.datetime.now()
    print(server_answer.decode())
    file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + server_answer.decode())
    sleep(5)
file.close()
client.close()
