import socket
import argparse

# Set up command line arguments
parser = argparse.ArgumentParser(description='UDP socket')
parser.add_argument('ip', type=str, help='IP address to bind the socket to')
parser.add_argument('-p', '--port', type=int, help='port number to bind the socket to')
args = parser.parse_args()

# Set the default port to 5050 if not provided
if args.port is None:
    args.port = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(args.ip)
# Bind the socket to the IP address and port
sock.bind((args.ip, args.port))

print(f'Listening on {args.ip}:{args.port}...')

# Start listening for messages
while True:
    # Receive a message
    data, address = sock.recvfrom(1024)
    print(f'Received message from {address}: {data.decode()}')

    # Send a message
    message = input('Enter a message to send: ')
    sock.sendto(message.encode(), address)
    print(f'Sent message to {address}: {message}')
