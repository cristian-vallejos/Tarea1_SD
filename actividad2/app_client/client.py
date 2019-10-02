import socket
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000)) # Esto debería depender de la IP del server.

while True:
    message = input("Ingrese el mensaje a enviar (pulse ENTER para cerrar el cliente): ")
    if message == "":
        break
    else:
        client.send(("client | " + message).encode())
        server_answer = client.recv(2048).decode()
        print(server_answer)
        date_now = datetime.datetime.now()
        with open("registro_cliente.txt", "a+") as file:
            file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + server_answer + "\n")
client.close()