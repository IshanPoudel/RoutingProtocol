import socket

# Create 8 UDP sockets
sockets = []
for i in range(8):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 5000 + i))  # Bind to a different port number for each socket
    sockets.append(sock)

# Send and receive data using each socket as needed
for i, sock in enumerate(sockets):
    # Example send-receive loop for socket i
    sock.sendto(b'Hello from socket %d' % i, ('127.0.0.1', 5000 + (i+1) % 8))  # Send data to the next socket in a circular manner
    data, addr = sock.recvfrom(1024)  # Receive data from any sender
    print('Socket %d received data: %s' % (i, data))