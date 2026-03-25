#build a base Model class and a specific Linear Model that inherits from it

class Model:
    def __init__(self, name):
        self.name = name
        self.is_fitted = False
    def fit(self):
        print(f"Fitting {self.name}")
        self.is_fitted = True
    def predict(self):
        if self.is_fitted == False:
            print("Error: Model not fitted")
        else:
            print("Predicting...")

class LinearRegression(Model):
    def __init__(self, name, learning_rate):
        super().__init__(name)
        self.learning_rate = learning_rate
    def describe(self):
        print(f"Model name : {self.name}")
        print(f"Learning rate = {self.learning_rate}")
        print(f"fitted:{self.is_fitted}")

my_model = LinearRegression("model_1",0.01)
my_model.predict()
my_model.fit()
my_model.predict()
my_model.describe()

