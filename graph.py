#import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  Number
#left = [50, 100, 150, 200, 250, 300] 
  
# heights of bars (Number of times)
# #height = [10, 24, 36, 40, 5] 
  
# labels for bars 
#tick_label = ['one', 'two', 'three', 'four', 'five'] (Insults)
  
# plotting a bar chart 
#plt.bar(left, height, tick_label = tick_label, 
        #width = 0.8, color = ['orange']) 
  
# naming the x-axis 
#plt.xlabel('Most popular insults in @RealDonaldTrump tweets') 
# naming the y-axis 
#plt.ylabel('Number of Uses') 
# plot title 
#plt.title('All of the insults Trump Uses!') 
  
# function to show the plot 
#plt.show() 


import numpy as np
import matplotlib.pyplot as plt
 
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
 