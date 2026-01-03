#use function for the basic1 task
def calculate(m):
    sum = 0
    for i in m:
        sum+=i
    return sum
def calavg(s):
    avg=s/3
    return avg
name=input("Enter your name:")
marks=[]
for i in range(3):
    m=int(input("enter marks in subject "+ str(i+1)))
    marks.append(m)
total=calculate(marks)
print("Student's Result")
print(f"Name: {name.title()}")
print(f"Sum : {total}")
print(f"Average : {calavg(calculate(marks))}")

