import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        
        return self

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
    
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# nested loops runtime is O(n^2)
# using a binary search tree created with the first list of names will be O(n)
# we can then loop through the 2nd list of names, O(n)
# search for the current name in the BST, O(log(n))
# if the name exists in the BST append it to the duplicates list

# create BST with arbitrary first value
bst = BSTNode('optimization')

# loop through first list of names and insert into BST
for name in names_1:
    bst.insert(name)

# loop through the second list of names and check if BST contains name
# if does contain, add the name to duplicates list
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
