from collections import Counter
class Dataset:
    def __init__(self,data):
        self.data = data
        self.size = len(data)
    def get_size(self):
        return self.size
    def describe(self):
        print(f"Dataset with {self.size} samples")

class LabeledDataset(Dataset):
    def __init__(self, data, labels):
        super().__init__(data)
        self.labels = labels
        self.n_classes = len(set(labels)) #to count unique labels
    def describe(self):
        super().describe()
        print(f"Number of classes is {self.n_classes}")
    def get_class_distribution(self):
        count = Counter(self.labels)
        return count

data = [[1,2], [3,4], [5,6], [7,8]]
labels = ["A", "B", "A", "B", "C"]

my_dataset = LabeledDataset(data, labels)
my_dataset.describe()
print(my_dataset.get_class_distribution())
print(f"Size: {my_dataset.get_size()}")
