from app.backand.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    __table_agrs__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(String)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
