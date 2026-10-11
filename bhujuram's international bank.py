 # BANK @ BHUJURAM SOREN
import random
a=0
b=1
c=3
print('       WELCOME TO THE','\n','     BANK OF BHUJURAM')
print('\n','\n')
name=(input('ENTER YOUR NAME :'))
print('\n','WELCOME',name,'TO OUR BANK')
print('\n')
account_no=int(input('ENTER YOUR 11 DIGIT ACCOUNT NUMBER :'))
if 10000000000<=account_no<=999999999999:
	while b==1:
		pincode=int(input('ENTER YOUR 4 DIGIT PINCODE :'))
		if 1000<=pincode<=9999:
			b=0
		else:
			while c>1:
				c=c-1
				print('INVALID PINCODE','\n')
				print('NUMBER OF ATTEMPT LEFT :',c)
				pincode=int(input('ENTER YOUR 4 DIGIT PINCODE :'))
				if 1000<=pincode<=9999:
					b=0
				else:
					b=2
				
else:
	a=1
	print('INVALID ACCOUNT NUMBER','\n')
	
	
balance=random.randint(10000,99999)
while a==0 and b==0:
	print("""
	CHOOSE WHAT YOU WANT 
	1/    Balance
	2/    Withdraw
	3/     Deposit
	4/     Quit
	   """)
	
	Option=(input("ENTER YOUR CHOICE :"))
	if Option=='1':
		print('YOUR BALANCE IS  ₹',balance)
	elif Option=='2':
	   	print('YOUR BALANCE IS  ₹',balance)
	   	Withdraw=float(input("ENTER WITHDRAW AMOUNT :"))
	   	if Withdraw>0 and Withdraw<=balance:
	   		balance=(balance-Withdraw)
	   		print('YOUR PRESENT BALANCE IS  ₹',balance)
	   	elif Withdraw>balance:
	   		print("INSUFFICIENT BALANCE IN YOUR ACCOUNT")
	   	else:
	   		print("NON WITHDRAW MADE")
	elif Option=='3':
	   	print('Balance  ₹',balance)
	   	Deposit=float(input("ENTER DEPOSIT AMOUNT  ₹"))
	   	if Deposit>0:
	   		balance=(balance+Deposit)
	   		print('YOUR PRESENT BALANCE IS  ₹',balance)
	   	else:
	   		print("NONE DEPOSIT MADE")
	elif Option=='4':
		break
	else:
		print('PLEASE CHOICE VALID OPTION')
print('\n','      THANK YOU FOR COMING...')