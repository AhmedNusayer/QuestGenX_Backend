from sqlalchemy.orm import Session
from Repository.model import Exam


def get_exam(db: Session, examId: int):
    return db.query(Exam).filter(Exam.examId == examId).first()


def save_exam(db: Session, userId: int, script: str):
    _exam = Exam(userId = userId, script = script)
    db.add(_exam)
    db.commit()
    db.refresh(_exam)
    return _exam