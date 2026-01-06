#function with dictionary
def askuser():
    name=input("enter your name")
    marks=[]
    for i in range (5):
        m=int(input("enter marks in subject"+str(i+1)))
        marks.append(m)
    return name,marks
def calcsum(marks):
    sum=0
    for i in marks:
        sum+=i
    return sum
def calcavg(s):
    return s/5
inputfromuser=askuser()
record={
    'Name':inputfromuser[0],
    'Marks':inputfromuser[1],
    'Sum':calcsum(inputfromuser[1]),
    'Average':calcavg(calcsum(inputfromuser[1]))
}
print(record)
for key,value in record.items():
    print(key,":",value)
