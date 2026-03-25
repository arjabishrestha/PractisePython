class Normalizer:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
    def __call__(self, value):
        normalized = (value - self.mean) / self.std
        return normalized
    def __str__(self):
        return f"Normalizer(mean = {self.mean}, std = {self.std})"
    def normalize_batch(self, values):
        norm_list = []
        for i in values:
            norm_value = self(i)  #same as self.__call__(i)
            norm_list.append(norm_value)
        return norm_list
    #norm_list = [self(x) for x in values] using list comprehension 

norm = Normalizer(50,10)
print(norm)
norm_result = norm(70)
print(f"Normalized form of 70 is {norm_result}")

batch = [50,60,70]
#to normalize this batch using normalizer class
norm_result_batch = norm.normalize_batch(batch)
print(f"Normalized batch : {norm_result_batch}")

