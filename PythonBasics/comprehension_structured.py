#comprehension with structured data
students = {
    "Rita": [70, 80, 90],
    "Sita": [60, 75, 85],
    "Gita": [88, 92, 79]
}
def calcavg(marks):
    sum=0
    for i in marks:
        sum+=i
    avg=sum/len(marks)
    return avg
"""
recordlist=[]
for key,value in students.items():
    record={}
    record["name"]=key
    record["avg"]=calcavg(value)
    recordlist.append(record)
print(recordlist)
"""
#using comprehension
record={}
studentslist=[{"name":key,"avg":calcavg(value)} for key, value in students.items()]
print(studentslist)

#studentslist with avg greater than 80
students_avg=[x for x in studentslist if x["avg"]>=80]
print(students_avg)
students_sorted=sorted(studentslist,key=lambda x:x["avg"], reverse=True)
print(students_sorted)
topper=students_sorted[0]["avg"]
print(f"Topper:{topper}")



