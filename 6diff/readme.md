How to run

./run_routers.sh






File: run_routers.sh
Runs n different routers with different port numbers according to the network configuration

File: router.py
The code reads a network configuration file called network.config and stores the adjacency matrix as objects of RouterIP. Each RouterIP object represents a node in the network and stores its IP address, its neighbors, and the cost to reach each neighbor.

The program then listens to UDP messages on a specific port number, which is passed as a command-line argument. The program then finds the corresponding RouterIP object for the given port number and binds a UDP socket to the IP address of the node.

The program then enters an infinite loop and listens for incoming UDP messages from its neighbors. When a message is received, the program updates its routing table by comparing the received neighbor table with its own neighbor table. If the received neighbor table has a shorter distance to a destination node than the current value in the program's neighbor table, the program updates its routing table.

The program then sends its neighbor table to its neighbors periodically to update their routing tables. If there are no updates in the routing table for a certain number of iterations, the program assumes that the routing table has converged and stops sending messages.

The code uses the socket library to create UDP sockets and send/receive messages. It also uses the json library to convert messages to JSON format for transmission. The program is executed from the command line with the port number as an argument.