from fastapi import APIRouter, Depends
from Repository.session import SessionLocal
from sqlalchemy.orm import Session
from Repository.schemas import RequestUser
import Repository.user_repo as user_repo


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/add_user')
async def add_user(request: RequestUser, db:Session = Depends(get_db)):
    user_repo.add_user(db, request.parameter)
    return request