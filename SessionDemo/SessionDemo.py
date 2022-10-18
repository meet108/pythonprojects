from flask import *

app = Flask(__name__)
app.secret_key = "demo"

@app.route('/')
def load_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    Name = request.form.get("n")
    session['k1'] = Name
    return render_template('PageOne.html')

@app.route('/sessionone')
def sessionone():
    data = session.get('k1')
    print("data: ",data)
    return render_template('PageTwo.html')

if __name__ == '__main__':
    app.run(threaded=True,debug=True)
