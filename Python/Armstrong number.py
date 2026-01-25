# n=153

# d=n//10
# r=n%10
# total= r**3

# r=d%10
# total= total + r**3

# d=d//10
# print(d)
# r=d%10
# total= total + r**3

# if n== total:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
# # Armstrong number check


num = 153
original_num = num
s = 0
l = len(str(num))

for i in range(l):
    reminder = num % 10
    s = s + reminder ** l
    num = num // 10

if l != 3:
    print("Invalid number")

if s == int('153'):
    print("Armstrong Number")

else:
    print("Not Armstrong")