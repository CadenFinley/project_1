# caden and trent
import sys

matrix: list[list[str | int]] = []
kp_file = ""

def read_file():
    global matrix
    with open(kp_file, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(", ")
                if len(parts) == 2:
                    matrix.append([int(parts[0]), int(parts[1])])
                elif len(parts) == 3:
                    matrix.append([parts[0], int(parts[1]), int(parts[2])])
            else:
                matrix.append([])
                    
def print_matrix(local_matrix: list[list[str | int]]):
    for row in local_matrix:
        print(row)
        
def create_local_matrix():
    local_matrix: list[list[str | int]] = []
    for row in matrix:
        line = row.copy()
        if line:
            local_matrix.append(line)
        else:
            break
    return local_matrix

def greedy_value():
    time_elapsed = 0
    weight_limit = 0
    local_matrix = create_local_matrix()
    
    print_matrix(local_matrix)
    print(time_elapsed)
    
def greedy_weight():
    time_elapsed = 0
    weight_limit = 0
    local_matrix = create_local_matrix()
    
    print_matrix(local_matrix)
    print(time_elapsed)
    
def greedy_ratio():
    time_elapsed = 0
    weight_limit = 0
    local_matrix = create_local_matrix()
    
    print_matrix(local_matrix)
    print(time_elapsed)
        

def main():
    global kp_file
    kp_file = sys.argv[1]
    read_file()
    greedy_value()
    # print_matrix()
   

if __name__ == "__main__":
    main()