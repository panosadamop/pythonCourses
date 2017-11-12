import operator

while True:
    student = input("Give students am and name separated by comma or type q to abord: \n")
    if student=='q':
        break
    data = dict.update(student.split(",") for item in student)
#converts keys to integers
    for sub in data:
        for key in sub:
            sub[key] = int(sub[key])

    data_ascending = sorted(data.items(), key=operator.itemgetter(0))



