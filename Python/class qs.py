# class qs

x= "madam"
y= x=x[::-1]
# if x == x[::-1]:
print(y)

# TO  reverse a string we use [::-1] slicing method

# number= 1,5,8,10,3

# maximum= number[0]
# for num in number:
#     if num > maximum:
#         maximum = num
# print("Maximum number is", maximum)
# TO find maximum number in a list we use for loop and if condition



# x= "This is python class"
# i= x("a","e","i","o","u")
# for i in x:
#     if i == ("a","e","i","o","u"):
#         print(x.count("))



class Below20ageExceptionerror(Exception):
    pass

age = int(input("Enter your age: "))
try:
    if age < 20:
        raise Below20ageExceptionerror("You are not eligible")
    else:
        print("You are eligible")
except Below20ageExceptionerror as e:
    print("error:", e)

print("run all code")