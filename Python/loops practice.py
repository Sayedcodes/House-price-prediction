#loops

#python was not include a last number like (1,3) The 3 has exclude by the python

# ---> So if i want 1 to 3 range
# so we will write the code (0,4) than the python will print
# the code 1 to 3 range because we start the code from 0 not a 1

# for x in range (0,501):
#     print("Rahmat mera beta")


# names=["Hamza","Ali","Ahmed","Hassan","Haris"]
# for name in names:
#     print(name)


# While loop

# i= 100

# while i >= 1:
#     print(i)
#     i -= 1

# n=int(input("enter the number: "))
# i=1
# while i <= 10:
#     print(n*i)
#     i+=1

# nums=1,4,9,16,25,36,49,64,81,100
# indx=0
# while indx < len(nums):
#     print(nums[indx])
#     indx += 1

# numbers=(1,4,9,16,25,36,49,64,81,100)

# num=16

# x= 0

# while x < len(num):
#     if (len(num[x])== num):
#         print()


# for i in range (1,6):
#     print(i)


# for i in range (1,4):
#     print(i)


# for i in range (1,5):
#     print("Hello")


# animals = ["cat", "dog", "cow"]

# for a in (animals) :
#     print(a)


# for i in ("hi"):
#     print(i)


# for i in range (10,13):
#     print (i)


# n= 0

# for row in range (1,6):
#     for col in range (row):
#         n=n+1
#         print(n, end= " ")

#     print()




check=1

while(check):

    age=int(input("enter the age: "))

    if age>=18:
        id=input("voter id available press y otherwise n: ")

        if id=="y" or id=="Y":

            print("voter is eligiable for vote")

        else: 
            ("voter is not eligiable for vote")

    else:
        ("voter is not eligiable for vote")

check=int(input("if you want to exit the loop press 0 otherwise 1: "))



for i in range(1, 11):
    for j in range(1, 11):
        if j <= i:
            print("█", end=" ")
        else:
            print(" ", end=" ")
    print(f"{(11 - i) * 10}%")


f_name= "Sayed"
l_name= "Hamza"

count = 0
while True:
    print(f_name + l_name)
    count += 1
    if count % 10 == 0:
        print(f"{count // 10} ------------------------------------------")
    if count == 5000000:
        break