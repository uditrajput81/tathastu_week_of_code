i=int(input("Enter number upto which you want fibonacci series:"))
a,b=0,1
for i in range(i+1):
	print(a,end=",")
	a,b=b,a+b
