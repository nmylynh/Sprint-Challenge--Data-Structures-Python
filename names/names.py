import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
names1Bst = BinarySearchTree(names_1[0]) # init starting node
for i in range(1,len(names_1)): # for the rest of the names 1 - last
    names1Bst.insert(names_1[i]) # insert each one

for name in names_2:
    if names1Bst.contains(name): 
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds") # 0.14 seconds


