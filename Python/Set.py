# Set

# collection={1,2,3,3,5,4,"Sayed","Hamza","S","H",15}

# print(collection)
# print(type(collection))


#add a collection in emty set#

# collection={}

# print(type(collection))

#they print a dict(dictinory) bcz of the only empty {} is used for dict
# if we want add a collection in empty set so we will write the syntax like this

# collection= set()
# print(collection)


# # if we want to add a value in empty set 
# collection=set()

# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(3)
# collection.add(3)

# print(collection)

#to remove a value from set
# collection.remove(3)
# print(collection)

#to clear a set
# collection.clear()
# print (len(collection))

# to remove a random value from set
# a={"a","b","c","d"}
# a.pop()
# print(a)

# give the unique value from the two sets
# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))

# to find the common value from two sets
# set1={1,2,3}
# set2={2,3,4}
# print(set1.intersection(set2))


# to find the different value from two sets
# set1={1,2,3}
# set2={2,3,4}
# print(set1.difference(set2))


# to find the subset from two sets (if all the value of set1 is in set2 then it will be true otherwise false)
# set1={1,2,3}
# set2={2,3,4,1}

# print (set2.issubset(set1))


# The isdisjoint() method in Python is used to check whether two sets are disjoint, meaning they have no elements in common.
#  If the sets are disjoint, it returns True; otherwise, it returns False.

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}

# print(set1.isdisjoint(set2))  # Output: True



# # The issuperset() method in Python is used to check whether a set is a superset of another set.
# A = {1, 2, 3, 4, 5}
# B = {1, 2, 3}
# Check if A is a superset of B
# print(A.issuperset(B)) # Output: True
# Check if B is a superset of A
# print(B.issuperset(A)) # Output: False


#Questions................
s1 = {"laptop", "mobile", "tablet", "pc"}
s2 = {"mouse", "keyboard", "pc"}

#Q1. Products not available in both sets (symmetric difference)

# not_in_both = s1.symmetric_difference(s2)
# print("Products not available in both sets:", not_in_both)

# Q2. Which product is available in both warehouse (intersection)

# print (s1.intersection(s2))


# Q3. Which product is not available in warehouse 1.

# print (s2.difference(s1))


# Q4. Which product is available in warehouse 2.

# print (s2)