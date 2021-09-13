a=list(map(int,input().split()))
n=len(a)
m=0
for i in range(n):
    for j in range(n):
        if i!=j:
            for q in range(n):
                if q!=j and i!=q:
                    x=a[i]
                    y=a[j]
                    z=a[q]
                    if (x<y+z)and(y<x+z)and(z<x+y):
                        p=(x+y+z)/2
                        s=(p*(p-x)*(p-y)*(p-z))**0.5
                        if s>m:
                            print(x,y,z)
                            m=s
print(m)
                            