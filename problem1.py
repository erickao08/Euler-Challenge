t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    n3 = int((n-1)//3)
    n5 = int((n-1)//5)
    n15 = int ((n-1)//15)
    if n <15:
        result = ((n3 + 1)*n3//2)*3 + ((n5 + 1)*n5 //2)*5
    else :
        result = ((n3 + 1)*n3//2)*3 + ((n5+1)*n5//2)*5 - ((n15+1)*n15//2)*15


    print(int(result))
