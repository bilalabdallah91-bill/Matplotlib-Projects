import random
import pandas as pd
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
# الهدف من الدرس انشاء رسم بياني تلقائي
x_values=[]
y_values=[]
index=count()
def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0,5))
    plt.cla()
    plt.plot(x_values,y_values)

ani=FuncAnimation(plt.gcf(),animate,interval=1000)

plt.tight_layout()
plt.show()