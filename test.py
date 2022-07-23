
from operator import methodcaller
from flask import Flask, redirect,render_template,request,url_for,jsonify,flash
import json
import sqlite3
import re
import requests
from dbcon import getDb
from flask_login import LoginManager,UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = b'\x1e\xfb\x06%\xd8IN\x8c\xad@\xe6M'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        f = request.form
        # print(f)
        tbl ={'table':'emp'}
        data=json.dumps(f)
        data1=json.loads(data)
        obj = getDb(tbl)
        # print(data1)
        # print(type(data1['email']))
        mail_1=data1['Email']
        full_mail = mail_1.split('@')
        lst =[]
        lst.append(full_mail[0])
        lst.append(full_mail[1])
        lst.append(data1['pass'])
        ans =obj.verify(lst)
        print(ans)
        if ans ==-1 or ans is None:
            flash('User not found please create account','error')
            return render_template('index.html')
        else:
            return render_template('home.html',user=ans)
    else:
        return render_template('index.html')



    

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method =='POST':
        f = request.form
        tbl ={'table':'emp'}
        data=json.dumps(f)
        data1=json.loads(data)
        obj = getDb(tbl)
        mail_1=data1['mail']
        full_mail = mail_1.split('@')
        data1['mail']=full_mail[0]
        data1['salut']=full_mail[1]
        print(data1)
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        if Pattern.match(data1['phone_no'])==False:
            flash('Enter Valid Phone Number','error')
            return redirect('signup')

        if data1['pass'] != data1['Repass']:
            flash('Password dont match','error')
            return redirect('signup')
        elif len(data1['phone_no'])<10:
            flash('Phone no must be of 10 digit','error')
            return redirect('signup')
        else:
            chk_pass=pass_check(data1['pass'])
            if chk_pass==-1:
                flash('Length of password should be greater tha 8 character','error')
                return redirect('signup')
            elif chk_pass==-2:
                flash('Password should be strong,include 1 num,1 symbol,1 upper and lower charc','error')
                return redirect('signup')
            else:
                expt=obj.insert(data1)
                if expt==-1:
                    flash('Phone/Email  already in use','error')
                    return redirect('signup')
                else:
                    print(data1)
                    return render_template('home.html',user=data1['fname'])

    return render_template('signup.html')



@app.route('/change',methods=['GET','POST'])
def change():
    if request.method=='POST':
        f=request.form
        print(f)
        data=json.dumps(f)
        data1=json.loads(data)
        mail_1=data1['Email']
        full_mail = mail_1.split('@')
        lst =[]
        lst.append(full_mail[0])
        lst.append(full_mail[1])
        lst.append(data1['pass'])
        lst.append(data1['pass1'])
        lst.append(data1['pass2'])
        print('change=',lst)
        if data1['pass1']!=data1['pass2']:
            flash('Password didnt match')
            return redirect('change')
        else:
            obj=getDb('emp1')
            match1 = obj.verify(lst)
            if match1 is None:
                flash('Password/Username entered wrong')
                return redirect('change')
            elif match1==-1:
                flash('Old Password entered wrong')
                return redirect('change')
            else:
                obj2 = obj.update(lst)
                print('test===',lst)
                flash('Password updated successfully')
                return render_template('/index.html')
    return render_template('/change.html')


@app.route('/deactivate',methods=['GET','POST'])
def deactivate():
    if request.method=='POST':
        f=request.form
        data=json.dumps(f)
        data1=json.loads(data)
        mail_1=data1['Email']
        full_mail = mail_1.split('@')
        lst =[]
        lst.append(full_mail[0])
        lst.append(full_mail[1])
        lst.append(data1['pass'])
        lst.append(data1['pass1'])
        obj=getDb('emp1')
        obj1 = obj.pass_return(lst)
        print(obj1,'ghdgshfjdfh')
        if obj1==1:
            flash('Account Deactivated Successfully')
            return render_template('/index.html')
            
        else:
            flash('Pass/Email didnt match')
            return redirect('deactivate')
    return render_template('/deactivate.html')

    # f =request.form
    # data= json.dumps(f)
    # data1=json.loads(data)
