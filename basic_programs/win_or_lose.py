# Write your code here
n = int(input())

nums = list(map(int, input().split()))

max_value = max(nums)

if(max_value%2 == 0):
	print("WON")
else:
	print("LOST")