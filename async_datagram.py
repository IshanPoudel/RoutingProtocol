import asyncio

#once you have filled the router class. 
#Assigns different port numbers to each node depending on the start port number

port_number =5050

#Read the config file and create a 2d array
import sys
import socket


# -----------------------------------Create Router Class-----------------------------

#Create a  RouterIP class that stores the name of the local host e.g. "127.0.0.8" and 
# all its neighbors and the cost e.g. "127.0.0.7": 6 , "127.0.0.6" : 4 

class RouterIP:

    def __init__(self , name):
        self.name = name
        # Children is  a dictionary that contains the  config and the cost
        self.neighbor={}
        self.sock=None

    def add_neighbors(self , neighbor_dict):
        self.neighbor = neighbor_dict

    def add_sock(self , sock):
        self.sock=sock

    def __str__(self):
        return f"MyClass(portnumber={self.name} , neighbors = {self.neighbor})"

with open('network.config' , 'r') as f:
    matrix_config = f.read()

#Store the matrix_config
lines = matrix_config.splitlines()

matrix = []

for line in lines:
    if line == 'EOF':
        break
    numbers=line.split()
    row = []
    for each_number in numbers:
        row.append(int(each_number))
    matrix.append(row)

router_list=[]

#Store the adjacency matrix as objects of RouterIp
for index , matrix_row in enumerate(matrix):
    router_config = str(port_number+index) 
    router = RouterIP(router_config)
    
    neighbor_dict = {}

    print(matrix_row)
    # Get each value and see if it is a neighbor
    i=0
    for weight in matrix_row:
        #Check if neighbor
        if weight!=0:
            #Add to a dictionary
            neighbor_dict.update({  str(port_number+i) : weight})  
        i=i+1
    router.add_neighbors(neighbor_dict)
            

    
    #Store routerIP object in a list 
    router_list.append(router)

#Store the port number

#Router list contains all the ip config , neighbors and cost
for value in router_list:
    print(value.name)
    print(value.neighbor)
    print("\n")


#Router list containes name and neighbor-dict with ip address andport

#Create six different udp connections. 
socket_list=[]

for router in router_list:
    #For each router create a upd connection
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)

    #Bind the socket to address
    local_address = ('127.0.0.1' , int(router.name))
    sock.bind(local_address)
    router.add_sock(sock)




#Receive and send message async


async def receive_message(router, queue):
    sock = router.sock
    print(f"Starting receive loop for router {router.name}")
    sock.settimeout(1.0)
    while True:
        try:
            message, address = await loop.sock_recv(sock, 1024)
            print("Message that i received\n")
            message_str = message.decode()
            queue.put_nowait((message_str, address))
        except socket.timeout:
            pass

    



async def send_message(router, queue):
    sock = router.sock
    
    
    for port, weight in router.neighbor.items():
        port_int = int(port)
        
        message = f"Message from router {router} to port {port} with weight{weight}"
        print(message)
        # Send message from the sock to the other one
        sock.sendto(message.encode(), ('127.0.0.1', port_int))
        # print(f"I sent the {message}")
    # Check the queue for received messages
    #Get messages to come back
    




loop = asyncio.new_event_loop()

asyncio.set_event_loop(loop)
#Add a separate coroutine to add and separate tasks.
tasks = []

queue = asyncio.Queue()

for router in router_list:
    # Start the receive_message and send_message coroutines for each router
    send_task = loop.create_task(send_message(router, queue))
    
    if router.name == "5050":
        pass
    else:
        receive_task = loop.create_task(receive_message(router, queue))
        tasks.append(receive_task)

    # Add the tasks to the list of tasks
    tasks.append(send_task)
    

# Run all the tasks concurrently
loop.run_until_complete(asyncio.wait(tasks))

loop.close()