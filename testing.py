# def dcSolv(dc,ans):


#     for key,value in dc.items():
#         if isinstance(value,dict):
            
#             dcSolv(value,ans)
#         else:
#             ans[key]=value
#     return ans


# def solve():
#     dc={'status': {'timestamp': '2022-07-24T19:40:25.567Z', 'error_code': 0,
#      'error_message': None, 'elapsed': 32, 
#      'credit_count': 1, 'notice': None}, 'data': {'id': 1, 'symbol': 'BTC',
#       'name': 'Bitcoin', 'amount': 1, 'last_updated': '2022-07-24T19:39:00.000Z', 
#       'quote': {'USD': {'price': 22780.1459179201, 'last_updated': '2022-07-24T19:39:00.000Z'}}}}
#     ansdict={}
#     ansdict=dcSolv(dc,ansdict)
#     print(ansdict)


# solve()

st = tuple(['a','f','z'])
qry =f"Insert into table{st} values()"
print(qry)

