# Write your code here
# input -> 1500 1.4 3
# o/p -> 68.000000
num = input().split()

num1,num2,num3 = map(float, num)

print(f"{num1*num2*num3/100 : .6f}")