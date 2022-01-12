def p(n,m,o):
    res=0
    for i in o:
        if res==m:
            n=n-1
            break
        if i=="H":
            res=res+1
    k=int((res/n)*100)
    return k
o=["T","T","H","T","H"]
print(p(5,4,o))