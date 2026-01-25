# Tuples

# tup=(2,"Hamza",True)

# print (type(tup))


# name=["Ali","Hamza","Ahsan"]

# tup1= tuple(name)

# print (tup1)
# print (type(tup1))


# t1= ("a","b","c","d"
#      )
# t2= input("Enter :")

# print (t1*3)


# if "a" in t1:
#     print ("Yes")
# else:
#     print ("No")

# if "c" in t1:
#     if t2 == t2:
#         print ("working")

#     else:
#         print( " not working")

# if "c" == t2:
#     print ( "Matched")

# else:
#     print ("also working")


# t1= ("a","b","c","d")

# for a in t1:
#     print (a)

# t1= (1,2,3,4)


# print ("the min is :",min(t1))
# print ("the max is :",max(t1))
# print ("the sum is :",sum(t1))
# print ("the length is :",len(t1))

# for i in t1:
#     if (i == "b"):
#         print (i*2)
#         continue
#     print (i)



# t1= ("class",10 ,"|" ,"Tuple ","set","and", "Frozen" , "set", "in", "python")

# print(t1.index("Python".lower()))


# t5= (1,2,3,4,5,6,7,8,9,10)

# t5= list(t5)
# t5[2]=5

# print (t5.index(5))


# t6= (1,2,3,4,5,6,7,8,19,10)

# # print (t6.index(19))

# #if we want to change any value in tuple we have to convert it into list first.... 
# # rather it can not be changed and it will give error.

# t6= list(t6)
# t6[8]=9
# t6= tuple(t6)
# print (t6)
# print (type(t6))

# PACKING
t1= 10,"Hamza",True

# print (t1)
# print (type(t1))


# UNPACKING

a,b,c = t1

print (b,c,a)

print (type(a))
print (type(b))
print (type(c))




