"""
Create a Dataset class that feels like a native Python object using Magic Methods.
Requirements:
Class name: Dataset
__init__(self, data): Store self.data (a list).
__len__(self): Return the number of samples in self.data.
__str__(self): Return a string like "Dataset with {n} samples".
__repr__(self): Return a string like "Dataset(data={first_item}...)" (show first item only).
Bonus: Add a method get_data() that returns the actual data list.
"""

class Dataset:
    def __init__(self, data):
        self.data =data
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return f"Dataset with {len(self.data)} samples"
    def __repr__(self):
        if len(self.data) == 0:
            return f"Dataset(data=[], size=0)"
        return f"Dataset(data={self.data[0]}, size = {len(self.data)})"
    def get_data(self):
        return self.data

my_dataset = Dataset([])
print(my_dataset)
print(repr(my_dataset))
print(len(my_dataset))
print(my_dataset.get_data())