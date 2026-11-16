import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn-v0_8')

jata=pd.read_csv('jata.csv')
ages=jata['Age']
dev_salaries=jata['All_Devs']
py_salaries=jata['Python']
jv_salaries=jata['JavaScript']
plt.style.use('fivethirtyeight')
fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=1)

ax1.plot(ages,dev_salaries,color='#444444',linestyle='--',label='dev_salaries')
ax2.plot(ages,py_salaries,label='py_salaries')


ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Worker Salary')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Worker Salary')
plt.savefig('biol.png',transparent=True)
plt.tight_layout()
plt.show()