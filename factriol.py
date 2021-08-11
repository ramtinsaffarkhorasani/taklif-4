a = int(input("addad 1 "))
b =0
def c(b):
    if b==0 or b==1:
        return 1
    else:
        return b * c(b-1)
while True:
    b+=1
    if c(b)== a:
        print("is True: ","factorial ",b,"is ",c(b))
        break
    if (b)>a:
        print('ghalat')
        break
