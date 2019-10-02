import socket
import datetime, random

messages_dict = ["Hola", "Sistemas", "Mensaje de prueba", "Funciona!", "Saludos", "Distribuidos",
                "Bienvenido", "Mensaje hacia el servidor", "Mensaje de prueba", "Enviado", "Adiós",
                "INF343", "Sockets", "Enviando mensaje al headnode", "Funciona?", "Ayuda", "exit"]

client_file_name = 'respuestas.txt'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("server", 5000))  # Esto debería depender de la IP del server.

while True:
    message = messages_dict[random.randint(0, len(messages_dict)-1)]
    client.send(message.encode())
    server_answer = client.recv(4096).decode()
    date_now = datetime.datetime.now()
    print(server_answer)
    with open(client_file_name, "a+") as file:
        file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + server_answer + "\n")
    if message == "exit":
        print("Se ha cerrado con éxito la conexión.")
        break
client.close()
