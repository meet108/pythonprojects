from flask import *
import pymysql

app = Flask(__name__)
app.secret_key = "demo"


def db_connect():
    connection = pymysql.connect(host='localhost', user='root', password='root', db='pythondb')
    return connection


@app.route('/')
def load_page1():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    connection = db_connect()
    Firstname = request.form.get('fn')
    Lastname = request.form.get('ln')
    Username = request.form.get('un')
    Password = request.form.get('pw')
    Address = request.form.get('ad')
    Gender = request.form.get('gender')
    City = request.form.get('city')
    Hobby = request.form.getlist('hobby')
    Hobbies = "-".join(Hobby)

    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into register_table(Firstname,Lastname,Username,Password,Address,Gender,City,Hobby) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            Firstname, Lastname, Username, Password, Address, Gender, City, Hobbies))

    connection.commit()
    print("Insert Successfully")
    cursor1.close()
    connection.close()
    return render_template("register.html")


@app.route("/view", methods=["GET"])
def view():
    connection = db_connect()
    cursor_object = connection.cursor(pymysql.cursors.DictCursor)

    cursor_object.execute("select * from register_table")

    data = cursor_object.fetchall()

    print(data)
    print(type(data))
    connection.commit()
    cursor_object.close()
    connection.close()
    return render_template("display.html", data=data)


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    connection = db_connect()
    cursor_object = connection.cursor()
    cursor_object.execute("Delete from register_table WHERE id='{}'".format(id))
    print("Delete Successfully")
    connection.commit()
    cursor_object.close()
    connection.close()
    return redirect(url_for('view'))
    # return redirect("/view")


@app.route("/edit", methods=["GET"])
def edit():
    id = request.args.get("id")
    connection = db_connect()
    cursor_object = connection.cursor(pymysql.cursors.DictCursor)
    cursor_object.execute("select * from register_table WHERE id='{}'".format(id))
    data = cursor_object.fetchall()
    print("Edit Successfully")
    connection.commit()
    cursor_object.close()
    connection.close()
    return render_template("edit.html", data=data)


@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    Firstname = request.form.get('fn')
    Lastname = request.form.get('ln')
    Username = request.form.get('un')
    # Password = request.form['Password']
    Address = request.form.get('ad')
    # Gender = request.form['Gender']
    # City = request.form['City']
    # Hobby = request.form.getlist('hobby')
    # Hobbies = "-".join(Hobby)
    connection = db_connect()
    cursor_object = connection.cursor(pymysql.cursors.DictCursor)
    # cursor_object.execute(
    # "UPDATE register_table SET (Firstname,Lastname,Username,Address) values ('{}','{}','{}','{}')".format(Firstname, Lastname, Username,Address))
    # "UPDATE register_table SET Firstname='" + Firstname + "',Lastname='" + Lastname + "',Username='" + Username + "',Address='" + Address + "' where id=" + id2)
    cursor_object.execute(
        "UPDATE register_table SET Firstname='{}',Lastname='{}',Username='{}',Address='{}'WHERE id={}".format(Firstname,
                                                                                                                Lastname,
                                                                                                                Username,
                                                                                                                Address,id))
    print("Update Successfully")
    connection.commit()
    cursor_object.close()
    connection.close()

    return redirect('/view')


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=5600)
