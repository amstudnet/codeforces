for _ in range(int(input())):    
    case=int(input())
    minx=-1
    maxx=9999999999
    res=[]
    for i in range(case):
        a,x=map(int,input().split())
        if a==1:
            minx=max(minx,x)
        elif a==2:
            maxx=min(maxx,x)
        elif a==3:
            res.append(x)
    if minx>maxx:print(0)
    else:
        #res.sort()
        newres=[]
        for i in range(len(res)):
            if minx<=res[i]<=maxx:
                newres.append(res[i])
        print(maxx-minx-len(newres)+1)
