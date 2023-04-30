import socket

# Define the routing configuration
# Format: {source IP: {destination IP: (destination IP, destination port)}}
routing_config = {
    "127.0.0.1": {
        "127.0.0.2": ("127.0.0.2", 5001),
        "127.0.0.3": ("127.0.0.3", 5002),
    },
    "127.0.0.2": {
        "127.0.0.1": ("127.0.0.1", 5001),
        "127.0.0.4": ("127.0.0.4", 5003),
    },
    "127.0.0.3": {
        "127.0.0.1": ("127.0.0.1", 5002),
        "127.0.0.5": ("127.0.0.5", 5004),
    },
    "127.0.0.4": {
        "127.0.0.2": ("127.0.0.2", 5003),
        "127.0.0.6": ("127.0.0.6", 5005),
    },
    "127.0.0.5": {
        "127.0.0.3": ("127.0.0.3", 5004),
        "127.0.0.7": ("127.0.0.7", 5006),
    },
    "127.0.0.6": {
        "127.0.0.4": ("127.0.0.4", 5005),
        "127.0.0.8": ("127.0.0.8", 5007),
    },
    "127.0.0.7": {
        "127.0.0.5": ("127.0.0.5", 5006),
    },
    "127.0.0.8": {
        "127.0.0.6": ("127.0.0.6", 5007),
    },
}

# Create a UDP socket for each node
sockets = {}
for ip, destinations in routing_config.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, 0))  # Bind to any available port on the node's IP address
    sockets[ip] = sock

# Main loop to send and receive messages
while True:
    # Receive messages on any socket
    for ip, sock in sockets.items():
        data, addr = sock.recvfrom(1024)
        print(f"Received '{data.decode()}' from {addr[0]}:{addr[1]} on node {ip}")

        # Forward the message to the appropriate destination if it's in the routing configuration
        if addr[0] in routing_config[ip]:
            dest_ip, dest_port = routing_config[ip][addr[0]]
            sockets[dest_ip].sendto(data, (dest_ip, dest_port))

    # Prompt the user to send a message
    source_ip = input("Enter the source IP address: ")
    dest_ip = input("Enter the destination IP address: ")
    message = input("Enter the message to send: ")

    # Send the message if the source and destination are in the routing configuration
    if source_ip in routing_config and dest_ip in routing_config[source_ip]:
        dest_ip, dest_port = routing_config



