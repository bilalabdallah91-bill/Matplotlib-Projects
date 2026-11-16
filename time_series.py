from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
plt.style.use('seaborn-v0_8')

rata=pd.read_csv('rata.csv')

rata['Date']=pd.to_datetime(rata['Date'])
rata.sort_values('Date',inplace=True)

price_date=rata['Date']
close_date=rata['Close']
plt.plot(price_date,close_date,marker='o',linestyle='solid')

plt.gcf().autofmt_xdate()
plt.title('pictoin Prices')
plt.xlabel('Dates')
plt.ylabel('Close Dates')
plt.legend()
plt.tight_layout()
plt.show()