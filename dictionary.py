# dictionary = a collection of {key:values} pairs ordered and changeable. No duplicates
capitals = {"USA" : "Washington D.C",
             "India": " New Dehli",
             "China" : "Beijing",
             "Russia" : "Moscow"}

# print(dir(capitals))
# gives you 
# print(help(capitals))
print(capitals.get("USA"))
# you input the key "USA" and ger rhe value
# When the key doesnt exist in our dictionary then youll get "none" you can use this to get a boolean value
if capitals.get("Japan)"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany" : "Berlin"})

# You can use this to add things to your list^^^
capitals.update({"Illinois" : "Springfield"})


# This shows us the updated version of our dictionary^^^

capitals.update({"USA" : "Detroit"})
# changes a value of said key
capitals.pop("China")
# removes that item
capitals.popitem()
# Removes the most recent item 

# capitals.clear
# this clears the dictionary
print(capitals)
keys = capitals.keys()
print(keys)
# this returns all the keys and not the values

values = capitals.values()
print(values)
# this returns all of the values and not the keys

for key in capitals.keys():
    print(key)
    
for values in capitals.values():
    print(values)
# a diff way to do this ^^^
    
items = capitals.items
print(items)
for key, value in capitals.items():
    print(f'{key}: {values}')