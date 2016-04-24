from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split


class MLAnalysis():
	def __init__(self):
		self.linreg = LinearRegression()

	def fitdata(self, dataset, target):
		self.linreg.fit(dataset, target)

	def validate(self, dataset):
		pass

	def predict(self, dataset):
		return self.linreg.predict(dataset)
