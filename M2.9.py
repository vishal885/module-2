#Write a Python program to sum of three given integers. However  if two values are equal sum will be zero

def sum(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum
print(sum(2, 2, 2))
print("*"*30)
print(sum(44,55,44))
print("*"*30)
print(sum(6,9,7))



