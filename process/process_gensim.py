import gensim
from gensim import summarize

# Open the text file
with open('research_paper.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text
tokens = gensim.utils.tokenize(text)

# Join the tokens into a string
text = ' '.join([token for token in tokens])

# Summarize the text
summary = summarize(text)

# Print the summary
print(summary)
