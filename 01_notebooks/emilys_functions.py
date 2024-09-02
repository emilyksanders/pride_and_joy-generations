# Imports
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date, time
from string import capwords
import statsmodels.api as sm

# Define my_date()
def my_date():
  return datetime.now().strftime('%Y-%m-%d_h%H-m%M-s%S')
my_date()

# Define autoplots()
def autoplots(d, y, qqplots = True, transform = False, line = False, verbose = True, folder = 'images'):
  '''a function to make a ton of graphs.
  Each plot is based on a subset of d where all variables in the
  plot have no null values.  The size of this subset (n) is 
  displayed in the subtitle of the plot, and can be used 
  similarly to d.isnull().sum(), if desired.
  
  args:
    d: dataframe, the dataframe of the information.
    
    y: string, the name of the column within the dataframe that is the target.
    
    qqplots: bool, whether to generate qqplots for each variable. Default = True.
    
    transform: bool, whether to generate qqplots of transformed versions 
      of each variable. Only used when `qqplots = True`, otherwise ignored. 
      Default = False. Included transformations are (x+z)**(1/2), (x+z)**(1/3), 
      and log(x+z+1), where z=abs(x.min()) if x.min()<0, else z=0.
    
    line: bool, whether to plot line graphs. Default = False.
    
    verbose: bool, whether to print updates while running. Default = True.

    folder: string, the name of the folder in which to save the plots.  Default = 'images'.
  
  return:
    a ton of plots in a FOLDER
  
  raise:
    pls no'''
  
  # Need these
  import os
  from string import capwords
  import matplotlib.pyplot as plt
  import seaborn as sns
  import statsmodels.api as sm
  import numpy as np
  import pandas as pd
  
  # Make a folder 
  try: 
    os.mkdir(folder)
  except:
    pass
  a = f'{folder}/plots_{my_date()}'
  os.mkdir(a)
  
  # Define these once
  n_grand = len(d[y])
  if verbose==True: print(n_grand)
  # in future versions, I'd like to raise a warning
  # if len(d[y])!=len(d[d[y].notna()])    
  # (i.e., if there are nulls in the target)
  n_features = d.shape[1]
  
  # Give y a good(ish) name
  ty = capwords(y.replace('_', ' '))
  if verbose==True: print(ty)
  
  # Plot the distributions of all variables
  for i in d.columns:
    if verbose==True: print(i)
    # Give it a good(ish) name
    t = capwords(i.replace('_', ' '))
    if verbose==True: print(t)
    
    # Extract the subset dataframe, drop NAs, get n
    df = d[i]
    if verbose==True: print(df.shape)
    df.dropna(inplace = True)
    n = len(df)
    
    # Plot a histogram of it
    plt.figure(figsize = (16, 9));
    plt.hist(df, bins = 'auto', color = 'purple');
    plt.suptitle(f'Distribution of {t}', size = 24)
    plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
    plt.xlabel(f'{t}', size = 20);
    plt.ylabel('Frequency', size = 20);
    plt.xticks(size = 16, rotation = 60);
    plt.yticks(size = 16);
    # plt.tight_layout()
    plt.savefig(f'./{a}/{i}_histogram.png');
    plt.close();
    
    # Plot a boxplot of it
    plt.figure(figsize = (16, 9))
    sns.boxplot(data = df, color = 'purple', orient = 'h')
    plt.suptitle(f'Distribution of {t}', size = 24)
    plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
    plt.xlabel(f'{t}', size = 20);
    plt.xticks(size = 16, rotation = 60);
    # plt.tight_layout()
    plt.savefig(f'./{a}/{i}_boxplot.png');
    plt.close();
    
    # Plot (a) qqplot(s) of it, if indicated
    if qqplots==True:
      
      # Raw data
      plt.figure(figsize = (9, 9));
      sm.qqplot(data = df, line='45', markerfacecolor = 'purple', 
        markeredgecolor = 'purple', alpha = 0.5);
      plt.suptitle(f'QQ-Plot of {t}', size = 24);
      plt.title(f'Based on {n} Observations out of {n_grand}', size = 18);
      plt.xticks(size = 16, rotation = 60);
      plt.yticks(size = 16);
      # plt.tight_layout();
      plt.savefig(f'./{a}/{i}_qqplot.png');
      plt.close();
      
      # Plot transformations, if indicated
      if transform == True:
        
        # Calculate z
        if df.min()<0:
          z=abs(df.min())
        else: 
          z=0
        
        # Square root
        plt.figure(figsize = (9, 9));
        sm.qqplot(data = ((df+z)**(1/2)), line='45', alpha = 0.5, 
          markerfacecolor = 'purple', markeredgecolor = 'purple');
        plt.suptitle(f'QQ-Plot of Square Root of {t}-Plus-{z}', size = 24);
        plt.title(f'Based on {n} Observations out of {n_grand}', size = 18);
        plt.xticks(size = 16, rotation = 60);
        plt.yticks(size = 16);
        # plt.tight_layout();
        plt.savefig(f'./{a}/{i}_qqplot_2nd_root.png');
        plt.close();
        
        # Cube root
        plt.figure(figsize = (9, 9));
        sm.qqplot(data = ((df+z)**(1/3)), line='45', alpha = 0.5, 
          markerfacecolor = 'purple', markeredgecolor = 'purple');
        plt.suptitle(f'QQ-Plot of Cube Root of {t}-Plus-{z}', size = 24);
        plt.title(f'Based on {n} Observations out of {n_grand}', size = 18);
        plt.xticks(size = 16, rotation = 60);
        plt.yticks(size = 16);
        # plt.tight_layout();
        plt.savefig(f'./{a}/{i}_qqplot_3rd_root.png');
        plt.close();
        
        # Log... ish
        plt.figure(figsize = (9, 9));
        sm.qqplot(data = np.log(df+z+1), line='45', alpha = 0.5, 
          markerfacecolor = 'purple', markeredgecolor = 'purple');
        plt.suptitle(f'QQ-Plot of Log of {t}-Plus-{z+1}', size = 24);
        plt.title(f'Based on {n} Observations out of {n_grand}', size = 18);
        plt.xticks(size = 16, rotation = 60);
        plt.yticks(size = 16);
        # plt.tight_layout();
        plt.savefig(f'./{a}/{i}_qqplot_log.png');
        plt.close();
    
  # Drop y from the list
  X = [col for col in list(d.drop(columns = [y]).columns)]
  
  # Make plots of each x against y
  for i in X:
    # Give it a good(ish) name
    t = capwords(i.replace('_', ' '))
    if verbose==True: print(t)
    
    # Extract the subset dataframe, drop NAs, get n
    df = d[[i, y]]
    df.dropna(inplace = True)
    n = len(df[y])
    
    # Plot a scatterplot of it against y
    plt.figure(figsize = (16, 9))
    plt.scatter(df[i], df[y], alpha = 0.5, color = 'purple')
    plt.suptitle(f'Relationship between {t} and {ty}', size = 24)
    plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
    plt.xlabel(f'{t}', size = 20);
    plt.ylabel(f'{ty}', size = 20);
    plt.xticks(size = 16, rotation = 60)
    plt.yticks(size = 16);
    # plt.tight_layout()
    plt.savefig(f'./{a}/{i}-by-{y}_scatterplot.png');
    plt.close();
    
    # Plot a line plot of it against y
    if line==True:
      plt.figure(figsize = (16, 9))
      plt.plot(i, y, data = df, color = 'purple')
      plt.suptitle(f'Relationship between {t} and {ty}', size = 24)
      plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
      plt.xlabel(f'{t}', size = 20);
      plt.ylabel(f'{ty}', size = 20);
      plt.xticks(size = 16, rotation = 60)
      plt.yticks(size = 16);
      # plt.tight_layout()
      plt.savefig(f'./{a}/{i}-by-{y}_lineplot.png');
      plt.close();
    
  # All together now
  n = len(d[y])
  
  # Plot a line plot of everything against y
  if line==True:
    plt.figure(figsize = (16, 9))
    for i in X:
      if verbose==True: print(i)
      plt.plot(i, y, data = d)
    plt.suptitle(f'Relationship between Predictors and {ty}', size = 24)
    plt.title(f'Based on {n_grand} Observations out of {n_grand}', size = 18)
    plt.xlabel(f'{t}', size = 20);
    plt.ylabel(f'{ty}', size = 20);
    plt.xticks(size = 16, rotation = 60)
    plt.yticks(size = 16);
    plt.legend();
    # plt.tight_layout()
    plt.savefig(f'./{a}/all-by-{y}_lineplot.png');
    plt.close();
  
  # Get some correlations
  corr = round(d.corr(numeric_only = True), 2)
  
  # Plot a heatmap
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True
  quarter_features = np.round((n_features/4), 0)
  plt.figure(figsize = (quarter_features, quarter_features))
  sns.heatmap(corr, square = True, 
    annot = True, cmap = 'coolwarm', mask = mask);
  plt.suptitle(f'Relationships Between Variables', size = 24)
  plt.title(f'Based on {n_grand} Observations out of {n_grand}', size = 18);
  # plt.tight_layout()
  plt.savefig(f'./{a}/all_heatmap.png');
  plt.close();
  
  # Plot a heatmap column on y
  if y in corr:
    plt.figure(figsize = (16, 9))
    sns.heatmap(np.asarray([corr[y].sort_values(ascending = False)]).T, 
      vmin = 0, vmax = 1, annot = True, cmap = 'coolwarm')
    plt.suptitle(f'Relationship between Predictors and {ty}', size = 24)
    plt.title(f'Based on {n_grand} Observations out of {n_grand}', size = 18)
    plt.xlabel(f'{ty}', size = 20);
    plt.yticklabels = True
    # plt.tight_layout()
    plt.savefig(f'./{a}/all-by-{y}_heatmap.png');
    plt.close();
