# Q. write a function To calculate frequency of char in string


def frequency(s):
    data = {}
    for char in s:
        if char not in data.keys():
            data[char] = 1
        else:
            data[char] += 1
    return data
x = frequency("programme")
for i, j in x.items():
    print(i, ":", j)


