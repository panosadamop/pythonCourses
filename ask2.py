def part(L,start=0,end=None,step=1):
    return sum(L[start:end:step])

n=6
alist = [i for i in range(1, n+1)]
print(alist)
print(part(alist, step=1,start=1,end=5))