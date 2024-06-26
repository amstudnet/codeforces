while 1:
    try:
        n=int(input())
        st=list(map(int,input().split()))
        st.insert(0,0)
        f=0
        for i in range(1,len(st)):
            if i==st[st[st[i]]]:
                print("yes")
                f=1
                break
        if f==0:
            print("no")
        
    except:
        break
