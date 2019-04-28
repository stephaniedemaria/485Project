import nltk
from nltk.corpus import stopwords
#from nltk.corpus import wordnet
import string
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import os
from os import path, getcwd
from PIL import Image
import numpy as np


#Models menu -> select punckt -> click download
#You need to do this step once
#nltk.download_gui()


#set path of data files...change the path on your computer in order for this to run
path = '/Users/emilyalvarado/Documents/GitHub/485Project/archive'
donaldmask = np.array(Image.open(path, "donald.png")))

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


#Wordcloud
wordcloud = WordCloud(background_color="white", width=1200,height=1000,
max_words=400, mask=donaldmask, collocations=False).generate(sentence)
image_colors = ImageColorGenerator(donaldmask)
fig, axes = plt.subplots(1, 3)
axes[0].imshow(wordcloud, interpolation="bilinear")
axes[1].imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()