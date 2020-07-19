import pandas as pd
import numpy as np

data = pd.DataFrame({
    "id":np.random.randint(0,2000,20),
    "order_id":np.random.randint(0,60,20),
    "age":np.random.randint(15,70,20)
    })


# 1.SELECT * FROM data;
print(data)

# 2.SELECT * FROM data LIMIT(10);
print(data.head(10))

# 3.SELECT id FROM data; // id是data表的特定一列
print(data.id)

# 4.SELECT COUNT(id) FROM data;
print(data['id'].count())

# 5.SELECT * FROM data WHERE id < 1000 AND age > 30;
print(( data['id']<1000 ) & ( data['age']>4 ))

# 6.SELECT id, COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1 = pd.DataFrame({
    "id":np.random.randint(0,2000,10),
    "order_id":np.random.randint(0,60,10),
    "age":np.random.randint(15,70,10)
    })

table2 = pd.DataFrame({
    "id":np.random.randint(0,2000,10),
    "order_id":np.random.randint(0,60,10),
    "age":np.random.randint(15,70,10)
    })
print(table1.groupby('id').agg({'order_id':pd.Series.nunique}))#分组计数

# 7.SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1, table2, on='id'))

# 8.SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1, table2]).drop_duplicates()) #UNION 操作符选取不同的值

# 9.DELETE FROM table1 WHERE id = 10;
print(table1.loc[table1['id'] == 10])

# 10.ALTER TABLE table1 DROP COLUMN column_name;
print(table1.drop(columns = ['column_name']))