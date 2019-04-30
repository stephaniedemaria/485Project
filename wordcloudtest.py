import nltk
from nltk.corpus import stopwords
#from nltk.corpus import wordnet
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from os import path
from PIL import Image
import numpy as np


#Models menu -> select punckt -> click download
#You need to do this step once
#nltk.download_gui()


#set path of data files...change the path on your computer in order for this to run

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d,'donald.png')).read()

donald_mask = np.array(Image.open(path.join(d,"donald.png")))



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
print("****Let's stem tokens:****")
stemmer = nltk.stem.SnowballStemmer('english')
for token in tokens:
    print(token,"becomes ",end='')
    token = stemmer.stem(token)
    print(token)

#nltk.download('wordnet')#Another way of downloading package instead of GUI
#Lemmatization
print("####Let's lemmatize tokens:####")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for token in tokens:
    print(token,"becomes ",end='')
    token = lemmatizer.lemmatize(token)
    print(token)
        
#Word frequency distribution
print("@@@@Give me word frequency distribution@@@@")
print(tokens)
wordfreqdist = nltk.FreqDist(tokens)
mostcommon = wordfreqdist.most_common(400)
print(mostcommon)

wc = WordCloud(background_color="white", max_words=2000, mask=donald_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

wc.generate(text)
wc.to_file(path.join(d, "donaldt.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(donald_mask, interpolation='bilinear')
plt.axis("off")
plt.show()