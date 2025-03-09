# Sum Upto Ten


from functools import reduce

# Write your code here
print(reduce(lambda a,b : a+b, list(range(1,11))))