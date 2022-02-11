import os
import sys

from sqlalchemy import delete, select, update


def main():
    # truncate book3
    Base.metadata.drop_all(engine, tables=[Book3.__table__])
    Base.metadata.create_all(engine)

    # 新增两条数据
    books = [Book3(name='t1', price=12), Book3(name='t2', price=24)]
    session.bulk_save_objects(books)
    session.commit()

    # 新增第3条数据
    book3 = Book3(name='t3', price=36)
    res = session.add(book3)
    session.flush()
    last_id = book3.id
    print(last_id, res)
    session.commit()

    # 删除第二条数据
    stmt = delete(Book3).where(Book3.name == 't2')
    res = session.execute(stmt)
    session.commit()
    assert 1 == res.rowcount

    # 修改第3条数据
    stmt = update(Book3).values(price=37).where(Book3.id == last_id)
    res = session.execute(stmt)
    session.commit()
    assert 1 == res.rowcount

    # 查询结果
    res = session.execute(select(Book3))
    result = res.scalars()
    row1, row2 = result
    assert 1 == row1.id and 't1' == row1.name and 12 == row1.price
    assert 3 == row2.id and 't3' == row2.name and 37 == row2.price


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath('./'))
    from v2.orm_dto import Base, Book3, engine, session
    main()
