again=1
while again==1:
	cal=input("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\nEnter Your Option(i.e 1,2,3,4): ")
	while cal>4 or cal<1:
		cal=input("Invalid Option, Enter Again(1,2,3,4): ")
	val1=input("Enter 1st value: ")
	val2=input("Enter 2nd value: ")
	if cal==1:
		print val1,"+",val2,"=",val1+val2
	elif cal==2:
		print val1,"-",val2,"=",val1-val2
	elif cal==3:
		print val1,"*",val2,"=",val1*val2
	elif cal==4:
		print val1,"/",val2,"=",val1/val2
	again=input("Do you want to perform operations again(Enter 1 for yes): ")
