# Sample Python code, showing how to sort
#  and how to use Queues

import sys
from queue import Queue

#++++++++++++++++++++++++++++
# each 'items' is a tuple: name (str), value (int), weight (int)
def useQueue(items):
    N = len(items) # N is number of items in list
    
    q = Queue()
    ready = Queue()
    # put two integers into the queue
    q.put(items[0][1])
    q.put(items[0][2])
    
    while not q.empty(): # while queue not empty
        v = q.get()
        if v < 100:
            q.put(v*2) # push 2v into queue
            q.put(v*v) # push v squared into queue
        else:
            print(f"v = {v}")
    
#++++++++++++++++++++++++++++
# each 'items' is a tuple: name (str), value (int), weight (int)
def putItInOrder(items):
    N = len(items) # N = number of items in list

    sortedItems = sorted(items, key=lambda x: x[0])
    print("When sorting by name (asc), the first item is:")
    print(sortedItems[0])

    sortedItems = sorted(items, key=lambda x: x[0],reverse=True)
    print("When sorting by name (desc), the first item is:")
    print(sortedItems[0])
    
    sortedItems = sorted(items, key=lambda x: x[1])
    print("When sorting by value (asc), the first item is:")
    print(sortedItems[0])

    sortedItems = sorted(items, key=lambda x: x[1],reverse=True)
    print("When sorting by value (desc), the first item is:")
    print(sortedItems[0])
    
    sortedItems = sorted(items, key=lambda x: x[2])
    print("When sorting by weight (asc), the first item is:")
    print(sortedItems[0])

    sortedItems = sorted(items, key=lambda x: x[2],reverse=True)
    print("When sorting by weight (desc), the first item is:")
    print(sortedItems[0])

    
    
#----------------------------------
#  MAIN
#----------------------------------

# make sure filename is provided
if len(sys.argv) < 2:
    print("Please provide filename at command-line.")
    quit()

# pull problem dataset from file
file = open(sys.argv[1],"r") # open file from which to read ("r")

# read count and max weight by
# taking first line from file, stripping off any spaces
# and splitting into two values (N,W) at the comma
N, W = file.readline().strip().split(',')
N = int(N) # store N as an integer (not string)
W = int(W) # store W as an integer (not string)

# make a list of N tuples, each with 3 values (initially empty strings and 0's)
items = [("",0,0) for _ in range(N)]
# replace those 0's with the values for each item
for r in range(N):
    name, value, weight = file.readline().strip().split(',')
    items[r] = (name, int(value), int(weight))
#print(items)

print()
print("<* Knapsack problem *>")
print(f"Weight limit: {W}")
print()
print(" Value Weight Name/Index")
print("-------------------------")
for x in range(len(items)):
    print(f" {items[x][1]:>4}   {items[x][2]:>4}    {items[x][0]}")

print()
print("Call the sample function useQueue")
useQueue(items)

print()
print("Call the sample function putItInOrder")
putItInOrder(items)
