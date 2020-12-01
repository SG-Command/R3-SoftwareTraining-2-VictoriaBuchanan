import socket

SIZE = 54

# Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

while True:
    msg = s.recv(54)
    print(msg.decode("utf-8"))