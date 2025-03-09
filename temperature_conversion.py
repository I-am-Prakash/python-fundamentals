# Write your code here

'''
Input
2
34.52
12

ouput
2
34.52
12
'''
n = int(input())

for _ in range(n):
	celcius = float(input())
	fahrenheit = (9*celcius)/5 +32
	print(f"{fahrenheit : .2f}")