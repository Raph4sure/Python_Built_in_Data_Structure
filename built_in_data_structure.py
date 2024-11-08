#python 3.7

# 1. Create an empty list called my_list.
my_list = list()
print(my_list)

# 2. Append the following elements to my_list: 10, 20, 30, 40.
for nos in [10, 20, 30, 40]:
  my_list.append(nos)
print(my_list)

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(my_list)

# 4. Extend my_list with another list: [50, 60, 70].
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)

# 5. Remove the last element from my_list.
del my_list[-1] 
print(my_list)

# 6. Sort my_list in ascending order.
my_list.sort()
print(my_list)

# 7. Find and print the index of the value 30 in my_list.
print(my_list.index(30));