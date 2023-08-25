from fastapi import UploadFile
from pdf2image import convert_from_path
import PyPDF2
import os
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\BS871\Desktop\Tesseract-OCR\tesseract.exe'


async def read_pdf_files(file: UploadFile):
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
            images = convert_from_path(file_path, poppler_path=r'C:\Users\BS871\Desktop\poppler-23.05.0\Library\bin')

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

    return contents_of_first_page

