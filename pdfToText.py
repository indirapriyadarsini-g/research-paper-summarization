import PyPDF2

pdf_file = open('ResearchPaper.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract the text from each page
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

pdf_file.close()

# Save the text to research_paper.txt
with open('research_paper.txt', 'w') as f:
    f.write(text)

print('Text saved to research_paper.txt')
