from logging import raiseExceptions
import sqlite3
from tokenize import group
from flask import jsonify
from flask_bcrypt import Bcrypt
from numpy import math
import re
import pandas as pd
from sqlite3 import Error

class getDb:
    def __init__(self,data):
        self.table = 'emp1'
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        self.by = Bcrypt()

    def insert(self,data):
        if data['country']=='':
            data['country']='On Earth'
        sql="Insert into emp1 values(?,?,?,?,?,?,?)"
        encrpt=self.by.generate_password_hash(data['pass'])
        data['pass']=encrpt
        try:
            self.c.execute(sql,(data['phone_no'],data['fname'],data['lname'],data['mail'],data['pass'],data['salut'],data['country']))
            obj = self.account(data['mail'],self.c)
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as er:
            print(er)
            
            return -1


        
    def verify(self,data):
        # sql=
        # sql="""Select count(*) from emp1 where email="""+str(data)
        # print(sql)

        self.c.execute("Select * from emp1 where email=? and mail=?",(data[0],data[1],))
        ans =self.c.fetchone()
        if ans is None:
            return None
        else:
            self.c.execute("Select pass from emp1 where email=? and mail=?",(data[0],data[1],))
            ans1 =self.c.fetchone()
            ans1=ans1[0]
            self.conn.close()
            match_pass = self.by.check_password_hash(ans1, data[2])
            if match_pass:
                return ans[1]+" "+ans[2]
            else:
                return -1

    def update(self,data):
        sql ="""Update emp1 set pass= ? where email = ?"""
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        encrpt=self.by.generate_password_hash(data[3])
        data2=(encrpt,data[0])
        self.c.execute("""Update emp1 set pass=? where email=?""",(encrpt,data[0],))
        ans1=self.c.fetchone()
        self.conn.commit()
        self.conn.close()
        return 'Password updated Successfully'


    def pass_return(self,data):
        sql ="""select pass from emp1 where email=? and mail=?"""
        try:

            self.c.execute(sql,(data[0],data[1],))
            ans1=self.c.fetchone()
            self.conn.close()
            print(ans1[0])
            chck1 =  self.by.check_password_hash(ans1[0], data[2])
            chck2=self.by.check_password_hash(ans1[0], data[3])
            print('chk',chck1)
            if chck1 and chck2:
                objt= self.exchange(data)
                return objt
        except :
            return -1

    def exchange(self,data):
        try:
            self.conn=sqlite3.connect('prod.db')
            self.c=self.conn.cursor()
            sql="""Select * from emp1 where email=? and mail=?"""
            print(sql)
            self.c.execute(sql,(data[0],data[1],))
            ans1 =self.c.fetchone()
            print('askk',ans1)
            sql2="""delete from emp1 where email=? and mail=?"""
            self.c.execute(sql2,(data[0],data[1],))
            self.conn.commit
            sql3="Insert into deactivate values(?,?,?,?,?,?)"
            self.c.execute(sql3,(ans1[0],ans1[1],ans1[2],ans1[3],ans1[4],ans1[5],))
            self.conn.commit()
            self.conn.close()
            print('Hello world')
            return 1
        
        except :
            print('failed')
            return -1

    def get_info(self,data):
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        dkeys=data.keys()
        col_ch=self.col_chk(data)
        sql ="Select * from info where"
        data1=[]
        sql2="Select * from info where"
        print('2',data)    
        if col_ch==False:
            return -1
        else:
            for i in dkeys:
                if data[i] !='':
                    sql=sql+' {0} =?'.format(i)
                    # sql2=sql2+'{0}={1}'.format(i,data[i])
                    sql=sql+' and'
                    data1.append(data[i])
            if sql[-3:]=='and':
                sql=sql[:-3]
            if len(data1)==0:
                print('NO Entry made')
            else:

                q_ans=self.db_info(data1,sql)
            

            return 1


        

    def col_chk(self,data):
        lst1=['Roll_no','phone_no','fname','lname' ,'email','mail','country']
        for i in data:
            if i not in lst1:
                return False
        return True

    def db_info(self,data,sql):
        try:
            self.conn=sqlite3.connect('prod.db')
            self.c=self.conn.cursor()
            # sql="""Select * from e where email=? and mail=?"""
            if len(data)==1:
                print(sql)
                print('tyep',type(data[0]))
                self.c.execute(sql,(data[0],))
                ans1 =self.c.fetchall()
                print(ans1)
                # print('in 1')
            elif len(data)==2:
                print(sql)
                self.c.execute(sql,(data[0],data[1],))
                ans1 =self.c.fetchall()
                print(ans1)
                print('in 2')
            elif len(data)==3:
                print(sql)
                self.c.execute(sql,(data[0],data[1],data[2],))
                ans1 =self.c.fetchall()
                print(ans1)
                print('in 3')
            elif len(data)==3:
                print(sql)
                self.c.execute(sql,(data[0],data[1],data[2],))
                ans1 =self.c.fetchall()
                print(ans1)
                print('in 3')
            elif len(data)==4:
                print(sql)
                self.c.execute(sql,(data[0],data[1],data[2],data[3]))
                ans1 =self.c.fetchall()
                print(ans1)
                print('in 3')
            elif len(data)==5:
                print(sql)
                self.c.execute(sql,(data[0],data[1],data[2],data[3],data[4]))
                ans1 =self.c.fetchall()
                print(ans1)
                print('in 3')   
        except:
            print('no data found')


    def update_info(self,data):
        qry="""Update info set """
        count=0
        for key,value in data.items():
            if value!='' and key != 'Roll_no':
                count+=1
                qry=qry+f"{key} ="
                qry=qry+'"'
                qry=qry+f"{value}"
                qry=qry+'"'+','
        qry=qry[:-1]+' '+f' where Roll_no = {data["Roll_no"]} '
        # try:
        if count==0:
            return 'No value Provided'
        else:
            print(qry)
            self.conn=sqlite3.connect('prod.db')
            self.c=self.conn.cursor()
            self.c.execute(qry)
            ans1 =self.c.fetchall()
            self.conn.commit()
            print(qry)
            # except:
            return 'Value Updated'

        
        # return 'Updated '
    def api_post(self,data):
        set=(
        'phone_no',
        'fname' ,
        'lname' ,
        'address' ,
        'b_group' ,
        'country' )
        qry = """Insert into api_tab('phone_no','fname','lname','address','b_group','country') values("""
        for i in set:
            if i in data:
                qry=qry+ "'" +data[i]+"'" +" ,"
            else:
                qry=qry+ "'" +' '+"'" +" ,"
                
        # for keys,values in data.items():
        #     print(keys)
        #     if keys not in set:
        #         return 'Wrong Key'
        #     else:
        #         qry=qry+ "'" +values+"'" +" ,"
        qry=qry[:-1] +")"
        print(qry)
        try:
        # print(qry)
            self.c.execute(qry)
            self.conn.commit()
            self.conn.close()
            return qry
        except :
            
            return 'Input data wrong'


    def dlt_api(self,data):
        qry=" Delete from api_tab where Roll_no = ?" 
        print(data)
        print(type(data))
        try:
            self.c.execute(qry,(str(data)))
            self.conn.commit()
            self.conn.close()
            return 'Deleted Successfully'
        except:
            return 'Wrong id given'
    
    def get_api(self,data):
        qry="""Select * from api_tab where """
        for keys,value in data.items():
            qry=qry+ f"{keys} = '{value}' and "
        qry=qry[:-4]
        print(qry)
        try:
            self.c.execute(qry)
            ans = self.c.fetchall()
            self.conn.commit()
            self.conn.close()
            print(ans)
            print(type(ans))
            return ans
        except:
            return 'Wrong Data'

    def update_api(self,data):
        qry="""Update api_tab set """
        count=0
        for key,value in data.items():
            if value!='' and key != 'Roll_no':
                count+=1
                qry=qry+f"{key} ="
                qry=qry+'"'
                qry=qry+f"{value}"
                qry=qry+'"'+','
        qry=qry[:-1]+' '+f' where Roll_no = {data["Roll_no"]} '
        # try:
        if count==0:
            return 'No value Provided'
        else:
            print(qry)
            self.conn=sqlite3.connect('prod.db')
            self.c=self.conn.cursor()
            self.c.execute(qry)
            ans1 =self.c.fetchall()
            self.conn.commit()
            print(qry)
            # except:
            return 'Value Updated'

    def user_id(self,user_id):
        sql=f"select phone_no from where email={user_id}"
        print(sql)
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        self.c.execute(sql)

        ans1 =self.c.fetchall()
        print(ans1)
        return 
        

    def buyCoin(self,user_id,data):
        # print(data,'data')
        coin_fract=self.coinCal(data)
        # print(data,'data')
        details = self.acc_details(user_id)
        amount = int(details['amount'][0])
        if amount< int(data['buy']):
            return "Insufficient Balance"
        amount =amount-int(data['buy'])
        qry2=f"Update account set amount ='{amount}',acc_updated=datetime('now', 'localtime') where user_id='{user_id}'"
        qry="""Insert into buy('user_id','acc_no','coin_name','at_price','amount','quantity','trx_time') values(?,?,?,?,?,?,datetime('now', 'localtime'))"""
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        print(details)
        act_no=details['account_no'][0]

        try:
            self.c.execute(qry,(user_id,act_no,data['symbol'],data['result'],data['buy'],coin_fract,))
            self.c.execute(qry2)
            # ans1 =self.c.fetchall()
            
            self.coin_bal(self.conn,data,user_id,act_no,coin_fract)
            # if coin_bal_chk==-1:
            #     self.conn.rollback()
            self.conn.commit()
            return 'Transaction success'
        except sqlite3.Error as err:
            print(err)
            self.conn.rollback()
            return 'Transaction failed'
       

    def buyDetails(self,user):
        qry=f"SELECT coin_name as Coin, sum(quantity) as Quantity,sum(amount) as Amount FROM buy where user_id = '{user}' GROUP BY coin_name "
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        try:
            df = pd.read_sql_query(qry, self.conn)
            if len(df.index)==0:
                return 'No Buying made'
            return df
        except sqlite3.Error as err:
            print(err,'buying err')
            return 'No buying made'

        # self.c.execute(qry,(user,))
        # ans1 =self.c.fetchall()
        

    def coinCal(self,data):
        coin_fract=round((float(data['result'])/float(data['buy'])),5)
        coin_fract=round((1/coin_fract),5)
        return coin_fract

    def account(self,data,conn):
        sql="Insert into account('user_id','acc_cr_time','acc_updated') values(?,datetime('now', 'localtime'),datetime('now', 'localtime'))"
        # self.conn=sqlite3.connect('prod.db')
        # self.c=self.conn.cursor()
        try:
            conn.execute(sql,(data,))
            ans1 =self.c.fetchall()
            self.conn.commit()
        except:
            conn.rollback()
        return 1

    def deposit(self,data,user_id):
        usr_acc=self.acc_details(user_id)
        print(usr_acc,'usr_acc')
        acc_nos=usr_acc['account_no'][0]
        usr_bal =usr_acc['amount'][0]
        print(acc_nos,"--->",usr_bal)
        total=int(usr_bal)+int(data)
        print(data,'total')
       
        qry ="Insert into acc_deposit('acc_no','user_id','deposit','acc_updated') values(?,?,?,datetime('now', 'localtime'))"
        qry2=f"Update account set amount ='{total}',acc_updated=datetime('now', 'localtime') where user_id='{user_id}'"
        self.conn=sqlite3.connect('prod.db')
        try:
            self.conn.execute(qry,(acc_nos,user_id,data,))
            self.conn.execute(qry2)
            self.conn.commit()
            self.c.close()
            return 'success'
        except sqlite3.Error as err:
            print(err)
            self.conn.rollback()
            return str(-1)
        return 'failed'
            


        


    

    def acc_details(self,user_id):
        sql =f"Select account_no,amount  from account where user_id ='{user_id}'"
        self.conn=sqlite3.connect('prod.db')
        self.c=self.conn.cursor()
        df = pd.read_sql_query(sql, self.conn)
        return df


    def coin_bal(self,connect,data,user_id,act_no,coin_fract):
        sql=f"select * from coin_bal where user_id ='{user_id}' and coin_name='{data['symbol']}'"
        ans=pd.read_sql_query(sql, connect)
        if len(ans)==0:
            qry ="Insert into coin_bal('user_id', 'acc_no', 'coin_name', 'quantity', 'trx_time') values(?,?,?,?,datetime('now', 'localtime'))"
            try:
                connect.execute(qry,(user_id,act_no,data['symbol'],coin_fract,))
            except sqlite3.Error as err:
                connect.rollback()
        else:
            qry=f"Update coin_bal set quantity= quantity+{coin_fract} where user_id='{user_id}' and coin_name ='{data['symbol']}'"
            try:
                connect.execute(qry)
            except sqlite3.Error as err:
                connect.rollback()
                

            

        print(ans)


        


        
        



        



        









             

    # def pass_check(self,cand_pass):


