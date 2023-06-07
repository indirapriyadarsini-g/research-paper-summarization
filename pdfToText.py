import PyPDF2
def toword(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create output file and write text to it
    with open('output.txt', 'w',encoding="utf-8") as output_file:
        for page in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page].extract_text() 
            output_file.write(page_text)

    # # Load the text data
    with open('output.txt', 'r',encoding='utf-8') as input_file:
        text = input_file.read()
    print(text)
    return text

