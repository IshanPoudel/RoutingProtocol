import socket
import threading

# define the IP address and port number for each socket
addresses = [("127.0.0.1", 5000+i) for i in range(6)]

def send_recv_messages(sock, dest_address):
    # send a message to the destination address
    message = "Hello from {}".format(sock.getsockname())
    sock.sendto(message.encode(), dest_address)

    # receive messages from all other sockets
    while True:
        data, source_address = sock.recvfrom(1024)
        if source_address != dest_address:
            print("Received '{}' from {}".format(data.decode(), source_address))

# create and start a thread for each socket
threads = []
for i in range(6):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addresses[i])
    for j in range(6):
        if i != j:
            dest_address = addresses[j]
            thread = threading.Thread(target=send_recv_messages, args=(sock, dest_address))
            threads.append(thread)
            thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()
