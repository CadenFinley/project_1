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
    weight_limit = 0
    num_of_items = 0
    local_matrix: list[list[str | int]] = []
    for row in matrix:
        line = row.copy()
        if line:
            if len(line) == 2:
                weight_limit = int(line[1])
                num_of_items = int(line[0])
            elif len(line) == 3:
                local_matrix.append(line)
        else:
            break
    return local_matrix, weight_limit, num_of_items

def sort_by_value(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: x[2], reverse=True)

def sort_by_weight(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: x[1])

def sort_by_ratio(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: int(x[2]) / int(x[1]), reverse=True)


def greedy_value():
    print("Greedy by value:")
    current_weight = 0
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    
    local_matrix = sort_by_value(local_matrix)
    
    print(num_of_items)
    print(weight_limit)
    print_matrix(local_matrix)
    
def greedy_weight():
    print("Greedy by weight:")
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    
    local_matrix = sort_by_weight(local_matrix)
    
    print(num_of_items)
    print(weight_limit)
    print_matrix(local_matrix)
    
def greedy_ratio():
    print("Greedy by ratio:")
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    
    local_matrix = sort_by_ratio(local_matrix)
    
    print(num_of_items)
    print(weight_limit)
    print_matrix(local_matrix)
        

def main():
    global kp_file
    kp_file = sys.argv[1]
    read_file()
    greedy_value()
    greedy_weight()
    greedy_ratio()
   

if __name__ == "__main__":
    main()