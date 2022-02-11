
'''
说明: 连接池设置, 如果设置pool_size=5, 那么最多只能开5个连接
'''
from sqlalchemy import create_engine, text

engine = create_engine('mysql+mysqldb://root:1234@localhost:3306/test1',
                    #    echo=True,
                       pool_size=5,
                       max_overflow=0,
                       pool_recycle=10)

conn1 = engine.connect()
res = conn1.execute(text('select * from book'))

conn2 = engine.connect()
res = conn2.execute(text('select * from book'))

conn3 = engine.connect()
res = conn3.execute(text('select * from book'))

conn4 = engine.connect()
res = conn4.execute(text('select * from book'))

print('1')

conn5 = engine.connect()
res = conn5.execute(text('select * from book'))

print('2')

conn6 = engine.connect()
print('3')
res = conn6.execute(text('select * from book'))

print(res.all())

'''
输出: 不会输出3 
    1
    2
'''
