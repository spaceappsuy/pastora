from rest_framework.response import Response
from rest_framework.views import APIView

from module_testing.tests import test_functionality


class PredictView(APIView):
	'''
		Desc: This View takes an observation about land conditions
		 	  and gives a qualification a number between 0 and 2,
			  being 0 the poorest conditions for raise animals
			  and two the best conditions.
	'''
	ml_instance = test_functionality()

	def get(self, request, format=None):
		if 'num_burn' in request.GET and \
		   'num_ind_avg' in request.GET and \
		   'fert_use' in request.GET:
		   	return Response(self.ml_instance.predict())
		return Response(None)
