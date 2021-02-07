
# Import Flask libraries
from flask import Flask, render_template, request

# Import CORS - needed to allow access to local DZI files
from flask_cors import CORS

# Configure the Flask app
app = Flask(__name__)
CORS(app)

# Route for the main page - simply render the index.html
@app.route('/')
def index():
    return render_template("index.html")

# Route for the POST call /diagnose_sample
#   - This function should be modified to include the ML analysis of the sample
#   - For now it only returns the text message "The image is now being diagnosed"
#
#   - OBS: The returned value of this route is not used to refresh the web page as this behavior was disabled with the
#   AJAX manager. This was done to allow calling the POST without refreshing the page
@app.route('/diagnose_sample', methods=['POST'])
def diagnose_sample():

    if request.method == 'POST':

        return 'The image is now being diagnosed'




if __name__ == "__main__":
    app.run(debug=True)
