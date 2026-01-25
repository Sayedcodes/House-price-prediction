#login

for i in range(1,4):
    print (i)
    user_id = "Sayed Hamza".lower()
    password = 1234

    u = input("Enter your username: ")
    p = int(input("Enter your password: "))

    if user_id == u and password == p:
        print("Login successful")
    else:
        print("Login failed, please try again")
    print("end loop")
