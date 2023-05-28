import mysql.connector


def checkDB():
    mydb = mysql.connector.connect(user='root', password='Vojtakropi21',
                                   host='docker-db-1',
                                   database='names')
    mycursor = mydb.cursor()

    sql = "INSERT INTO counts (count, Filename) VALUES (%s, %s)"
    val = (2, "test")
    mycursor.execute(sql, val)

    mydb.commit()

    mydb.close()

def countMarek(filename, text):
    counts = text.lower().count('marek')

    mydb = mysql.connector.connect(
        user='root',
        password='Vojtakropi21',
        host='docker-db-1',
        database='names'
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO counts (count, Filename) VALUES (%s, %s)"
    val = (counts, filename)
    mycursor.execute(sql, val)

    mydb.commit()

    mydb.close()


def getcount():
    mydb = mysql.connector.connect(user='root', password='Vojtakropi21',
                                   host='docker-db-1',
                                   database='names')
    mycursor = mydb.cursor()

    sql = "SELECT * from  counts"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    flag = False
    jsondata = '{"results": ['
    for a in myresult:
        if (flag):
            jsondata = jsondata + ","
        jsondata = jsondata + '{"occurences" : ' + str(a[1]) + ', "file" : "' + a[2] + '"}'
        flag = True
    jsondata = jsondata + ']}'
    mydb.close()
    return jsondata
