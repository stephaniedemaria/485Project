import pandas as pd
tweets = pd.read_csv("archive.csv")
tweets.head()

import numpy as np
import matplotlib.pyplot as plt

def get_candidate(row):
    candidates = []
    text = row["text"].lower()
    if "moron" in text:
        candidates.append("moron")
    return ",".join(candidates)
tweets["candidate"] = tweet.apply(get_candidate,axis=1)


# Make a fake dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()
 