import sqlite3
conn = sqlite3.connect('prod.db')
c=conn.cursor()
c.execute("""Alter table emp1 add column user_id integer unique AUTOINCREMENT""")
# c.execute("Insert into info2 values(25, 9889595800, 'faraz', 'uddin', 'ahmadfaraz', 'gmail','')")
# c.execute("Insert into info2 values(2, 9889595032, 'faraz', 'uddin', 'ahmadfarazuddin01', 'gmail','')")
# c.execute("Insert into info2 values(3, 9889595033, 'faraz', 'siddiqui', 'ahmadfaraz01', 'gmail','')")
# c.execute("delete from api_tab where Roll_no=2")
# c.execute("Insert into api_tab(phone_no,fname,lname,address,b_group,country) values('998959393','aku78','','azadnagar1','','India') ")
# c.execute("""drop table api_tab""")



conn.commit()
# c.execute("""Create table api_tab (Roll_no integer primary key AUTOINCREMENT,
#     phone_no text  not null unique,
#     fname text not null,
#     lname text,
#     address text not null,
#     b_group text,
#     country text default 'India'
# )""")
# print('table created')
# conn.commit()

# c.execute("Insert into emp values('Faraz','uddin',15000)")
# c.execute("Alter table emp add mail_1 text")
# c.execute('drop table emp')
c.execute("""select * from emp1""")

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