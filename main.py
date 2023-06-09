from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import PyPDF2
import openai
import json
import Repository.model as model
from Repository.session import engine
import router

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


app.include_router(router.router, prefix="/api/user", tags=["user"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/questFromPDF/")
async def genereate_quest_frompdf(no_of_quest: int, file: UploadFile):
    try:
        # creating a pdf reader object
        reader = PyPDF2.PdfReader(file.file)
        contents_of_first_page = reader.pages[0].extract_text()
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"message": {str(e)}}

    openai.api_key = settings.openai_api_key

    data_format = '[' \
                  '    {' \
                  '        "id": "1",' \
                  '        "question": "Here goes the question",' \
                  '        "options": ["option 1", "option 2", "option 3", "option 4"]' \
                  '        "answer": "answer of the question among the options"' \
                  '    }' \
                  ']'

    model = "gpt-3.5-turbo"
    prompt = f"""
    Create ```{no_of_quest}``` mcq questions along with 4 options for each questions from the content ```{contents_of_first_page}```.
    Format the content of your response as a JSON object with "Question" and "Options" as the keys for each
    "Question" and "Options" pair. In the "Options" key there will be 4 comma seperated options. Give each question an id
    """

    prompt = f"""
       Create ```{no_of_quest}``` mcq questions along with 4 options for each questions from the content ```{contents_of_first_page}```.
       Format the content of your response as a JSON object with "Question", "Options" and "Answer" as the keys. An example response
       format is {data_format}
       """

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )

    return json.loads(response.choices[0].message["content"])
