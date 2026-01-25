# Dictniory
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.

#Create a dictionary
# std= {"Name":"Sayed Hamza","Roll.no":1,"Age":20}
# print (countries["Name"],countries["Roll.no"],countries["Age"])

# countries= {
#     "Afghanistan": "Kabul",
#     "Pakistan": "Islamabad",
#     "India": "New Delhi",
#     "USA": "Washington",
#     "UK": "London"
# }
# To see a Keys of a dictionary
# print (countries.keys())

# To see a Values of a dictionary
# print (countries.values())

# To see a Items of a dictionary
# print (countries.items())

#itrate through a dictionary (Loop through a dictionary)

# for i,j in countries.items():
#     print (f"The country name is {i} and its capital is {j}")
#     print("\n")


# students= {
#     "name": ["Sayed Hamza", "Syed Hamza" , "Sayyed Hamza"],
#     "roll.no": {"rol1":1,"rol2":2,"rol3":3},
#     "age": 20,}

#Call with key name------------------------------
# print(students["roll.no"]["rol3"])
#find the index number------------------------------
# print (students["name"].index("Sayed Hamza"))
#Call with index number------------------------------
# print(students["name"][0])
#Want to see all keys of a dictionary------------------------
# print(students.keys())


countries= {
    "Afghanistan": "Kabul",
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "USA": "Washington",
    "UK": "London"
}

#to add a new item to a dictionary ( method 1)
# countries["Germany"]="Berlin"
# countries["Italy"]="Rome"
# print(countries)

#to add a new item to a dictionary ( method 2)
# countries.update({"France":"Paris","Spain":"Madrid"})
# print(countries)

# itrate through a dictionary ( to see a values line by line)
for i,j in countries.items():
    print (f"The country name is {i} and its capital is {j}")
    print (f"--->{i} and {j}") 

# Remove  a key value pair from a dictionary and return the value
# print (countries.pop("India")) # Removes "India": "New Delhi"
# print (countries)


# Remove the last inserted key-value pair from a dictionary and return it as a tuple
# print (countries.popitem())  # Removes the last item, e.g., ("Spain", "Madrid")
# print (countries)

#Membership test
# countries= {
#     "Afghanistan": "Kabul",
#     "Pakistan": "Islamabad",
#     "India": "New Delhi",
#     "USA": "Washington",
#     "UK": "London"
# }

# for i in countries:
#     if "India" in countries:
#         print ("Yes, 'India' is in the countries.")
#         break
#     else:
#         print ("No, 'India' is not in the countries.")

# Merging two dictionaries
# d1= {1:"a",2:"b"}
# d2= {3:"c",4:"d"}
# # Merging two dictionaries

# DD= d1.copy()   # Create a copy of d1
# DD.update(d2)   # Merge d2 into the copy of d1
# print (DD)


# d313= {"name": ["Sayed Hamza","Hammad","Ali"],
#        "id": [1,2,3],
#        "address": ["Karachi","Lahore","Islamabad"],
#        "phone": [1234567890,9876543210,5678901234]}


# ids= int(input("Enter your id: "))

# if ids in d313["id"]:
#     i = d313["id"].index(ids)
#     print (f'Name: {d313["name"][i]} \n std id: {d313["id"][i]} \n Location: {d313["address"][i]}')

# else:
#     print ("ID not found.")