#dictionary inside list
students = [
    {"name": "Arjabi", "marks": [78, 80, 85]},
    {"name": "Anita", "marks": [88, 90, 92]},
    {"name": "Sarita", "marks": [70, 75, 72]}
]
def calavg(marks):
    sum=0
    for k in marks:
        sum+=k
    return sum/3
for i in students:
    studmarks=(i.get("marks"))
    i["average"]=calavg(studmarks)
print(students)
sorted_students=sorted(students,key=lambda x:x["average"],reverse=True)
print(sorted_students)

