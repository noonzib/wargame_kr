from socket import *
from time import ctime

HOST = ''
PORT = 31337
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    tcpCliSock, addr = tcpSerSock.accept()
    print ('Connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
    
    tcpCliSock.close()
tcpSerSock.close