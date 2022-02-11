from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Book3(Base):
    __tablename__ = 'book3'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)


engine = create_engine('mysql+mysqldb://root:1234@localhost:3306/test1',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session= Session()
