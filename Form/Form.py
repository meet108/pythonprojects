from flask import *

app = Flask(__name__)


@app.route('/')
def load_page1():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():
    Firstname = request.form.get('fn')
    Lastname = request.form.get('ln')
    Username = request.form.get('un')
    Password = request.form.get('pw')
    Address = request.form.get('ad')
    Gender = request.form.get('gender')
    City = request.form.get('city')
    Hobby = request.form.getlist('hobby')
    Hobbies = "-".join(Hobby)
    return 'Firstname:{}<br> Lastname:{}<br> Username:{}<br> Password:{}<br> Address:{}<br> Gender:{}<br>City:{}<br> Hobbies:{}'.format(
        Firstname, Lastname, Username, Password, Address, Gender, City, Hobbies)


if __name__ == '__main__':
    app.run(threaded=True, port=5600)
