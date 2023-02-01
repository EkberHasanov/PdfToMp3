from typing import Coroutine, List
import PyPDF2
from gtts import gTTS

def read_pdf_content(file_url: str) -> str:
    with open(file_url, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text: List[str] = list()
        for page_number in range(len(pdf_reader.pages)):
            current_page = pdf_reader.pages[page_number]
            text.append(current_page.extract_text())
        text_content = '\n'.join(text)
        return text_content

async def generate_audio(text: str, file_name: str) -> None:
    tts = gTTS(text=text, lang='en')
    tts.save(f"uploads/{file_name}.mp3")
