# # # """x=10
# # # y=5
# # # result = x-y
# # # print(result)

# # # print(5+5)

# # # a=8
# # # b=1
# # # print(a-b)

# # # TOtal= sum [1, 2, 3, 4, 5]
# # # print(TOtal)

# # # google= "www.google.com"
# # # print(google)"""

# # # num1=1
# # # num2=2

# # # print("sum of 2 numbers   is"
# # # , num1+num2)


# # amount= 2800

# # note_500= amount//500
# # amount %= 500

# # print("The amount is now:", note_500)

# # note_200 = amount//200


# # print("The amount is now:", note_200)




# open('desktop.ini', 'w').write('''[.ShellClassInfo]
# IconResource=imageres.dll,-102
# ''')
# import os
# import shutil
# # Define the source and destination paths
# source = 'desktop.ini'
# destination = os.path.join(os.path.expanduser('~'), 'Desktop', 'desktop.ini')
# # Move the file
# shutil.move(source, destination)
# print("desktop.ini has been moved to the Desktop.")
# # Check if the file exists on the Desktop
# if os.path.exists(destination):
#     print("desktop.ini file exists on the Desktop.")

# else:
#     print("desktop.ini file does not exist on the Desktop.")
# # Check if the file is hidden
# if os.path.isfile(destination) and not os.access(destination, os.R_OK):
#     print("desktop.ini file is hidden.")
# else:
#     print("desktop.ini file is not hidden.")
# # Check if the file is read-only
# if os.path.isfile(destination) and not os.access(destination, os.W_OK):
#     print("desktop.ini file is read-only.")
# else:
#     print("desktop.ini file is not read-only.")

# # Check if the file is executable

# if os.path.isfile(destination) and os.access(destination, os.X_OK):
#     print("desktop.ini file is executable.")
# else:
#     print("desktop.ini file is not executable.")
# # Check if the file is a directory

# if os.path.isdir(destination):
#     print("desktop.ini file is a directory.")
# else:
#     print("desktop.ini file is not a directory.")
# # Check if the file is a regular file
# if os.path.isfile(destination):
#     print("desktop.ini file is a regular file.")
# else:
#     print("desktop.ini file is not a regular file.")
#         # Check if the file is a symbolic link
#         # if os.path.islink(destination):
#         #   print("desktop.ini file is a symbolic link.")
#         # else:
#         #   print("desktop.ini file is not a symbolic link.")
#         # # Check if the file is a block device
#         #   
#         # if os.path.isfile(destination) and os.stat(destination).st_mode & 0o60000:
#         #   
#         # print("desktop.ini file is a block device.")
#         # else:
#         #   
#         #   
#         # print("desktop.ini file is not a block device.")
#         # # Check if the file is a character device
#         # if os.path.isfile(destination) and os.stat(destination).st_mode & 0o20000:
#         #   
    
        





x= input("Enter a your name: ")


