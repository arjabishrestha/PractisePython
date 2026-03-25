#printing from dictionary
record={
    "Maths":96,
    "English":78,
    "Science":80,
    "Social":70,
    "Nepali":71
}
#print only subjects
for subject in record.keys():
    print(subject)

#print only marks
for marks in record.values():
    print(marks)

#print both
for key,value in record.items():
    print(f"{key}->{value}")