import socket

print("Creating socket object")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Getting local machine name")
host = socket.gethostname()

print("Connecting to hostname on the port")
port = 5050
client_socket.connect((host, port))

while True:
    # receive and print the server's message
    server_message = client_socket.recv(1024).decode('ascii')
    print(server_message)

    # send a message to the server
    message = input('Enter your message: ')
    client_socket.send(message.encode('ascii'))

# close the client socket
client_socket.close()
