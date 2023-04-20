
import socket

PORT = 5051
HOST = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST , PORT)
sock.bind(server_address)
print(f"Listening on {server_address[0]}:{server_address[1]}...")
