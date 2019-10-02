import socket, struct
import datetime

# Traspaso de mensajes cliente -> headnode -> datanode
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000)) # Esto debería depender de la IP del server.

while True:
    data = client.recv(2048)
    headnode_message = data.decode().split(" | ")
    if (headnode_message[0] == "0") or (headnode_message[0] == "1") or (headnode_message[0] == "2"):
        date_now = datetime.datetime.now()
        answer = ("datanode | El datanode " + headnode_message[0] + " ha registrado satisfactoriamente el mensaje: '" + headnode_message[1] + "'.\n").encode()
        client.send(answer)
        with open("data" + headnode_message[0] + ".txt", "a+") as file:
            file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + headnode_message[1] + "\n")
    #elif headnode_message[0] == "close":
        #break;
client.close()
