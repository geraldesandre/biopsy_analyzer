
from flask import Flask, render_template, url_for, request, redirect, session, escape
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'



# @app.route('/')
# def index():
#     return render_template("index2.html")


@app.route('/diagnose_sample', methods=['POST'])
def diagnose_sample():

    if request.method == 'POST':

        print('Calling NEW special POST')

        return 'Return message'




@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        print('CALLED POST METHOD')

        if 'modal_visible' in session:
            session['modal_visible'] = not session['modal_visible']
        else:
            session['modal_visible'] = True

        # return "The image is now being diagnosed"
        return redirect('/')

    else:

        print('CALLED GET METHOD')

        if 'modal_visible' in session:
            if session['modal_visible']:
                message = 'Modal is visible'
                return render_template("index.html", param=message)

        message = 'Modal is NOT visible'
        return render_template("index.html", param=message)

        # return render_template('index.html', show_predictions_modal=True)


if __name__ == "__main__":
    app.run(debug=True)
