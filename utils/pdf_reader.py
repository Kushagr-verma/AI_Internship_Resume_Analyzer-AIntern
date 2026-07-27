import fitz

def read_pdf(path):
    text = ""
    pdf = fitz.open(path)
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text
#retuns the pdf into the text for making pyhton read it 

