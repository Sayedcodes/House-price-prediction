# while

# user = int(input("Enter the number: "))

# while user >= 1:
#     print(user)
#     if user == 100000:
#         print("Done with the Loop")
#         break
#     user+=1

correct_password= 10
attempt= 0
max_attempts= 3

while attempt < max_attempts:
    password = int(input("Enter the password: "))

    if password == correct_password:
        print("Login Sucessfully,Welcome")

        break

    else:
        print("The pin is incorrect.Try again")

        attempt+=1

if attempt == max_attempts:
        print("The portal has locked,Try again after the few minutes")




# number = int(input("Enter the number: "))

# while number<=5:
#     print(number)
#     break
# else:

#     print("Loop done")


# count= 1

# while (count>10):
#     print(count)

#     count-=1

# else:
#     print("im under the else")


#Do while loop (exit controlled loop / Infinite loop)


# while True:
#     num= int(input("Enter the positive number: "))
#     print(num)

#     if not num>5:
#         break
