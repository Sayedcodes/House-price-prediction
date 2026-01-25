# Code

Q1= "Koi couple wali reel nhi bheji thi? (Y/N): "
Q2= "Aur jo mene couple wali dekhi thi wo bheji thi? (Y/N): "

for i in range(1):
    Muskan_answer= input(Q1).upper()
    if Muskan_answer == "N":
        Muskan_answer= input(Q2).upper()
        if Muskan_answer == "N":
            print("Mera pyara Bachchaww 😭")
        else:
            print("Tut gaya mera dil")
    else:
         print("Tut gaya mera dil")





