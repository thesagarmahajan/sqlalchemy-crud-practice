import sqlalchemy as db
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, select
Base = declarative_base()
class User(Base):
    # Specifying Table name
    __tablename__ = "users"

    # Specifying Columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return f"name='{self.name}', email='{self.email}', password='{self.password}'"

engine = db.create_engine("mysql://root:123123@localhost/sqlalchemy_practice")

with Session(engine) as session:
    statement = select(User)
    result = session.execute(statement).all()
    for user in result:
        u = user._mapping['User']
        print(u.name)
    session.commit()
