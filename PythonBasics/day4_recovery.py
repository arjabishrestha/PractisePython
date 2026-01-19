#function to calculate sum, avg and find maximum number from the list of numbers in a function
def tasklist(n,l):
    sum=0
    for i in num:
        sum+=i
    avg=sum/l
    maxi=max(n)
    return sum,avg,maxi
num=[1,4,9,2,7]
l=len(num)
s,avg,maxi=tasklist(num,l)
record={
    "sum":tasklist(num,l)[0],
    "avg":tasklist(num,l)[1],
    "maximum":tasklist(num,l)[2]
}
for key,value in record.items():
    print(key,":",value)
print(record)
print(record.items())

#sorting in descending order using lambda

print("Assending Order")
sorted_list=sorted(num,key=lambda x:x)
for i in sorted_list:
    print(i)
print("Descending Order")
sorted_list=sorted(num,key=lambda x:x,reverse=True)
for i in sorted_list:
    print(i)


