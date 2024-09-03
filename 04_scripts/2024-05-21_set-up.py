# Capstone Setup

# Module Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
from datetime import datetime, date, time
from string import capwords

# Working Directory
os.getcwd()
os.chdir('C:/Users/emily/Git_Stuff/General_Assembly/04_Projects/project-capstone')
os.listdir()

# Import Data
# (This will likely change as my dataset choice changes!)
df = pd.read_csv(
  './potential_datasets/2024-05-21_download_SAMHSA_NSDUH-2019-DS0001/NSDUH_2019_Tab.txt', 
  sep = '\t', low_memory=False)

# This thing has 2741 columns!  
# I'm going to pair it down by printing out the column names, 
# copying them to a text file, and then
# going through the codebook to see which ones I really need.

#print(list(df.columns))
# commented out bcz omg.




