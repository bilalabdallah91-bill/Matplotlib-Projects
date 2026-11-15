from matplotlib import pyplot as plt
import pandas as pd
#plt.style.use('fivethirtyeight')
fata=pd.read_csv('fata.csv')
ages =fata['Age']
bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins=bins,edgecolor='black',log=True)

x=fata['Age'].median()
color='#fc4f30'
plt.axvline(x,color=color,linewidth=2,label='Median')

plt.title('Ages of Respondent')

plt.legend()
plt.tight_layout()
plt.show()