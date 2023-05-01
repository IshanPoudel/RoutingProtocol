import socket

# Define a function to create a UDP socket and bind it to a port
def create_socket(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    return sock

# Create 8 UDP sockets with different port numbers
sockets = [create_socket(port) for port in range(8000, 8008)]

# Send a message to each socket
for i, sock in enumerate(sockets):
    message = f"Hello from socket {i}".encode()
    sock.sendto(message, ('127.0.0.1', 9000))

# Receive a message from each socket
for i, sock in enumerate(sockets):
    data, address = sock.recvfrom(1024)
    print(f"Received message from socket {i}: {data.decode()}")


