adict = {1:'A', 20:'B', 50:'C'}

print(sum([max(adict), min(adict)]))

print(sorted([max(adict), len(adict), sum(adict), min(adict)]))

print(len([max(adict), len(adict), min(adict)]))


bdict = [max(adict) if i%2 else min(adict) for i in range(4)]
print(bdict)