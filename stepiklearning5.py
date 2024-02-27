##n=int(input())
##s=0
##kol=0
##maximum=0
##minimum=9
##kol_ch=0
##m=1
##while n>0:
##    x=n%10
##    s=s+x
##    kol=kol+1
##    if maximum<x:
##        maximum=x
##    if minimum>x:
##        minimum=x
##    if x%2==0:
##        kol_ch+=1
##    m=m*x
##    n=n//10
##print(s)
##print(kol)
##print(maximum)
##print(minimum)
##print(kol_ch)
##print(m)
n = int(input())
count = 0
level = 0
while n > level:
    count+=1
    level = level + count
    n = n - level
print(count)
   
