t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    sum1=a+b+c
    if sum1%9==0 and sum1//9<=min(a,b,c):print('YES')
    else:print('NO')
