from collections import Counter

# Open the text file in read mode and read the contents
with open('research_paper.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text into sentences
sentences = text.split('. ')

# Calculate the frequency of each word in the text
word_freq = Counter(text.split())

# Calculate the score of each sentence based on the frequency of its words
scores = {}
for sentence in sentences:
    for word in sentence.split():
        if word in word_freq:
            if len(sentence.split()) < 30:
                if sentence not in scores:
                    scores[sentence] = word_freq[word]
                else:
                    scores[sentence] += word_freq[word]

# Get the top 3 sentences with the highest scores
summary = ' '.join([sentence for sentence, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]])

# Print the summary
print("Summary")
print(summary)
