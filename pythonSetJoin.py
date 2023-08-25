# using union()
# return new set containing all itmems from both sets. 
# or update() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# or set1.update(set2)
# update and union -> exclude any duplicate items
print(f"set3:{set3}")

# what is instersection_update()
# keep only the items that exist in both x and y
x = {"a", "b", "c"}
y = {"g", "m", "a"}
# not return new set, keep the intesected value in x
x.intersection_update(y)
print(f"x: {x}")

# the intersection() return new set
z = x.intersection(y)
print(f"z: {z}")

# symetric_diffrence_update() 
# keep only the elements that are not present
# in both set. 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("x:", x)
# return new set not present in both sets
z = x.symmetric_difference(y)
print("z:", z)

# what the diffrence between difference() 
# and symmetric_difference()
"""
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
diff_set = set1.difference(set2)
print(diff_set)
{1, 2}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)
{1, 2, 6, 7}
"""
