# Setting the positions and width for the bars
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'bad_words': ['Loser', 'Dumb', 'Terrible', 'Stupid', 'Weak', 'Dishonest', 'Witch hunt', 'Hate', 'Hoax'],
        'tweets_office': [33, 22, 68, 17, 80, 64, 192, 85, 70],
        'all_tweets': [234, 222, 204, 183, 156, 115, 215, 232, 80]}
df = pd.DataFrame(raw_data, columns = ['bad_words', 'tweets_office', 'all_tweets'])
df


pos = list(range(len(df['tweets_office']))) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['tweets_office'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['bad_words'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['all_tweets'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['bad_words'][1]) 


# Set the y axis label
ax.set_ylabel('Number of times used')

# Set the chart's title
ax.set_title('Bad Words')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['bad_words'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['tweets_office'] + df['all_tweets'])] )

# Adding the legend and showing the plot
plt.legend(['Tweets as a president', 'All time tweets'], loc='upper left')
plt.grid()
plt.show()