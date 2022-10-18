# pip install pymysql

import pymysql


def insertLogin():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb'
    )

    un = "aa"
    pwd = "bb"
    role = "cc"
    status = "dd"

    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into loginmaster(loginUsername,loginPassword,loginRole,loginStatus) values ('{}','{}','{}','{}')".format(
            un, pwd, role, status))

    connection.commit()


insertLogin()
