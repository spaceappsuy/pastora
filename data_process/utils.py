import pandas as pd
import numpy as np


class ProcessCSV():
	'''
		This class provides the basic methods for process and 
		give a numpy dataset for be used in a ML algorithm
	'''
	def __init__(self):
		self.data = []
		self.target = []

	# FIXME: error_bad_lines should be True for strict validation
	def read_csv(self, name):
		self.data = pd.read_csv(name, error_bad_lines=False)

	def fix_data(self, fix_value, value):
		self.data = self.data.replace(fix_value, value)

	def parse_data(self, column):
		fields_to_parse = []

		for val in self.data[column]:
			if not(val in fields_to_parse):
				fields_to_parse.append(val)

		items = [ item for item in range(0, len(fields_to_parse)) ]

		self.data = self.data.replace(fields_to_parse, items)

	def parse_data_to_numpy_arrays(self, dataframe, columns):
		return dataframe[columns]
