import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Credit card transactions - India - Simple.csv')
temp = df.copy()

#......................... i ans .......................

temp = df[(df['Exp Type'] == 'Travel') & (df['Gender'] == 'M')]
print("\n\n",temp['Amount'].sum())

#......................... ii ans .......................

temp2 = df['City'].value_counts()
male = (temp2 & (df['Gender'] == 'M'))
female = (temp2 & (df['Gender'] == 'F'))

print("\nMale : ",male ,"\nFemale : ", female)


#......................... iii ans .......................

print("\n",df['Card Type'].value_counts())
print("\n",df['Exp Type'].value_counts())

#......................... iv ans ..........................

sns.boxenplot(df['Amount'],df['Exp Type'])
plt.show()