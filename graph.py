import matplotlib.pyplot as plt
import pandas as pd

headers = ['Word', 'Frequency']

df = pd.read_csv('trumpwords.csv', delimiter=",", names=headers)
x = df['Word']
y = df['Frequency']

plt.bar(x, y)
plt.xlabel('Bad Word')
plt.ylabel('Number of times used')
plt.title('Frequency of bad words used in Trump's tweets')
plt.show()


