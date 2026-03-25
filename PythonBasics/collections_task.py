from collections import Counter, defaultdict, namedtuple

#count the vowels in a sentence using Counter
sentence = 'Hello, I am learning Counter'
sentence = sentence.lower()
vowels = 'aeiou'
vowels_only = [char for char in sentence if char in vowels]
print (vowels_only) #it is list of vowels
vowels_count = Counter(vowels_only)
print (vowels_count)
common = vowels_count.most_common(1)
print(f"Most common vowel: {common}")

#use defaultdict to group a list of words by their length
words = ['cat', 'dog', 'elephant', 'ant', 'bird']
group = defaultdict(list)
for word in words:
    group[len(word)].append(word)  #eg: group[3](list type) so append
print(group)
#use of defaultdict cause it creates the key safely so we don't have to check if the key is present

#create a namedtuple to store employee information
Employee = namedtuple('Employee', ['name', 'id', 'salary'])
e1 = Employee('John', 101, 50000)
e2 = Employee('Sarah', 102, 60000)

print(e1.name)
print(e1.salary)
if e1.salary >45000:
    print(f"Salary of {e1.name} is greater than 45000")