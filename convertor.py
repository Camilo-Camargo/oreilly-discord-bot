import requests
import os
import subprocess

def download_and_convert(url):
    response = requests.get(url)

    file_name = os.path.basename(url)

    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    file_name_pdf = os.path.splitext(file_name)[0] + '.pdf'
    subprocess.run(['ebook-convert', file_name, file_name_pdf])

    return file_name_pdf
