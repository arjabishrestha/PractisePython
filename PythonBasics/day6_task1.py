#filter from the list
marks = [45, 78, 90, 67, 82]
newlist=[]
squarelist=[]
for mark in marks:
    if mark>=70:
        newlist.append(mark)
    squarelist.append(mark**2)
maxmarks=max(marks)
print(newlist)
print(squarelist)
print(f"Maximum marks is {maxmarks}")