import PyPDF2

pdf_file = open('ResearchPaper.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract the text from each page
text = ""
for page_num in range(len(pdf_reader.pages)):
    # Get the text from the current page
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
 # Add the text from the current page to the string
        text += page_text

pdf_file.close()

# Save the text to research_paper.txt
with open('research_paper.txt', 'w',encoding='utf-8') as f:
    f.write(text)

print('Text saved to research_paper.txt')
