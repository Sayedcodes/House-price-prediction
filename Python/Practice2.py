# import time
# from colorama import Fore, Style, init

# # Practice2

# # Dictinaory={
# #     "table": ["a piece of furniture", "list of facts & figures"],
# #     "cat":"a small animal"
# # }

# # print(type(Dictinaory["table"]))


# # classroom={"Python","Java","Javascript","C++","C",
# #            "Python","Java","Python","Java","C++"}


# # print("Classroom = ",len(classroom))




# # Dic={}

# # E=int(input("Enter English marks :"))
# # Dic.update({"English":E})

# # M=int(input("enter Maths marks :"))
# # Dic.update({"Maths":M})

# # U=int(input("Enter Urdu marks :"))
# # Dic.update({"Urdu":U})

# # print(Dic)



# # specifications= ["Electric","Fast","Flying","Non-electric"]
# # Cars= ["Lamborgini","BMW","Dr.Jhatka","Tesla"]


# # for s in specifications:
# #     for c in Cars:
# #         print(s,c)

# #     print("-------")


# #Print a table

# # for i in range(1,11):
# #     print("5 x",i,"=",5*i)

# # for i in range(1,11):
# #     print(2*i)




# init(autoreset=True)

# colors = [
#     Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW,
#     Fore.YELLOW, Fore.YELLOW, Fore.YELLOW
# ]

# lines = [
#     "She looks just like a dream",
#     "The prettiest girl I've ever seen",
#     "From the cover of a magazine",
#     "In the car, cruising around with you",
#         "And my baby, you know that I got you",
#     "Hit the road, I'm taking off with you",
#     "Not in a hurry, there's something about you, oh"
# ]

# delays = [
#     3.1,5,5,2.5,4,4,1.5
# ]

# for i, (line, delay) in enumerate(zip(lines, delays)):
#     color = colors[i % len(colors)]
#     print(color + line + Style.RESET_ALL)
#     time.sleep(delay) 
