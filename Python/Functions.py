# TODO: Functions.py

# python function to greet a user by their name with input prompt
# def greet():
#     name=input("Enter your name: ")
#     print(f"Hello, {name}!")
# greet()

#

# def greet(name,age):
#     print("Hello",name,age)
# greet("Alice",30)


# Questions
# Q1

# def login_system(username,password):
#      if username==username and password=="2004":
#          return "Login Successful"
#      else: return "Login Failed"

# print(login_system("Sayed Hamza","2004"))

# Q2

# Args Function
# def args_function(*n):
#     print(sum(n))
# args_function(1,2,3,4,5)

# Kwargs Function

def func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
func(name="Alice", age=30, city="New York")
