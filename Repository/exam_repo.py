from sqlalchemy.orm import Session
from Repository.model import Exam, User


def get_exams_by_userid(db: Session, userId: int):
    user = db.query(User).filter(User.id == userId).first()
    exams = user.exams if user else []
    return exams


def save_exam(db: Session, userId: int, script: str):
    _exam = Exam(userId = userId, script = script)
    db.add(_exam)
    db.commit()
    db.refresh(_exam)
    return _exam