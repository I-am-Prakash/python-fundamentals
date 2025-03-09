# Write your code here
'''
Input
4
23
12
44
32

Output
ODD
EVEN
EVEN
EVEN
'''
n = int(input())

for i in range(n):
	a= int(input())
	if(a%2 == 0):
		print("EVEN")
	else:
		print("ODD")