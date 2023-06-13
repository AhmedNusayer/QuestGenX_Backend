from fastapi import APIRouter
from config import settings
from fastapi import UploadFile
from pdf2image import convert_from_path

import PyPDF2
import os
import pytesseract
import openai
import json

from Services import audio_service


router = APIRouter()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@router.post('/generateQuestion')
async def generate_question(no_of_quest: int, file: UploadFile):
    try:
        # Save the uploaded file to disk
        file_path = f"temp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # creating a pdf reader object
        reader = PyPDF2.PdfReader(file.file)
        contents_of_first_page = reader.pages[0].extract_text()
        if contents_of_first_page == "":
            print("scanned pdf")
            images = convert_from_path(file_path, poppler_path=r'E:\poppler-23.05.0\Library\bin')

            texts = []
            for i, image in enumerate(images):
                text = pytesseract.image_to_string(image, lang='Bengali')
                texts.append(text)
                break

            contents_of_first_page = texts

        # Remove the temporary file
        os.remove(file_path)
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
       Format the content of your response as a JSON object with "Question", "Options" and "Answer" as the keys. The "Answer"
       should be among the options.  An example response format is {data_format}
       """

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )

    # return response
    return json.loads(response.choices[0].message["content"])


@router.post('/evaluateSpeech')
async def evaluate_speech(file: UploadFile):
    file_path = file.filename

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    audio_data = audio_service.get_large_audio_transcription_on_silence(file_path)

    openai.api_key = settings.openai_api_key
    model = "gpt-3.5-turbo"

    prompt = f"""
           You are an English language learning assistant. The student has given you the text {audio_data}.
           Give a review of this text. Mention if there is any grammatical error or not. 
           Give your review in points and in a friendly tone. If there is any room for improvement
           then suggest it too.
           """

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )

    os.remove(file_path)

    return response.choices[0].message["content"]

