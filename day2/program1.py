num=int(input("Enter number:"))

#checking number is even or odd
if num%2==0:
	print("Number is even")
else:
	print("number is odd")


 #check for prime
count=0
if num>0:
	for i in range(1,num+1):
		if num%i==0:
			count+=1
	if count==2:
		print("%d is prime"%(num))
	else:
		print("%d is not prime"%(num))

#checking for palindrome
temp=num
rev=0
count=0
while(temp>0):
	dig=temp%10
	rev=rev*10+dig
	temp=temp//10
	count+=1             #counting the number of digits entered
if temp==rev:
	print("%d is palindrome number"%(num))
else:
	print("%d is not palindrome"%(num))

#checking for armstrong number
temp2=num
sum=0
while temp2>0:
	dig2=temp2%10
	sum+=dig2**count
	temp2=temp2//10
if sum==num:
	print("%d is armstrong number"%(num))
else:
	print("%d is not armstrong number"%(num))
