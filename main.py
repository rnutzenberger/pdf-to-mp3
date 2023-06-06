import pyttsx3
import pypdf

#Add PDF to same directory and set the file path to the next line below

pdfreader = pypdf.PdfReader(open(r"",'rb')) #enter PDF path in quotes
speaker = pyttsx3.init()

new_page =""
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n' ,' ')
    new_page+=clean_text
    

print(new_page)
speaker.save_to_file(new_page,'resume.mp3')
speaker.runAndWait()

speaker.stop()