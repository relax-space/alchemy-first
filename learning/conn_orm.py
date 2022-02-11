'''
说明: orm连接池设置, 如果设置pool_size=5, 那么最多只能开5个连接
'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    price = Column(Integer)


engine = create_engine(
    'mysql+mysqldb://root:1234@localhost:3306/test1', max_overflow=0)
Base.metadata.create_all(engine)

session = Session(engine)
res = session.get(Book, 1)
print(1)

session = Session(engine)
res = session.get(Book, 1)
print(2)

session = Session(engine)
res = session.get(Book, 1)
print(3)

session = Session(engine)
res = session.get(Book, 1)
print(4)

session = Session(engine)
res = session.get(Book, 1)
print(5)

session = Session(engine)
res = session.get(Book, 1)
print(6)

session = Session(engine)
res = session.get(Book, 1)
print(7)


'''
输出: 默认会创建5个连接,所以第6个连接不会创建成功
   1
   2
   3
   4
   5
'''
