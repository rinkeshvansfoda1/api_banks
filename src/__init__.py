from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource


import sql_bank_postgresql
import sql_bank_branch
import sql_bank_detail

app=Flask(__name__)
api=Api(app)

BASE_URL='/api/v1'
@app.route(BASE_URL,methods=['GET','POST'])
def index():
    if request.method=='GET' or request.method=='POST':
        return render_template('index.html')

@app.route(BASE_URL+'/banks',methods=['GET','POST'])
def banks():
    if request.method=='GET' or request.method=='POST':
        data=sql_bank_postgresql.data()
        if len(data)==0:
            return render_template('404.html'),404
        return jsonify(data)


@app.route(BASE_URL+'/banks/<ids>',methods=['GET','POST'])
def branch(ids):
    if request.method=='GET' or request.method=='POST':
        data=sql_bank_branch.data(ids)
        if len(data)==0:
            return render_template('404.html'),404

        return jsonify(data)


@app.route(BASE_URL+'/banks/<idd>/<branchs>',methods=['GET','POST'])
def branch_detail(idd,branchs):
    if request.method=='GET' or request.method=='POST':
        data=sql_bank_detail.data(idd,branchs)
        if len(data)==0:
            return 'page not found',404
        return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)