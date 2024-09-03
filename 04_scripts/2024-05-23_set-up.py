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
#os.chdir('C:/Users/emily/Git_Stuff/General_Assembly/04_Projects/project-capstone')
os.listdir()

# Import Data
meyer = pd.read_csv('./potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', sep = '\t', low_memory=False)



