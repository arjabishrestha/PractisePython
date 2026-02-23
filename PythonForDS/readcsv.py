#read csv file 
import csv
file=open("students.csv","r")
reader=csv.reader(file)
header=next(reader)
cleandata=[]
for row in reader:
    if row[1]=='':
        continue
    try:
        type(int(row[2]))
    except ValueError:
        continue
    row[1]=int(row[1]) #convert age to int
    row[2] = int(row[2])
    print(row,type(row[1]),type(row[2]))
    cleandata.append(row)
print(cleandata)
def assign_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"
new_data = []
for row in cleandata:
    name, age, marks = row

    grade = assign_grade(int(marks))   # feature creation

    new_row = [name, age, marks, grade]
    new_data.append(new_row)
print(new_data)
file.close()
file= open("clean_students.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name", "Age", "Marks", "Grade"])
writer.writerows(new_data)
file.close()
