from sqlalchemy.orm import Session
from Repository.model import User
from Repository.schemas import UserSchema


def get_user(db:Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()


def add_user(db:Session, user: UserSchema):
    _user = User(email = user.email)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


