import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
jata=pd.read_csv('jata.csv')

ages=jata['Age']
dev_salaries=jata['All_Devs']
py_salaries=jata['Python']
jv_salaries=jata['JavaScript']

plt.plot(ages,py_salaries,label='py_salaries')
plt.plot(ages,jv_salaries,label='jv_salaries')
plt.plot(ages,dev_salaries,color='#444444',linestyle='--',label='dev_salaries')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Worker Salary')

plt.tight_layout()
plt.show()