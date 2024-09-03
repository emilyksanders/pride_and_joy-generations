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
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Working Directory
os.getcwd()
#os.chdir('C:/Users/emily/Git_Stuff/General_Assembly/04_Projects/project-capstone')
os.listdir()

# Set these right off the bat
pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None 

# Import Data

# THIS IS THE ORIGINAL
# meyer = pd.read_csv(
#   './potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', 
#   sep = '\t', low_memory=False, na_values = ' ') # Thanks to ibrahim rupawala for highlighting the na_values argument
#   # https://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas/47105408#47105408

# THIS IS THE MOST UP TO DATE VERSION FOR WORKING ON
meyer = pd.read_csv('2024-06-06_recodes-for-feat-eng-dict-done_religious-ohe-done_reordered.csv')
meyer.shape

