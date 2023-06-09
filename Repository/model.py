from sqlalchemy import Column, Integer, VARCHAR, BIGINT
from Repository.session import Base

class User(Base):
    __tablename__ = "User"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR)
