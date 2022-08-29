import pyttsx3
import PyPDF4

book = open('Lecture 2 DNS Spring22.pdf', 'rb')
reader = PyPDF4.PdfFileReader(book)
pages = reader.numPages
audio = pyttsx3.init()

voices = audio.getProperty('voices')
audio.setProperty('voice', voices[0].id)

for num in range(1, pages):
    page = reader.getPage(num)
    text = page.extractText()
    audio.say(text)
    audio.runAndWait()