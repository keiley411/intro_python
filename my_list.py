my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Lists:", my_list)

# insert value at the second position
my_list.insert(1, 15)
print("New list:", my_list)

# extend my_list with another list
new_list= [50,60,70]

my_list.extend(new_list)
print("Extended list:", my_list)

# remove the last element from the list
my_list.remove(40)
print("Removed list:", my_list)

# sort my_list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# find and print the index of the value 30 in my_list
index = my_list.index(30)
print("Index of 30:", index)
