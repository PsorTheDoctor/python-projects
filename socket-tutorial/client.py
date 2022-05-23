import socket

header = 64
port = 5050
format = 'utf-8'
disconnect_msg = 'Disconnected!'
server = '192.168.56.1'
address = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)


def send(msg):
    msg = msg.encode(format)
    msgLength = str(len(msg)).encode(format)
    msgLength += b' ' * (header - len(msgLength))

    client.send(msgLength)
    client.send(msg)
    print(client.recv(2048).decode(format))


send('Hello World!')
send(disconnect_msg)
