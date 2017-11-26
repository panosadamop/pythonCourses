def myrange(N,logos):
    counter = 0
    n = 1
    while counter <= N:
        counter += 1
        n *= logos
        yield n


for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)