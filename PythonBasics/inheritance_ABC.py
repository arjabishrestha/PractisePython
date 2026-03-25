from abc import ABC, abstractmethod
import numpy as np
class Transformer(ABC):
    @abstractmethod  #decorator that forces this method to be implemented in the child class
    def fit(self, data):
        pass
    @abstractmethod
    def transform(self, data):
        pass
    def __str__(self):
        return f"Transformer : {self.__class__.__name__}" #don't know how to know name of the class here

class Normalizer(Transformer):
    def __init__(self):
        self.mean = 0
        self.std = 1
    def fit(self, data):
        self.mean = sum(data) / len(data)
        self.std = np.std(data)
    def transform(self, data):
        normalized = [(x - self.mean) / self.std for x in data]
        return normalized

class MinMaxScaler(Transformer):
    def __init__(self):
        self.min = 0
        self.max = 0
    def fit(self, data):
        self.min = min(data)
        self.max = max(data)
    def transform(self, data):
        if self.max - self.min == 0:
            return [0.0 for x in data]
        scaled = [(x - self.min) / (self.max - self.min) for x in data]
        return scaled

data = [10, 20, 30, 40, 50]
norm = Normalizer()
print(norm)
norm.fit(data)
print(norm.transform(data))

scaler = MinMaxScaler()
scaler.fit(data)
print(scaler)
print(scaler.transform(data))