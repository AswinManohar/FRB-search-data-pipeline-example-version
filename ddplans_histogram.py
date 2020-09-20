import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def histogram(filename,name):
    ddplan=pd.read_csv(filename,header=None)
    x=ddplan[0]
    df=pd.DataFrame(x)
    df.columns=['plan']
    dftolist=df['plan'].tolist()
    dflist=list(df['plan'])
    counter=Counter(dflist)
    
#fd=pd.DataFrame.from_dict(counts,orient='index')
    pd.Series(dflist).value_counts().plot('bar')
    y=pd.Series(dflist).value_counts()
    ax=y.plot(kind='barh',figsize=(10,10),color='#86bf91',edgecolor=None,zorder=2)
    ax.set_xlabel("Number of Pointings", labelpad=20, weight='bold', size=12)
  # Set y-axis label
    ax.set_ylabel("observational configuration", labelpad=20, weight='bold', size=12)
    plt.savefig(name)
    plt.bar(y,width=0.5)
    plt.show()

    








ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_250','sample_250.png')

#ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_125','sample_125.png')
#ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_80','sample_80.png')
#ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_100','sample_100.png')
#ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_175','sample_175.png')

#ax=histogram('/hercules/u/aswin/database/interesting_plots/sample_500','sample_500.png')





#fd=pd.DataFrame.from_dict(counts,orient='index')
    #pd.Series(dflist).value_counts().plot('bar')
   # y=pd.Series(dflist).value_counts()
    #ax=y.plot(kind='barh',figsize=(10,10),color='#86bf91',edgecolor=None,zorder=2)
    #ax.set_xlabel("Number of Pointings", labelpad=20, weight='bold', size=12)
  # Set y-axis label
    #ax.set_ylabel("observational configuration", labelpad=20, weight='bold', size=12)
    #plt.savefig(name)
   # plt.bar(y,widh=.5)
   # plt.show()










