import re
from nltk import ngrams
from collections import Counter
text = """The girl bought a chocolate
        The boy ate the chocolate
        The girl bought a toy
        The girl played with the toy"""

def ngram_model(corpus, n):
    tokens = re.findall(r'\b\w+\b', corpus)
    n_grams = list(ngrams(tokens, n))

    total_ngrams = len(n_grams)
    ngram_probabilities = Counter(n_grams)
    for ngram in ngram_probabilities:
        ngram_probabilities[ngram] /= total_ngrams
    
    return ngram_probabilities

def predic_next_word(ngram_probabilities, n, user_input):
    ngram = tuple(user_input.split()[-n+1:])
    next_word = max(ngram_probabilities, key=lambda x: ngram_probabilities[x] if x[:-1] == ngram else 0)
    return next_word[-1]

# n = int(input("Enter the value of n: "))
n = 2

user_input = input("text here: ")
ngram_model = ngram_model(text, n)
print(predic_next_word(ngram_model, n, user_input))
