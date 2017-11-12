import copy

di1={1:[1,2,3], 2:{1:'A', 2:'B'}}

di2 = copy.copy(di1)
di2[2][1] = 'X'

di3 = copy.deepcopy(di1)
di3[1][0] = 'Y'

print(di1)
print(di3)

print("---------------------------------------------")
print("---------------------------------------------")
adict = {1:'A', 20:'B', 50:'C'}

print(sum([max(adict), min(adict)]))

print(sorted([max(adict), len(adict), sum(adict), min(adict)]))

print(len([max(adict), len(adict), min(adict)]))


bdict = [max(adict) if i%2 else min(adict) for i in range(4)]
print(bdict)

print("---------------------------------------------")

di1 = {1:10, 2:20, 3:30}
di2={}

for it in di1.items():
    di2[it[0]] = it[1] + 100
print(di2)
print(di2.get('1','Δεν υπάρχει το κλειδί'))