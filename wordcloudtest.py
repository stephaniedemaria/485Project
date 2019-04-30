import numpy as np
import csv
import random
from nltk.corpus import stopwords
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib as plt
import os


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(10, 50)

csv_path = "archive.csv"
fa_path = "/Users/emilyalvarado/Sites/485Project/"

icon = "github"
	
# http://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
icon_path = fa_path + "donald.png"
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

wc = WordCloud(background_color="white", max_words=2000, mask=mask,
               max_font_size=300)
               
# generate word cloud
wc.generate_from_frequencies(words_array)
wc.recolor(color_func=grey_color_func)
wc.to_file("github_wordcloud.png")