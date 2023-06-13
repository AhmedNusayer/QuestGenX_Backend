from sqlalchemy import Column, Integer, VARCHAR, BIGINT, ForeignKey
from Repository.session import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR)
    exams = relationship("Exam", back_populates="user")


class Exam(Base):
    __tablename__ = "exams"

    examId = Column(BIGINT, primary_key=True, autoincrement=True)
    userId = Column(BIGINT, ForeignKey('users.id'))
    script = Column(VARCHAR)
    user = relationship("User", back_populates="exams")