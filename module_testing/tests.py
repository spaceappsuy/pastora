import os
import numpy as np

from data_process.utils import ProcessCSV
from data_analysis.utils import MLAnalysis

def test_functionality():
	csv_vegetation_composition = ProcessCSV()
	ml_p = MLAnalysis()

	csv_vegetation_composition.read_csv(
		os.getcwd() + '/module_testing/' + 'LC09_Vegetation_Composition_Structure.csv'
	)

	# Refix data
	csv_vegetation_composition.fix_data(-9999, 0)
	csv_vegetation_composition.fix_data('No data reported', 'no')
	csv_vegetation_composition.parse_data('Location')
	csv_vegetation_composition.parse_data('Num_burn')
	csv_vegetation_composition.parse_data('Fert_use')

	veg_composition_x = csv_vegetation_composition.subset_data(
		csv_vegetation_composition.data,
		[
			'Location',
			'Fert_use',
			'Num_ind_und',
			'Num_ind_ovr',
			'Num_burn'
		]
	)

	csv_vegetation_composition.target = get_target_qualification_vegetation(
		veg_composition_x
	)
	csv_vegetation_composition.data = veg_composition_x

	'''
		Format set to predict:
		[location, num_burn, num_ind_avg, fert_use]
	'''

	# FIXME: Change the error fields
	ml_p.fitdata_classification(
		csv_vegetation_composition.parse_to_numpy_array(
			csv_vegetation_composition.data
		),
		csv_vegetation_composition.target
	)
	return ml_p

def get_target_qualification_vegetation(dataframe):
	target = []
	K = 150000
	for datarow in np.array(dataframe):
		num_burn = float(datarow[4]) if datarow[4] != 0 and datarow[4] != -9999 else 1
		num_fert_use = 2 if datarow[1] == 'yes' else 1
		num_ind_avg = 0

		if datarow[2] != -9999:
			if datarow[3] != -9999:
				num_ind_avg = float(np.average([datarow[2], datarow[3]]))
			else:
				num_ind_avg = datarow[2]
		elif datarow[3] != -9999 and datarow[2] == -9999:
			num_ind_avg = datarow[3]

		x = (1 / num_burn) * (num_ind_avg + num_fert_use)
		target.append(int(x*3 / K))

	return np.array(target)
