#task: build a simple class to represent a single data point in a dataset

class DataPoint:
    def __init__(self, features, label):
        self.features = features
        self.label = label
        self.is_normalized = False

    def normalize(self):
        print("Normalizing features...")
        self.is_normalized = True

    def describe(self):
        print(self.label)
        print(self.is_normalized)

point = DataPoint([5.1, 3.5, 1.4, 0.2], "setosa")
point.describe()
point.normalize()
point.describe()
