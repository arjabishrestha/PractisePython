#program that takes name, marks in 3 subjects, print result
name=input("Enter your name: ")
marks=[]
for i in range(3):
    m=int(input("Enter marks in subject "+str(i+1)+" "))
    marks.append(m)
sum=0
for i in marks:
    sum+=i
avg=sum/3
print(f"Sum of marks is {sum}")
print(f"Average of marks is {avg}")

