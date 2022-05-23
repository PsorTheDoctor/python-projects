import socket

header = 64
port = 5050
host = socket.gethostbyname(socket.gethostname())
address = (host, port)
format = 'utf-8'
disconnect_msg = 'Disconnected!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)


def handleClient(conn, address):
    print('New connection: {} connected'.format(address))

    while True:
        msgLength = conn.recv(header).decode(format)

        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(format)

            if msg == disconnect_msg:
                break

            print('{}: {}'.format(address, msg))
            conn.send('Message received'.encode(format))

    conn.close()


def start():
    server.listen()
    print('Server is listening on {}'.format(host))

    while True:
        conn, addr = server.accept()
        handleClient(conn, addr)


start()
