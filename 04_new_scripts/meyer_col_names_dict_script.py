# Clean script copied from Jupyter

# Import modules
import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
from warnings import simplefilter
import json
import re

# Settings preferences
pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None 
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
# Thanks to daydaybroskii and KingOtto at Stack Overflow for that one

# Import the data
# chunk up a long url
path1 = '../../General_Assembly/04_Projects/project-capstone/potential_datasets/'
path2 = '2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/'
file = 'ICPSR_37166/DS0007/37166-0007-Data.tsv'

# Read it
meyer = pd.read_csv(path1+path2+file, 
  sep = '\t', low_memory=False, na_values = ' ')
# Many thanks to ibrahim rupawala for highlighting the na_values argument

# Check it
meyer.shape
meyer.info()

# Rename the columns

# first make all lower caser
meyer.columns = [c.lower() for c in list(meyer.columns)]

# create a dictionary of old to new names
meyer_col_names = {i: i for i in list(meyer.columns)}

# make broad fixes
# backreferencing! : https://stackoverflow.com/questions/14458160/while-replacing-using-regex-how-to-keep-a-part-of-matched-string
# meyer_col_names = {k: re.sub(r'w([123])', r'w\1_', k) for k, v in meyer_col_names.items()}

# Keyes, part 1: w123_q04-09
meyer_col_names = {k: 
  re.sub(r'(w[123])(q[0][4-9])$', r'\1_keyes-\2', k)
  for k, v in meyer_col_names.items()}

# Keyes, part 2: w123_q10-18
meyer_col_names = {k: 
  re.sub(r'(w[123])(q[1][0-8])$', r'\1_keyes-\2', k)
  for k, v in meyer_col_names.items()}

# composite Keyes
meyer_col_names = {k: 
  re.sub(r'(w[123])socialwb', r'\1_keyes_composite', k)
  for k, v in meyer_col_names.items()}

# Satisfaction with life, part 1: w1_q186-189
meyer_col_names = {k: 
  re.sub(r'w1(q[1][8][6-9])', r'w1_life_sat-\1', k)
  for k, v in meyer_col_names.items()}

# Satisfaction with life, part 2: w1_q190
meyer_col_names = {k: 
  re.sub(r'w1(q[1][9][0])', r'w1_life_sat-\1', k)
  for k, v in meyer_col_names.items()}
  
# composite life sat
meyer_col_names = {k: 
  re.sub(r'(w[1])lifesat', r'\1_life_sat', k)
  for k, v in meyer_col_names.items()}

# MEIM-R: w1_q21-26
meyer_col_names = {k: 
  re.sub(r'w1(q[2][1-6])', r'w1_meim-\1', k)
  for k, v in meyer_col_names.items()}
  
# composite MEIM
meyer_col_names = {k: 
  re.sub(r'w1meim', r'w1_meim', k)
  for k, v in meyer_col_names.items()}

# Gay ID centrality, wave 1: w1_q40-44
meyer_col_names = {k: 
  re.sub(r'w1(q[4][0-4])', r'w1_gay_id_cent-\1', k)
  for k, v in meyer_col_names.items()}

# Gay ID centrality, wave 2 and 3: w2-3_q24-28
meyer_col_names = {k: 
  re.sub(r'(w[23])(q[2][4-8])', r'\1_gay_id_cent-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite Gay ID centrality
meyer_col_names = {k: 
  re.sub(r'(w[123])idcentral', r'\1_gay_id_cent', k)
  for k, v in meyer_col_names.items()}

# community connectedness, wave 1: w1_q53-59
meyer_col_names = {k: 
  re.sub(r'w1(q[5][3-9])', r'w1_comm_conn-\1', k)
  for k, v in meyer_col_names.items()}

# community connectedness, wave 2 and 3: w2-3_q30-36
meyer_col_names = {k: 
  re.sub(r'(w[23])(q[3][0-6])', r'\1_comm_conn-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite community connectedness
meyer_col_names = {k: 
  re.sub(r'(w[123])connectedness', r'\1_comm_conn', k)
  for k, v in meyer_col_names.items()}
  
# health care stereotype threat, w1q60-63
meyer_col_names = {k: 
  re.sub(r'w1(q[6][0-3])', r'w1_hc_threat-\1', k)
  for k, v in meyer_col_names.items()}

# composite health care stereotype threat
meyer_col_names = {k: 
  re.sub(r'w1_hcthreat', r'w1_hc_threat', k)
  for k, v in meyer_col_names.items()}
  
# kessler, wave 1: w1_q77a-77f
meyer_col_names = {k: 
  re.sub(r'w1(q[7][7])([a-f])', r'w1_kessler-\2', k)
  for k, v in meyer_col_names.items()}
  
# kessler, wave 2: w1_q84a-84f
meyer_col_names = {k: 
  re.sub(r'w2(q[8][4])([a-f])', r'w2_kessler-\2', k)
  for k, v in meyer_col_names.items()}

# kessler, wave 3: w1_q64a-64f
meyer_col_names = {k: 
  re.sub(r'w3(q[6][4])([a-f])', r'w3_kessler-\2', k)
  for k, v in meyer_col_names.items()}
  
# do another pass to add the a-f text
# STRAYS FROM THE PATTERN BCZ SECOND PASS!
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][a])', r'w1_kessler_nervous-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][b])', r'w1_kessler_hopeless-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][c])', r'w1_kessler_restless_fidgety-\2', v)
  for k, v in meyer_col_names.items()}

meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][d])', r'w1_kessler_so_depressed-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][e])', r'w1_kessler_everything_effort-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-(q[6-8][4-7][f])', r'w1_kessler_worthless-\2', v)
  for k, v in meyer_col_names.items()}

# composite kessler
meyer_col_names = {k: 
  re.sub(r'(w[123])kessler6', r'\1_kessler', k)
  for k, v in meyer_col_names.items()}

# alcohol use, wave 1 & 2: w12_q85-87
meyer_col_names = {k: 
  re.sub(r'(w[12])(q[8][5-7])', r'\1_alcohol-\2', k)
  for k, v in meyer_col_names.items()}
  
# alcohol use, wave 3: w3_q65-67
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[6][5-7])', r'\1_alcohol-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite alochol use
meyer_col_names = {k: 
  re.sub(r'(w[123])auditc', r'\1_alcohol', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 1, part 1: w1_q90-99
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[9][0-9])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 1, part 2: w1_q100
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][0][0])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 2, part 1: w2_q89
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[8][9])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 2, part 2: w2_q90-99
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[9][0-9])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 3, part 1: w3_q70-79
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[7][0-9])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# drug use, wave 3, part 2: w3_q80
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[8][0])', r'\1_drugs-\2', k)
  for k, v in meyer_col_names.items()}

# composite drug use
meyer_col_names = {k: 
  re.sub(r'(w[1-3])dudit', r'\1_drugs', k)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 1: w1_q125-127
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][2][5-7])', r'\1_stigma-\2', k)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 2, part 1: w2_q108-109
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][0][8-9])', r'\1_stigma-\2', k)
  for k, v in meyer_col_names.items()}

# felt stigma, wave 2, part 2: w2_q110
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][0])', r'\1_stigma-\2', k)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 3: w3_q90-92
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[9][0-2])', r'\1_stigma-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite felt stigma
meyer_col_names = {k: 
  re.sub(r'(w[1-3])feltstigma', r'\1_stigma', k)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 1, part 1: w1_q128-129
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][2][8-9])', r'\1_int_homo-\2', k)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 1, part 1: w1_q130-132
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][3][0-2])', r'\1_int_homo-\2', k)
  for k, v in meyer_col_names.items()}

# internalized homophobia, wave 2: w2_q111-115
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][1-5])', r'\1_int_homo-\2', k)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 3: w1_q93-97
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[9][3-7])', r'\1_int_homo-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite internalized homophobia
meyer_col_names = {k: 
  re.sub(r'(w[123])internalized', r'\1_int_homo', k)
  for k, v in meyer_col_names.items()}
  
# bi stigma, wave 2 (only), part 1: w2_q117-119
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][7-9])', r'\1_bi_stigma-\2', k)
  for k, v in meyer_col_names.items()}

# bi stigma, wave 2 (only), part 2: w2_q120-121
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][2][0-1])', r'\1_bi_stigma-\2', k)
  for k, v in meyer_col_names.items()}
  
# composite bi stigma
meyer_col_names = {k: 
  re.sub(r'(w[2])bistigma', r'\1_bostwick_bi_stigma', k)
  for k, v in meyer_col_names.items()}

# change them all to disc-q#a-i  
# everyday discrimination, wave 1: w1_q144A-I
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][4][4][a-i])', r'\1_disc-\2', k)
  for k, v in meyer_col_names.items()}

# everyday discrimination, wave 2: w2_q131A-I  
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][3][1][a-i])', r'\1_disc-\2', k)
  for k, v in meyer_col_names.items()}
  
# everyday discrimination, wave 3: w3_q126A-I  
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[1][2][6][a-i])', r'\1_disc-\2', k)
  for k, v in meyer_col_names.items()}

# change all disc-___a, b, c, etc. to their values
# THESE STRAY FROM THE PATTERN BECAUSE IT'S A SECOND PASS ON THE SAME ENTRIES
# I added the underscore in the pattern to look for, and have it look in the v
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][a])', r'\1_disc_less_courtesy-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][b])', r'\1_disc_less_respect-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][c])', r'\1_disc_poorer_service-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][d])', r'\1_disc_thought_not_smart-\2', v)
  for k, v in meyer_col_names.items()}

meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][e])', r'\1_disc_acted_afraid-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][f])', r'\1_disc_thought_dishonest-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][g])', r'\1_disc_acted_better_you-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][h])', r'\1_disc_called_names_insulted-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_disc-(q[1][2-4][1-6][i])', r'\1_disc_threatened_harassed-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite everyday discrimination
meyer_col_names = {k: 
  re.sub(r'(w[123])everyday', r'\1_disc', k)
  for k, v in meyer_col_names.items()}

# THIS is the pdf that I'm working through with the variable names:
# file:///C:/Users/emily/Git_Stuff/General_Assembly/04_Projects/project-capstone/potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/37166-Documentation-methodology.pdf
# and look at the documentation crosswalk (in original folder) to cross ref between waves




# see it pretty
print(json.dumps(meyer_col_names, indent = 2))
  

# Display the n per wave; note that 3 = waves 1 and 2, but not wave 3, & 4 = all 3 waves
meyer['waveparticipated'].value_counts(dropna = False).sort_index()




