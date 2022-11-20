import psycopg2

cnn=None

def data(id,branch):
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
        sql=("Select banks.name,branches.ifsc,branches.bank_id,branches.branch,branches.address,branches.city,branches.district,branches.state FROM branches INNER JOIN banks ON branches.bank_id=banks.id where bank_id={} and branch='{}';".format(id,branch))
        # or sql="Select banks.name,* FROM branches INNER JOIN banks ON branches.bank_id=banks.id where bank_id=60 and branch='RTGS-HO';"
        cs.execute(sql)
        recs=cs.fetchall()
        # return recs
        for i in recs:
            lst.append({'Bank Name':i[0],
                        'IFSC':i[1],
                        'Id':i[2],
                        'Branch':i[3],
                        'Address':i[4],
                        'City':i[5],
                        'District':i[6],
                        'State':i[7]})
        return lst

    except psycopg2.OperationalError as e:
        print(e)
    finally:
        if cnn:
            cnn.close()
