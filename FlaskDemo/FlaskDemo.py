from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/load_page')
def load_page():
    return render_template('registerPage.html')

@app.route('/register',methods=['post'])
def register():
    firstname = request.form.get('fn')
    return firstname

if __name__ == '__main__':
    app.run()
