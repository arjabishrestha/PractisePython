#function that takes input, function to calculate sum, function to calculate avg
def askuser():
    marks=[]
    for i in range (5):
        m=int(input("enter marks in subject"+str(i+1)))
        marks.append(m)
    return marks
def calcsum(marks):
    sum=0
    for i in marks:
        sum+=i
    return sum
def calcavg(s):
    return s/5
markslist=[]
markslist=askuser()
total=calcsum(markslist)
average=calcavg(total)
print(f"Marks in 5 subjects {markslist}")
print(f"Sum of marks is {total}")
print(f"Average is {average}")

