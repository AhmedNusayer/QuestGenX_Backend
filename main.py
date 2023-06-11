from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Repository.session import engine
from Routers import user_router, exam_router

import Repository.model as model


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(user_router.router, prefix="/api/user", tags=["User"])

app.include_router(exam_router.router, prefix="/api/exam", tags=["Exam"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


