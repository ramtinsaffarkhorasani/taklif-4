def a(c,n):
    for i in range(1,m):
        for j in range(1,n):
            if (i+j)%2==0:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print("")
a(c, n)(int(input("addad aval ")),int(input('addad dovom ')))