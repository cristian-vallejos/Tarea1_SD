import socket, struct
import datetime, os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("headnode", 10000)) # Esto debería depender de la IP del server.

while True:
    data = client.recv(2048)
    headnode_message = data.decode().split(" | ")
    if (headnode_message[0] == "0") or (headnode_message[0] == "1") or (headnode_message[0] == "2"):
        try:
            os.mkdir('datanode' + headnode_message[0])
        except FileExistsError:
            print("Directory " , 'datanode' + str(headnode_message[0]) ,  " already exists")

        date_now = datetime.datetime.now()
        answer = ("datanode | El datanode " + headnode_message[0] + " ha registrado satisfactoriamente el mensaje: '" + headnode_message[1] + "'.").encode()
        client.send(answer)
        with open("datanode" + headnode_message[0] + "/data.txt", "a+") as file:
            file.write(date_now.strftime("%Y-%m-%d %H:%M:%S") + " -> " + headnode_message[1] + "\n")
    #elif headnode_message[0] == "close":
        #break;
client.close()
