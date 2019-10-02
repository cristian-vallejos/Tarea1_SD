import socket


print('SERVIDOR INICIADO')
server_file_name = 'log.txt'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))
server.listen(10)

while True:
    conn, addr = server.accept()
    client_message = ''
    while True:
        data = conn.recv(4096).decode()
        if not data: break
        client_message += data
        file = open(server_file_name, "a+")
        file.write(str(addr[0]) + ":" + str(addr[1]) + " -> " + data + "\n")
        file.close()
        print("Mensaje recibido y registrado correctamente.\n")
        conn.send("El servidor ha recibido satisfactoriamente su mensaje.\n".encode())
    conn.close()
    print('Se ha perdido la conexión con el cliente.\n')
