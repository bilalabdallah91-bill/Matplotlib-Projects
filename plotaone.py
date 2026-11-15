from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')

data=pd.read_csv('data.csv')
ages=data['Age']
dev_salaries=data['All_Devs']
py_salaries=data['Python']
js_salaries=data['JavaScript']

plt.plot(ages,dev_salaries,color='#444444',linestyle=('--'),label='All_Devs')
plt.plot(ages,py_salaries,label='Python')
overall_median=data['All_Devs'].median()

plt.legend()
plt.fill_between(ages,py_salaries,dev_salaries,where=(py_salaries>dev_salaries),
                 interpolate=True,alpha=0.25,label='Above Avg')

plt.fill_between(ages,py_salaries,dev_salaries,color='red',where=(py_salaries<=dev_salaries),
                 interpolate=True,alpha=0.25,label='below Avg')

plt.legend()
plt.xlabel('Ages')
plt.ylabel('Mediun Salary (USD)')
plt.title('Mediun Salary(USD) by age')
plt.show()


