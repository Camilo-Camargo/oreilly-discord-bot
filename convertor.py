import requests
import os
import subprocess
from pdf2docx import Converter 

def download_and_convert(url):
    response = requests.get(url)

    file_name = os.path.basename(url)

    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    file_name_pdf = os.path.splitext(file_name)[0] + '.pdf'
    subprocess.run(['ebook-convert', file_name, file_name_pdf])

    return file_name_pdf
def convert_pdf_to_word(url):
    response = requests.get(url)
    if response.status_code == 200:
        pdf_filename = "file.pdf"
        with open(pdf_filename, 'wb') as file:
            file.write(response.content)

        output_filename = os.path.splitext(pdf_filename)[0] + ".docx"
        cv = Converter(pdf_filename)
        cv.convert(output_filename, start=0, end=None)
        cv.close()

        os.remove(pdf_filename)
        return output_filename
    else:
        raise Exception("The PDF file could not be downloaded.")
