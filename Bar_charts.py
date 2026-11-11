from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

sileces=[120,80,30,20]
labels=['sixty','fourty','Extra1','Extra2']
colors=['#fc4f30','#008fd5','#6d904f','#e5ae37',]
plt.title('My Awsome pie chart')
plt.pie(sileces,labels=labels,colors=colors,wedgeprops={'edgecolor':'black'})
plt.tight_layout()
plt.show()

# Blue=#0008fd5
# Red=#fc4f30
# Yellow=#e5ae37
# Green=#6d904f