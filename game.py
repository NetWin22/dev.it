import os
import subprocess
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to Dev.it! Choose what you want to play!")
print("---")
print("1.  Play Normal Mode")
print("2.  Play Tutorial")
print("3.  Check out more from Kytheraen Network")
print("4.  Exit")
print("")
choice1 = int(input())
print("")
if choice1 == 1:
	subprocess.run([sys.executable, "normal_mode.py"])
elif choice1 == 2:
	subprocess.run([sys.executable, "tutorial.py"])
elif choice1 == 3:
	print("Go to https://kytheraen.website and find more!")
elif choice1 == 4:
	sys.exit()
