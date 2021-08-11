a = int(input(' addad aval '))
b = int(input('addad dovom '))
for i in range(1, min(a, b)+1):
    if (a % i == 0 and b % i == 0):
        c = i
print(c)