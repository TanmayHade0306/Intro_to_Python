myDict = {
    "Fast": "In a Quick Manner",
    "Tanmay" : "The Richest Person",
    "Marks" : [1,2,3,4],
    "anotherdict" : {'Tanmay': 'Player'},
    1 : 2
}

#Dictionary Methods
# print(list(myDict.keys())) #prints the keys of the dictionary 
# print(myDict.values()) #Prints the values of the dictionary
# print(myDict.items()) #Prints the (key,value) for all contents of the dictionary
# print(myDict)
updateDict = {
    "Jay" : "Brother",
    "Tanmay" : "Millioner"
}
myDict.update(updateDict)#updates the dictionary by adding key value pair from updateDict
print(myDict)


print(myDict.get("Tanmay")) # prints value associated with key "Tanmay"
print(myDict["Tanmay"]) # prints value associated with key "Tanmay"

#The Difference between .get and [] syntax in Dictionaries:
print(myDict.get("Tanmay2")) # Returns none as Tanmay2 is not presents in the dictionary
print(myDict["Tanmay2"])# throws an error  as Tanmay2 is not presents in the dictionary

