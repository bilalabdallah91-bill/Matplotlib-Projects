from matplotlib import pyplot as plt
plt.style.use('seaborn-v0_8')
import pandas as pd
sata=pd.read_csv('sata.csv')
view_count=sata['view_count']
likes=sata['likes']
ratio=sata['ratio']

plt.scatter(view_count,likes,c=ratio,cmap='summer',edgecolor='black',linewidth=1,alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('like/dislike')


plt.xscale('log')
plt.yscale('log')


plt.xlabel('view count')
plt.ylabel('tolal likes')
plt.title('Treanding Youtube Video')
plt.legend()
plt.tight_layout()
plt.show()
