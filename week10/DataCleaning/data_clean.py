#查出所有评论，清除掉评论内容为空的包括只含有空格（只有表情评论的）
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from snownlp import SnowNLP

try:
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/python_learn')
except sqlalchemy.exc.OperationalError as e:
    print('Error is '+str(e))
    exit

#数据清洗-》删除评论为空的数据
engine.execute('delete from product_comment where content is null or LENGTH(trim(content)) = 0;');
sql = 'select * from product_comment where is_pos is null;'
df = pd.read_sql_query(sql, engine)
df.dropna(subset=['content'],inplace=True)
pre_sql = 'update product_comment set is_pos = {} where id ={};'
# 将评价结果
for i in range(len(df.index)):
    text = df['content'][i]
    s = SnowNLP(text)
    if s.sentiments < 0.5:
        df.loc[i, 'is_pos'] = '0'
    else:
        df.loc[i, 'is_pos'] = '1'
    engine.execute(pre_sql.format(df.loc[i, 'is_pos'],df.loc[i, 'id'])) 
engine.execute("update product p set p.pos_count = (select count(1) from product_comment c where c.is_pos ='1' and c.product_id = p.id);");
engine.execute("update product p set p.neg_count = (select count(1) from product_comment c where c.is_pos ='0' and c.product_id = p.id)");
    