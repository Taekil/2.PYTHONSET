"""
python - Access Set items
not by referring to an index or a key
using for loop
"""
def printSet(set:set):
    i = 0
    for x in set:
        print(f"thisSet for loop {i}: {x}")
        i += 1

# variables
apple = 'A'
banana = 'B'
cherry = 'C'
dates = 'D'
elderBerry = 'E'
fig = 'F'
grape = 'G'
honeyDew = 'H'

thisSet = {apple, banana, cherry}

printSet(thisSet)

print(banana in thisSet) # True
print('C' in thisSet) # True
#print(pine in thisSet) errored
print('D' in thisSet) # False

"""
add and remove set items
"""
# add
thisSet.add(dates)
print("added")
printSet(thisSet)

# create a new set
addOn = {elderBerry, fig, grape}

# update
thisSet.update(addOn)
print("updated")
printSet(thisSet)

# update with any iterable ojbect
myList = [honeyDew]
thisSet.update(myList)
print("updated with List")
printSet(thisSet)

# remove
# if there is no target item in the set, return error
thisSet.remove(apple)
print("remove A")
printSet(thisSet)
# thisSet.remove('P') error

thisSet.discard(banana)
print("discard B")
printSet(thisSet) # not raise error

# pop() can be return random item, 
# and random item removed from the set. 
print(thisSet.pop())
printSet(thisSet)

# thisSet.clear() -> empty set. 

# del thisSet -> remove the set(remove the memory)


