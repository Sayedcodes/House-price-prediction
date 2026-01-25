#check untill the user come for vote eligiable

check=1
while(check):
    age=int(input("Enter your age: "))
    if age >= 18:
        id=input("voter id available? (yes/no): ")
        if id=="yes" or id=="Yes":
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote,you need a voter id.")
    else:
        print("You are not eligible to vote, due to age.")     

    check=int(input("Do you want end the loop press 0: oterwise 1")  )