import sys
sys.set_int_max_str_digits(5000)
d={1:1,}
i,j=2,3
first,second=1,1
while i<=5000:
    first,second=second,first+second
    if len(str(second))==i and i not in d:
        d[i]=j
        i+=1
    j+=1
     
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(d[n])
