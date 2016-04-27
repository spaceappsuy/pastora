from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split


class MLAnalysis():
	def __init__(self):
		self.linreg = LinearRegression()
		self.kclass = KNeighborsClassifier(n_neighbors=3)

	def fitdata_linear_regression(self, dataset, target):
		self.linreg.fit(dataset, target)

	def fitdata_classification(self, dataset, target):
		self.kclass.fit(dataset, target)

	def validate(self, dataset):
		pass

	def predict_linearregression(self, dataset):
		parse_dataset = list(map(float, dataset))
		return self.linreg.predict(parse_dataset)

	def predict_classification(self, dataset):
		parse_dataset = list(map(float, dataset))
		return self.kclass.predict(parse_dataset)
