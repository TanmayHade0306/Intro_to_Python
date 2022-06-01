#Create an empty set
b = set()
print(type(b))

## adding values to empty set
b.add(4)
b.add(5)
b.add(4)
b.add(5) # Adding a value repeatedly does not change a set
b.add((2,4,5,1))

## Accessing Elements
# b.add({5,7,8,1}) # Cannot add list ([]) or dictionary ({}) to sets
print(b)

## length of the set
print(len(b)) # prints the length of the set

## Removal of an Item
b.remove(5) # Remove 5 from set
#b.remove(15) #Throws an error while trying to remove 15(which is not present in the4 set)
print(b)

print(b.pop())
print(b)

