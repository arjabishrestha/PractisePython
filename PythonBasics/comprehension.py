#task 1 using list comprehension
marks = [45, 78, 90, 67, 82]
new_marks=[x for x in marks if x>=70]
print(new_marks)
square_marks=[x**2 for x in marks]
print(square_marks)
print(f"maximum marks is {max(marks)}")