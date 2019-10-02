import socket

print("Servidor iniciado.")
print("Esperando consultas por parte del cliente...\n")

server_file_name = 'log.txt'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))
server.listen(10)

while True:
    conn, addr = server.accept()
    while True:
        data = conn.recv(4096)
        if not data: break
        print("Se ha establecido conexión con el cliente.\n")
        file = open(server_file_name, "a+")
        file.write(str(addr[0]) + ":" + str(addr[1]) + " -> " + data.decode() + "\n")
        file.close()
        print("Mensaje recibido y registrado correctamente.\n")
        conn.send(("El servidor ha recibido satisfactoriamente su mensaje '" + data.decode() + "'.").encode())
    print('Se ha perdido la conexión con el cliente.\n')
    conn.close()
server.close()
