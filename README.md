## Synopsis

Pastora gives the tools for empowering the pastoralism communities via information, with the purpose of make decisions that will improve their quality of life.

## Description of the demo

The application uses a .csv file as sample data source for emulate the behavior of consume data from NASA API, and then create a dataset which it will be used for learn an machine learning algorithm that classify with a number the favorable condition level of a location for development by observating three features(amount of burnings, fertilizer use and vegetation density). Then, these results will display on map suggesting the most favorable and near places of subsisting.

## Instalation

	1. It is recommendable to use a virtual environment.
	2. Execute pip install -r requirements.txt on the root application
	3. You can test the endpoint for predict an observation with the url:

		/api/predict

		that receive num_burn, num_ind_avg and fert_use key names as parameters.

## Additional notes
   **Resources used**
   
	- https://search.earthdata.nasa.gov

	- http://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=939 (Vegetation information)

	- http://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=979 (Precipitation)

   For test the application with a client, also we have an ionic app solution:
   https://github.com/DRivAlegre/client-app-pastora

   If you have any trouble about UTF-8 support when you running the server, you just should execute two lines on the console:
   	
   	export LC_ALL=en_US.UTF-8
	export LANG=en_US.UTF-8

   Right now, it is just the backend application and an endpoint for expose a predict machine learning method.

## TODO
- Add contributor section


