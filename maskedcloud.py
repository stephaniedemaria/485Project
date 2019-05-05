#####We could not finish this in time because of env issues 
import nltk
from nltk.corpus import stopwords
#from nltk.corpus import wordnet/stopwords/punckt
import numpy as np
import csv
from PIL import Image
import string
import random
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import os

#Copy path from archive file but don't include csv
path = '/Users/emilyalvarado/Documents/GitHub/485Project/archive'

#create empty list sentences
sentence = ""

#loop to open files and save lines to sentence
for filename in os.listdir(path):
    with open(os.path.join(path,filename), "r", encoding='utf8') as f:
        for line in f:
            sentence = sentence + line

#Remove leading and ending whitespace
sentence = sentence.strip()
print("Remove whitespaces:",sentence)

#All lowercase
sentence = sentence.lower()
print("Lowercase:",sentence)

#Remove punctuations
sentence = sentence.translate(str.maketrans('','',string.punctuation))
print("Remove punctuation:",sentence)

#Remove numbers
sentence = sentence.translate(str.maketrans('','','0123456789'))
print("No numbers sentence:",sentence)
    
#Create tokens for the text
tokens = nltk.word_tokenize(sentence)
print("Tokenization:",tokens)

#Remove stop words
stops = set(stopwords.words("english"))
for token in tokens:
    if token in stops:
        tokens.remove(token)
print("Remove stop words:",tokens)

#Stemming
print("Stemming Tokens")
stemmer = nltk.stem.SnowballStemmer('english')
for token in tokens:
    print(token,"becomes ",end='')
    token = stemmer.stem(token)
    print(token)

#Lemmatization
print("Lemmatize Tokens")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for token in tokens:
    print(token,"becomes ",end='')
    token = lemmatizer.lemmatize(token)
    print(token)
        
#Word frequency distribution
print("Word Frequency")
print(tokens)
wordfreqdist = nltk.FreqDist(tokens)
mostcommon = wordfreqdist.most_common(10000)
print(mostcommon)


def orange_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(24, 99%%, %d%%)" % random.randint(40, 70)

mask =np.array(Image.open("/Users/emilyalvarado/Documents/GitHub/485Project/images/donald.jpg"))
wordcloud = WordCloud(background_color="white",
                        max_words=600,
                        mask=mask,
                        random_state=5,
                        stopwords= stopwords.words("english")
).generate(sentence)
plt.imshow(wordcloud.recolor(color_func=orange_color_func, random_state=5))
plt.axis("off")
plt.show()
