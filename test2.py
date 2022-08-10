import sqlite3
import pandas as pd
conn = sqlite3.connect('prod.db')
c=conn.cursor()

# qry =f"""select account_no as temp from account where user_id ='faraz'"""
# print(qry)
# c.execute("""Alter table emp1 add column user_id integer unique AUTOINCREMENT""")
# c.execute("Insert into info2 values(25, 9889595800, 'faraz', 'uddin', 'ahmadfaraz', 'gmail','')")
# c.execute("Insert into info2 values(2, 9889595032, 'faraz', 'uddin', 'ahmadfarazuddin01', 'gmail','')")
# c.execute("drop table buy")
# c.execute("delete from api_tab where Roll_no=2")
# c.execute("drop table acc_deposit")
# c.execute("""BEGIN TRANSACTION""")


# CREATE TABLE account (
#     user_id   text not null ,
#     amount integer default 0,
#     FOREIGN KEY (amount)
#        REFERENCES emp1 (email) 
# );

# conn.commit()
# c.execute("""CREATE TABLE buy (
#    trx_id integer primary key AUTOINCREMENT,
#    user_id text not null,
#    acc_no text not null,
#    coin_name text not null,
#    amount integer not null,
#    quantity integer not null,
#    trx_time text not null,
#    FOREIGN KEY (acc_no)
#        REFERENCES account(account_no),
#     FOREIGN KEY (user_id)
#        REFERENCES emp1(email)

# )""")
# print('table created')
# conn.commit()

# c.execute("Insert into emp values('Faraz','uddin',15000)")
# c.execute("Alter table emp add mail_1 text")
# c.execute('drop table emp')
c.execute("""select * from sell""")
conn.commit()
# df = pd.read_sql_query(qry, conn)

ans = c.fetchall()

print((ans))

# c.execute('SELECT name from sqlite_master where type= "table"')
# conn.commit()
# conn.close()

# from flask_bcrypt import Bcrypt

# by = Bcrypt()

# s = by.generate_password_hash('Alia@123')
# print(s)
# print(by.check_password_hash('$2b$12$ZgFiZtIaEKYZLpflpgkBo.K9t2ol2RqD04tbCz9Q/.1FC6c5QdmwO,'Alia@123'))

# sql="Update emp1 set pass=1234 where email ='rk'"
# c.execute("""Update emp1 set pass=? where email =?""",('1234','rk'))
# ans=c.fetchall()
# conn.commit()
# conn.close()
# print(ans)

#  b'$2b$12$YDz2Nvznp/dYx0.xeDBbDulkuG76Xm7duuL0mzIF8aYsYBniiU2Eu'
#  b'$2b$12$.ZVGi.aHMkmh1sAONTOvmuTcsFs1Jr0m2OcK1mNGVMPgliNFTUmoq'