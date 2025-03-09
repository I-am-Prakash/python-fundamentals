# Write your code here
weights = list(map(float, input().split()))

average_weight = sum(weights)/len(weights)

print(f"{average_weight : .6f}")