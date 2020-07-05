import pymysql

db_info ={
    'host' :'127.0.0.1',
    'port' :3306,
    'user' :'root',
    'password' :'123456',
    'db':'python_learn'
}

# 1.连接
conn = pymysql.connect(host=db_info['host'], port=db_info['port'], user=db_info['user'], password=db_info['password'], db=db_info['db'], charset='utf8')
print(conn)

cursor = conn.cursor()

sql='insert into maoyan(m_index,title,tag,time) values(%s,%s,%s,%s)'
effect_row=cursor.execute(sql,(1,'111','111','2020-09-01'))   # effect_row=1

#一定记得commit
conn.commit()

sql = "select * from maoyan"
print(sql)
# resultNum = cur.execute(sql,[user,pwd])
resultNum = cursor.execute(sql)
print(resultNum)

# 4.关闭游标
cursor.close()

# 5.关闭连接
conn.close()