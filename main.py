def f1(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(f1(4))
def f2(n):
    sum=0
    for i in range(1,n+1):
        for j in range(i,i+1):
            sum+=i
    return sum
print(f2(3))