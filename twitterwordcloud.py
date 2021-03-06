import nltk
from nltk.corpus import stopwords
#from nltk.corpus import wordnet
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

#Models menu -> select punckt -> click download
#Also download stopwords and wordnet
#nltk.download_gui() 


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
wordcloud = WordCloud(background_color="white",width=1200,height=1000,
max_words=400,collocations=False,stopwords= stopwords.words("english")).generate(sentence)
plt.figure( figsize=(20,10), facecolor='k' )
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()