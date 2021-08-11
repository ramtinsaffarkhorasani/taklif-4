import math
print('a*(x^2) + b*x + c = 0')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
s = math.sqrt((b ** 2) - (4 * a * c))
if s > 0:
    print('javb ', ((-1 * b) + s) / (2 * a))
    print('javab', ((-1 * b) - s) / (2 * a))
elif s == 0:
    print('Asnwer is', (-1 * b) / (2 * a))
else:
    print("error")