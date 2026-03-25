#functions,list,dictionary
students = {
    "Rita": [70, 80, 90],
    "Sita": [60, 75, 85],
    "Gita": [88, 92, 79]
}
def calavg(marks):
    sum=0
    for mark in marks:
        sum+=mark
    return sum/3
#avg={
    #"Rita":calavg(students["Rita"]),
    #"Sita":calavg(students["Sita"]),
    #"Gita":calavg(students["Gita"])
#}
avg = {}
for name, marks in students.items():
    avg[name] = calavg(marks)

for key,value in avg.items():
    if(value >= 80):
        print(key)