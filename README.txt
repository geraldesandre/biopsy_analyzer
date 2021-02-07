
***** Instructions on how to install and run the code ***** 


STEP 1 - Activate the Virtual Environment and install all dependencies

	Run the following commands at the root of the project:

		pip install virtualenv
		virtualenv venv
		venv\Scripts\activate
		py -mpip install -r requirements.txt
	
	
STEP 2 - Run the Flask web application
	
	Run the following commands at the root of the project (while still in the virtual environment):
	
		python flaskr/app.py
	

STEP 3 - Access the application

	Open a web browser and access the URL: http://127.0.0.1:5000/
	
	
	
	
***** Basic functionality of the code ***** 

- The main page shows a zoomable image of a biopsy sample displayed with the OpenSeaDragon UI.
- It also contains a button that calls a POST method on http://127.0.0.1:5000/diagnose_sample.
- This method is implemented in the python back end, but it only returns a string saying "The image is now being diagnosed".
- The button also invokes a Bootstrap Modal dialog showing the same message.



***** Generation of the DZI images *****

- To use the OpenSeaDragon UI effectively, the biopsy image has been converted from SVS to DZI format.
- This was done using the library libvips (https://libvips.github.io/libvips/install.html) and following the procedure described here: https://github.com/ashleytowers/OpenSeadragon-Web-Microscopy-Example
	