# caden and trent

matrix: list[list[str | int]] = []
kp_file = "test_cases.kp"

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
                    
def print_matrix():
    for row in matrix:
        print(row)
        
def greedy_value():
    time_elapsed = 0
    print(time_elapsed)
    
def greedy_weight():
    time_elapsed = 0
    print(time_elapsed)
    
def greedy_ratio():
    time_elapsed = 0
    print(time_elapsed)
        

def main():
    read_file()
    print_matrix()
   

if __name__ == "__main__":
    main()