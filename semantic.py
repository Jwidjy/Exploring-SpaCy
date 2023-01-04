import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))      # Output: 0.5929929675536907
print(word3.similarity(word2))      # Output: 0.4041501317354622
print(word3.similarity(word1))      # Output: 0.22358827466989753

# Interesting that cat & monkey has a higher degree of similarity than monkey & banana,
# even though the word length is more similar. 

word4 = nlp("gold")
word5 = nlp("silver")
word6 = nlp("oil")

print(word4.similarity(word5))      # Output: 0.8599958939127074
print(word6.similarity(word5))      # Output: 0.25827076708122343
print(word6.similarity(word4))      # Output: 0.32633358884110636

# Working with vectors, comparing a series of words
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",             # Output: 0.6300651682574135
             "Hello, there is my car",          # Output: 0.8033180111627156
             "I\'ve lost my car in my car",     # Output: 0.6787541016512638
             "I\'d like my boat back",          # Output: 0.5624940517078084
             "I will name my dog Diana"]        # Output: 0.6491444739190607

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# It seems that when the example file is run with the simpler language model
# 'en_core_web_sm' as opposed to the model 'en_core_web_md', the simpler model
# doesn't have word vectors loaded & that resulting similarities are based on
# taggers, parsers & NER (named entity recognition).