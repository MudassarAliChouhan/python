import user
import sys
import functions

while(True):
	functions.menu()
	choice = input("Enter Your Choice: ")
	
	if(choice == "1"):
		user.User.add()
		print("Done")
		input()
	elif(choice == "2"):
		user.User.update()
		input()
	if(choice == "3"):
		user.User.printAll()
		input()
	elif(choice == "4"):
		user.User.remove()
	elif(choice == "0"):
		sys.exit(0)

user.User.print()
