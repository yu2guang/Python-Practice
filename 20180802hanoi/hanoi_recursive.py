def hanoi(n,origin,temp,final):
	if(n>0):
		hanoi(n-1,origin,final,temp)
		print(n,":",origin,"->",final)
		hanoi(n-1,temp,origin,final)

while(1):
	num = int(input("please input the number(press 0 to leave): "))
	if(num==0):
		break
	hanoi(num,'A','B','C')
