
from flask import Flask, render_template, url_for, request, redirect, session, escape
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'




@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        if 'modal_visible' in session:
            session['modal_visible'] = not session['modal_visible']
        else:
            session['modal_visible'] = True

        return redirect('/')

    else:

        if 'modal_visible' in session:
            if session['modal_visible']:
                message = 'Modal is visible'
                return render_template("index.html", param=message)

        message = 'Modal is NOT visible'
        return render_template("index.html", param=message)


if __name__ == "__main__":
    app.run(debug=True)
