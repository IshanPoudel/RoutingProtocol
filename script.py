#Read the config file and create a 2d array

with open('network.config' , 'r') as f:
    matrix_config = f.read()

#Store the matrix_config
lines = matrix_config.splitlines()

matrix = []

for line in lines:
    numbers=line.split()
    row = []
    for each_number in numbers:
        row.append(int(each_number))
    matrix.append(row)

print(matrix)

