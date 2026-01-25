# #Q1. (1,2,3)

# max(1, 2, 3)
# print (max(1, 2, 3))

#Q2. ("Hello", "World")

v = ("a", "e", "i", "o", "u")

count = 0
for i in "Hello World":
    if i.lower() in v:
        print(i)
        count += 1
print(count)