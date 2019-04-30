# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.30
 
# set height of bar
bars1 = [33, 22, 68, 17, 80, 64, 192, 85, 70]
bars2 = [234, 222, 204, 183, 156, 115, 215, 232, 83]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Tweets since Trump became president')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='All time tweets by Trump')
 
# Add xticks on the middle of the group bars
plt.xlabel('Inappropriate Words', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Loser', 'Dumb', 'Terrible', 'Stupid', 'Weak', 'Dishonest', 'Witch hunt', 'Hate', 'Hoax']) 
# Create legend & Show graphic
plt.legend()
plt.show()
