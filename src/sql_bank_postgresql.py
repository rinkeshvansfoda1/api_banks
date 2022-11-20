import psycopg2

cnn=None


def data():
    lst=[]
    try:
        cnn=psycopg2.connect(database="banks",
                            host="localhost",
                            user="postgres",
                            password="root",
                            port=5432)
        print('database connected')
        cs=cnn.cursor()
        cnn.commit()
        print('Fetching Data......')
        sql='SELECT * FROM banks;'
        cs.execute(sql)
        recs=cs.fetchall()
        # return recs

        for i in recs:
            lst.append({'name':i[0],'id':i[1]})
        return lst

    except psycopg2.OperationalError as e:
        print(e)
    finally:
        if cnn:
            cnn.close()
