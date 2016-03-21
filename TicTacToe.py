again=1
while again==1:
	arr=["1","2","3","4","5","6","7","8","9"]
	count=0
	while count<9:
		print "\n			  ",arr[0]," | ",arr[1]," | ",arr[2]," \n"
		print "			 -----|-----|------\n"
		print "			  ",arr[3]," | ",arr[4]," | ",arr[5]," \n"
		print "			 -----|-----|------\n"
		print "			  ",arr[6]," | ",arr[7]," | ",arr[8]," \n"
		print "Player-",count%2+1
		val=input("Enter you location: ")
		while arr[val-1] == 'O' or arr[val-1]=='X':
			val = input("Invalid input, Enter Again: ")
		if count%2==0:
			arr[val-1]='O'
		elif count%2==1:
			arr[val-1]='X'
		count=count+1
		if (arr[0]=="O" and arr[1]=="O" and arr[2]=="O") or (arr[3]=="O" and arr[4]=="O" and arr[5]=="O") or (arr[6]=="O" and arr[7]=="O" and arr[8]=="O") or (arr[0]=="O" and arr[3]=="O" and arr[6]=="O") or (arr[1]=="O" and arr[4]=="O" and arr[7]=="O") or (arr[2]=="O" and arr[5]=="O" and arr[8]=="O") or (arr[0]=="O" and arr[4]=="O" and arr[8]=="O") or (arr[2]=="O" and arr[4]=="O" and arr[6]=="O"):
			print "Congratulations, Player 1 is the winner\n"
			break		
		elif (arr[0]=="X" and arr[1]=="X" and arr[2]=="X") or (arr[3]=="X" and arr[4]=="X" and arr[5]=="X") or (arr[6]=="X" and arr[7]=="X" and arr[8]=="X") or (arr[0]=="X" and arr[3]=="X" and arr[6]=="X") or (arr[1]=="X" and arr[4]=="X" and arr[7]=="X") or (arr[2]=="X" and arr[5]=="X" and arr[8]=="X") or (arr[0]=="X" and arr[4]=="X" and arr[8]=="X") or (arr[2]=="X" and arr[4]=="X" and arr[6]=="X"):
			print "Congratulations, Player 2 is the winner\n"
			break	
		if count==9:
			print "This game is a DRAW \n"
			break
	again=input("Do you want to play again(Enter '1' for yes): ")
