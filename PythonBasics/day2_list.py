#marks in 5 subjects, store in list, find sum,avg,max,min
marks=[]
for i in range(5):
    m=int(input("enter marks in subject "))
    marks.append(m)
sum=0
for i in marks:
    sum+=i
print(f"Sum= {sum}")
print(f"Average= {sum/5}")
print(f"Highest marks is {max(marks)}")
print(f"Lowest marks is {min(marks)}")
