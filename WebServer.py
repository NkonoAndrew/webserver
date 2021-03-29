from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
#Prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The webserver is on port:", serverPort)
while True:
    #establish the connection
    print('Ready to serve')
    connectionSocket, adrr =  serverSocket.accept()

    try:
        message = connectionSocket.recvfrom(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #send one HTTP header line into socket
        message1 = "\nHTTP/1.1 200 OK \n"
        connectionSocket.send(message1.encode())

        #send the content of the requested file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        message2 = '\nHTTP1.1 404 Not Found\n'
        connectionSocket.send(message2.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
