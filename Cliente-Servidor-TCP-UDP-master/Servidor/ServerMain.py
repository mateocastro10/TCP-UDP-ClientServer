from udpServerConfig import * 
from tcpServerConfig import *

def selectAnProtocol():
    answ = int(input('Seleccione el protocolo: 1- TCP  2-UDP'))
    return answ

if __name__ == '__main__':
    r = selectAnProtocol()
    if r==1 or r==2:
        if r==1:
            server = TCPServer(12000)
        else:
            server = UDPServer(12000)
    server.createSocket()
    server.receiveMessage()