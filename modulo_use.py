# Write your code here
# input => 35 10
# o/p => NO

total_candies, cousin_count = map(int, input().split())

if total_candies%cousin_count == 0 :
	print("YES")
else:
	print("NO")