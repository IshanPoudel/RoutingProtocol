#Open router and specify the port. 
#once you have filled the router class. 
#Assigns different port numbers to each node depending on the start port number

import sys
import time


port_number = int(sys.argv[1])
start_port_number=5050

#Read the config file and create a 2d array

import socket

#-----------ENUM CLASS for ports-----------------

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

with open('/Users/user/Desktop/CSE4344ComputerNetworks/RoutingImplementation/6diff/network.config' , 'r') as f:
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
    router_config = str(start_port_number+index) 
    router = RouterIP(router_config)
    
    neighbor_dict = {}

    print(matrix_row)
    # Get each value and see if it is a neighbor
    i=0
    for weight in matrix_row:
        #Check if neighbor
        if weight!=0:
            #Add to a dictionary
            neighbor_dict.update({  str(start_port_number+i) : weight})  
        i=i+1
    router.add_neighbors(neighbor_dict)
            

    
    #Store routerIP object in a list 
    router_list.append(router)

#Store the port number

#Router list contains all the ip config , neighbors and cost
for value in router_list:
    print(value)



routing_table = router_list


#Need to know which node this is. 
#send and receive message udp connection

#Loop through therouterlist
actual_socket = router_list[0]
for router in router_list:
    if int(router.name) == port_number:
        actual_socket = router

print(actual_socket)

#once you get the actual socket , start sending and receiving messages to neighbours. 
#bind
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)

#Bind the socket to address , we get the port number from 
local_address = ('127.0.0.1' , int(actual_socket.name))
sock.bind(local_address)



def listen_and_send_udp(sock , router):

    print(router)


    update_flag = 1
    #No updates

    try:
        sock.settimeout(1.0)

        while True:
            try:
                data, source_address = sock.recvfrom(1024)
                message_received = data.decode()

                print("Received message: {}".format(message_received))

            except socket.timeout:
                pass

            #Send message to all its neighbors

            if update_flag==1:
                
                for port, weight in router.neighbor.items():
                    port_int = int(port)
                    
                    message = f"Message from router {router.name} to router {port} with weight {weight}"
                    
                    # Send message from the sock to the other one
                    sock.sendto(message.encode(), ('127.0.0.1', port_int))
                    print(message)
                update_flag=0
    except Exception as error:
        print(error)
        
# /Users/user/Desktop/CSE 4344 Computer Networks/RoutingImplementation/6diff/router.py

#Add a timeout for all scripts to open

time.sleep(10)
print(f"\n\n Starting to listen . Currently at router {actual_socket.name} \n\n")
listen_and_send_udp(sock , actual_socket)


