from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,0,0.1,0]

plt.pie(slices,labels=labels,explode=explode,shadow=True,
autopct='%1.0f%%',startangle=270,wedgeprops={'edgecolor':'black'})
plt.title('My Awsome pie chart')
plt.tight_layout()
plt.show()