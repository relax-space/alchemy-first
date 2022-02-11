'''
说明: alchemy 通过sql 实现增删改查
'''
from sqlalchemy import create_engine, text

engine = create_engine(
    'mysql+mysqldb://root:1234@localhost:3306/test1', echo=True)

# 清空表
engine.execute(text('truncate table book2'))

# 新增2条数据
data = [{'name': 't1', 'price': 10}, {
    'name': 't2', 'price': 12}]
res = engine.execute(
    text('insert into book2(name,price) values(:name,:price)'), data)
assert 2 == res.rowcount

# 删除第二条数据
res = engine.execute(
    text('delete from book2 where name=:name'), {'name': 't2'})
assert 1 == res.rowcount

# 更新第一条数据
res = engine.execute(text('update book2 set price=:price where name=:name'), {
    'name': 't1', 'price': 20})
assert 1 == res.rowcount

# 查询第1条数据
res = engine.execute(text('select * from book2'))
result = res.all()
for i in result:
    assert 't1' == i.name
    assert 20 == i.price
    assert 1 == i.id
print(result)
