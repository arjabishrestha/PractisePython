#list program extended to show dictionary
name=input("enter your name")
marks=[]
for i in range(5):
    m=int(input("enter marks in subject "))
    marks.append(m)
sum=0
for i in marks:
    sum+=i
avg=sum/5
report={
    "Name":name,
    "Marks":marks,
    "Sum":sum,
    "Average":avg
}
print(report)
print(f"Name: {report["Name"]}")
print(f"Marks in 5 subjects: {report["Marks"]}")
print(f"Marks in 1st subject {report["Marks"][0]}")
print(f"Sum: {report["Sum"]}")
print(f"Average: {report["Average"]}")
print(report.items())
#dict traversal
for i in report:
    print(f"{i}:{report[i]}")
for key,value in report.items():
    print(key,":",value)