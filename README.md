# QuestGenX_Backend

1. python -m venv my_venv
2. For windows: .\my_venv\Scripts\activate, For mac: source ./my_venv/bin/activate
3. pip install -r requirements.txt
4. Create a new file named '.env'
5. Add the following lines in that file:
OPENAI_API_KEY = "your-api-key"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "DB password"
POSTGRES_SERVER = "localhost"
POSTGRES_PORT = 5432
POSTGRES_DB = "DB name"
DATABASE_URL = "postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_SERVER:POSTGRES_PORT/POSTGRES_DB"
TESSERACT_EXE_PATH = "path to the tesseract.exe file"
6. Create a new directory named 'temp'
7. To run: uvicorn main:app --reload


Download 'poppler' from the following link 'https://github.com/oschwartz10612/poppler-windows/releases/tag/v23.05.0-0'

Download Tesseract from the following link
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe

To read Bangla characters download trained data from https://github.com/tesseract-ocr/tessdata/blob/main/script/Bengali.traineddata
Add the downloaded file to 'path-to-tesseract\tessdata' folder.