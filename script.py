#Read the config file and create a 2d array

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




#Create a  RouterIP class that stores the name of the local host e.g. "127.0.0.8" and 
# all its neighbors and the cost e.g. "127.0.0.7": 6 , "127.0.0.6" : 4 

class RouterIP:

    def __init__(self , name):
        self.name = name
        # Children is  a dictionary that contains the  config and the cost
        self.neighbors={}

    def add_neighbors(self , neighbor_dict):
        self.neighbor = neighbor_dict


router_list=[]

#Store the adjacency matrix as objects of RouterIp
for index , matrix_row in enumerate(matrix):
    router_config = "127.0.0." + str(index+1)
    router = RouterIP(router_config)
    
    neighbor_dict = {}

    print(matrix_row)
    # Get each value and see if it is a neighbor
    i=0
    for weight in matrix_row:
        #Check if neighbor
        if weight!=0:
            #Add to a dictionary
            neighbor_dict.update({"127.0.0." + str(i+1) : weight})  
        i=i+1
    router.add_neighbors(neighbor_dict)
            

    
    #Store routerIP object in a list 
    router_list.append(router)



#Router list contains all the ip config , neighbors and cost
for value in router_list:
    print(value.name)
    print(value.neighbor)
    print("\n")


