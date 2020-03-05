import random
import os

class User:
	filename = "User.db"
	def add():
		file = open(User.filename,"a")
		name = User.getUniqName()
		id = str(User.getUniqno())
		date = User.dateParse()
		file.write(id)
		file.write(",")
		file.write(name)
		file.write(",")
		file.write(date)
		file.write("\n")
		file.close()
	def getUniqno():
		rand = 1
		while True:
			if(User.chkData(0,rand)):
				return rand
			rand = random.randrange(1,10)
		return False
	def getUniqName():
		name = input("Enter You name: ")
		while True:
			if(User.chkData(1,name)):
				return name
			print("name has existance please try another")
			name = input("Enter You name: ")
		return name
	def chkData(index,exist):
		index = int(index)
		exist = str(exist)
		file = open(User.filename,"r")
		while True:
			line = file.readline()
			if(line==""):
				break
			data = line.split(",")
			if(data[index]==exist):
				return False
		return True
	def printAll():
		file = open(User.filename,"r")
		while True:
			line = file.readline()
			if(line==""):
				break
			data = line.split(",")
			print("Name: ",data[1])
			print("Id: ",data[0])
			print("DOB: ",data[2])
		return True
	def dateParse():
		print("Date of Birthdd/mm/yyyy: ")
		date = input()
		while True:		
			if(date[2]=="/" and date[5]=="/" and len(date)==10):
				return date
			else:
				print("re-type invalid or length")
				date = input()
	def update():
		tempfile = User.filename+".tmp"
		file = open(User.filename,"r")
		name = input("Enter User name: ")
		if(not User.chkData(1,name)):
			tFile = open(tempfile,"w")
			while True:
				line = file.readline()
				if(line==""):
					break
				data = line.split(",")
				if(data[1]==name):
					getName = User.getUniqName()
					getDate = User.dateParse()
					tFile.write(data[0])
					tFile.write(",")
					tFile.write(getName)
					tFile.write(",")
					tFile.write(getDate)
					tFile.write("\n")
				else:
					tFile.write(line)
			file.close()
			os.remove(User.filename)
			tFile.close()
			os.rename(tempfile,User.filename)				
		file.close()
	def remove():
		tempfile = User.filename+".tmp"
		file = open(User.filename,"r")
		name = input("Enter User name: ")
		if(not User.chkData(1,name)):
			tFile = open(tempfile,"w")
			while True:
				line = file.readline()
				if(line==""):
					break
				data = line.split(",")
				if(data[1]!=name):
					tFile.write(line)
			file.close()
			os.remove(User.filename)
			tFile.close()
			os.rename(tempfile,User.filename)				
		file.close()