@app.route('/price',methods=['GET','POST'])
def price():
    if request.method=='POST':
        f=request.form
        f=json.dumps(f)
        f=json.loads(f)
        print(f)
        
        coin=f['Cname']
        # api=
        api= "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?symbol={0}&amount=1".format(coin)
        # api="https://api.coingecko.com/api/v3/simple/price?ids={0}&vs_currencies=usd".format(coin)
        print(api)
        payload = {}
        headers= {
            "X-CMC_PRO_API_KEY": "2715b13c-4f46-4f41-ba19-9e78817a51f6"
        }
        # x= requests.get(api,headers={"accept": "application/json"})
        x = requests.request("GET", api, headers=headers, data = payload)
        status_code = x.status_code
        result = x.json()
        print(result)
        print(type(result))

        amount=float(result['data']['quote']['USD']['price'])
        # amount=int(amount['usd'])
        print(amount)
        url = "https://api.apilayer.com/exchangerates_data/convert?to=inr&from=usd&amount={0}".format(amount)
        payload1 = {}
        headers1= {
            "apikey": "M5OFl9Hqr31T5mqZusfJb72doOixRuXG"
        }
        x1 = requests.request("GET", url, headers=headers1, data = payload1)
        status_code = x1.status_code
        result1 = x1.json()
        print(type(result1))
        # result1=float(result1)


        
        # x1= requests.get(api,headers={"accept": "application/json"})
        print()

        return render_template('/price.html',inr=result1)
    else:
        return render_template('/price.html')

# @app.route('//user_info/<int:Roll_no>/',methods=['GET'])
@app.route('/user_info',methods=['GET'])
def user_info():
    if request.method=='GET':
        f=request.args
        f=json.dumps(f)
        f=json.loads(f)
       
        print('1',f)
        # if f['phone_no']!='':
        #     f['phone_no']=int(f['phone_no'])
        
        obj=getDb('emp1')
        obj1 = obj.get_info(f)
        


        # print(type(f))
        if isinstance(f,dict):
            return render_template('/infoget.html')
       
    return render_template('/infoget.html')



@app.route('/update_info',methods=['GET','PATCH'])
def update_info():
    f=request.args
    f=json.dumps(f)
    f=json.loads(f)

    obj=getDb('emp1')
    # obj1 = obj.get_info(f)
    return obj.update_info(f)
    # if request.method=='PATCH':
    #     f=request.args
    #     f=json.dumps(f)
    #     f=json.loads(f)
    #     print(f)
    #     obj=getDb('emp1')
    #     obj1=obj.update_info(f)
    #     if isinstance(f,dict):
    #         return render_template('/update_page.html')
       
    # return render_template('/update_page.html')




@app.route('/post_api' ,methods=['POST'])
def post_api():
    f= request.args
    f=json.dumps(f)
    f=json.loads(f)
    obj = getDb('emp1')
    obj=obj.api_post(f)
    return str(obj)

@app.route('/dlt_api/<int:Roll_no>' ,methods=['DELETE'])
def dlt_api(Roll_no):
    # f= request.args
    # f=json.dumps(f)
    # f=json.loads(f)
    obj = getDb('emp1')
    obj=obj.dlt_api(Roll_no)
    return str(obj)

@app.route('/update_api' ,methods=['PATCH'])
def update_api():
    f= request.args
    f=json.dumps(f)
    f=json.loads(f)
    obj = getDb('emp1')
    obj=obj.update_api(f)
    return str(obj)

@app.route('/get_api' ,methods=['GET'])
def get_api():
    f= request.args
    f=json.dumps(f)
    f=json.loads(f)
    obj = getDb('emp1')
    obj=obj.get_api(f)
    return str(obj)




def pass_check(pass_w):
    lst=list(pass_w)
    lst_set=set(lst)
    ch ='@!#$%^&+-?'
    pass_len=False
    is_uppr=False
    is_lwr=False
    is_ch=False
    is_num=False
    if len(pass_w)<8:
        return -1
    else:
        pass_len=True
    for i in pass_w:
        print(i)
        if i.isupper():
            is_uppr=True
        elif i.islower():
            is_lwr=True
        elif i in ch:
            is_ch=True
        elif i.isnumeric():
            is_num=True
        if is_uppr and pass_len and is_lwr and is_ch and is_num:
            return 1
    return -2






    


    





    

    



if __name__ == "__main__":
    app.run(debug=True)