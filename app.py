from flask import Flask, request, url_for, render_template, redirect
from login_signup import check_member, add_new_user
from predict import prediction
import sqlite3

conn = sqlite3.connect('members.db',check_same_thread=False)
cur = conn.cursor()
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    data = {}
    data['isOk'] = True
    data['register'] = False
    if(request.method=='POST'):
        if(request.form['sub_button'] == 'Resume the Party'):
            isThere = check_member(cur,request.form['user_name'],request.form['password'])
            if(isThere):
                return redirect(f"/predict/{request.form['user_name']}")
            else:
                data['isOk'] = False
                return render_template('home.html',data=data)
        else:
            add_new_user(conn,cur,request.form['email'],request.form['user_name'],request.form['password'])
            data['register'] = True
            return render_template('home.html',data=data)
    return render_template('home.html',data=data)

@app.route("/predict/<name>",methods=['POST','GET'])
def predict(name):
    data = {}
    data['predict'] = False
    if(request.method=='POST'):
        data['predict'] = True
        mrp = int(request.form['mrp'])
        product = request.form['product']
        date = int(request.form['date'])
        predicted_valu = prediction(product,mrp,date)
        data['predicted_valu'] = predicted_valu
        data['product'] =  product
        data['mrp'] = request.form['mrp']
        data['date'] = request.form['date']
        return render_template('predict.html',data=data)
    return render_template('predict.html',data=data)


app.run(debug=True)