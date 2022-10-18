from flask import *

app = Flask(__name__)
app.secret_key = "demo"


@app.route('/')
def load_page():
    return render_template("Register.html")


@app.route('/loadLogin')
def loadLogin():
    return render_template("Login.html")


@app.route('/register', methods=['POST'])
def register():
    RegisterFirstName = request.form.get('fn')
    RegisterLastName = request.form.get('ln')
    RegisterUserName = request.form.get('un')
    RegisterPassword = request.form.get('pw')

    session['k1'] = RegisterFirstName
    session['k2'] = RegisterLastName
    session['k3'] = RegisterUserName
    session['k4'] = RegisterPassword

    return render_template('Login.html')


@app.route('/login', methods=['POST'])
def login():
    LoginUserName = request.form.get('un')
    LoginPassword = request.form.get('pw')

    RegisterUserName = session['k3']
    RegisterPassword = session['k4']

    if LoginUserName == RegisterUserName and LoginPassword == RegisterPassword:
        data = session['k1'] + " " + session['k2']
        return render_template("Welcome.html", data=data)
    else:
        flash("Invalid Username or Password")
        return redirect('/loadLogin')


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
