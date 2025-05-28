import nltk
from nltk.tokenize import sent_tokenize

corpus = """My name is John. I live in New York City. I love programming in Python.
I also enjoy hiking and photography. The weather here is usually great, but it's get quite cold in winter."""

sentences = sent_tokenize(corpus, language='english')
print(sentences)

# sentences are in form of a list
type(sentences)

# iterate through the sentences

for sentence in sentences:
    print(sentence)

# ------------Convert the Paragraph into the words --------------
# AND Also the sentences into the words

from nltk.tokenize import word_tokenize

words = word_tokenize(corpus)
words


# --------------------------Lets convert the sentences into words------------------------------
# Here we have to loop through the each sentence inside the sentences list 
sentences_words = [word_tokenize(sentence) for sentence in sentences]
sentences_words

from nltk.tokenize import wordpunct_tokenize

# Using wordpunct_tokenize to split words and punctuation
punct_words = wordpunct_tokenize(corpus)
punct_words


from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

# Using TreebankWordTokenizer to tokenize the corpus

treeban_words = tokenizer.tokenize(corpus)
treeban_words