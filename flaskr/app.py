
from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/diagnose_sample', methods=['POST'])
def diagnose_sample():

    if request.method == 'POST':

        print('Calling NEW special POST')

        return 'The image is now being diagnosed'


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
