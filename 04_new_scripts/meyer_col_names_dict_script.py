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
  re.sub(r'(w[123])(q[0][4-9])$', r'\1_keyes-\2', v)
  for k, v in meyer_col_names.items()}

# Keyes, part 2: w123_q10-18
meyer_col_names = {k: 
  re.sub(r'(w[123])(q[1][0-8])$', r'\1_keyes-\2', v)
  for k, v in meyer_col_names.items()}

# composite Keyes
meyer_col_names = {k: 
  re.sub(r'(w[123])socialwb', r'\1_keyes', v)
  for k, v in meyer_col_names.items()}

# Satisfaction with life, part 1: w1_q186-189
meyer_col_names = {k: 
  re.sub(r'w1(q[1][8][6-9])', r'w1_life_sat-\1', v)
  for k, v in meyer_col_names.items()}

# Satisfaction with life, part 2: w1_q190
meyer_col_names = {k: 
  re.sub(r'w1(q[1][9][0])', r'w1_life_sat-\1', v)
  for k, v in meyer_col_names.items()}
  
# composite life sat
meyer_col_names = {k: 
  re.sub(r'(w[1])lifesat', r'\1_life_sat', v)
  for k, v in meyer_col_names.items()}

# MEIM-R: w1_q21-26
meyer_col_names = {k: 
  re.sub(r'w1(q[2][1-6])', r'w1_meim-\1', v)
  for k, v in meyer_col_names.items()}
  
# composite MEIM
meyer_col_names = {k: 
  re.sub(r'w1meim', r'w1_meim', v)
  for k, v in meyer_col_names.items()}

# Gay ID centrality, wave 1: w1_q40-44
meyer_col_names = {k: 
  re.sub(r'w1(q[4][0-4])', r'w1_gay_id_cent-\1', v)
  for k, v in meyer_col_names.items()}

# Gay ID centrality, wave 2 and 3: w2-3_q24-28
meyer_col_names = {k: 
  re.sub(r'(w[23])(q[2][4-8])', r'\1_gay_id_cent-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite Gay ID centrality
meyer_col_names = {k: 
  re.sub(r'(w[123])idcentral', r'\1_gay_id_cent', v)
  for k, v in meyer_col_names.items()}

# community connectedness, wave 1: w1_q53-59
meyer_col_names = {k: 
  re.sub(r'w1(q[5][3-9])', r'w1_comm_conn-\1', v)
  for k, v in meyer_col_names.items()}

# community connectedness, wave 2 and 3: w2-3_q30-36
meyer_col_names = {k: 
  re.sub(r'(w[23])(q[3][0-6])', r'\1_comm_conn-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite community connectedness
meyer_col_names = {k: 
  re.sub(r'(w[123])connectedness', r'\1_comm_conn', v)
  for k, v in meyer_col_names.items()}
  
# health care stereotype threat, w1q60-63
meyer_col_names = {k: 
  re.sub(r'w1(q[6][0-3])', r'w1_hc_threat-\1', v)
  for k, v in meyer_col_names.items()}

# composite health care stereotype threat
meyer_col_names = {k: 
  re.sub(r'w1_hcthreat', r'w1_hc_threat', v)
  for k, v in meyer_col_names.items()}
  
# kessler, wave 1: w1_q77a-77f
meyer_col_names = {k: 
  re.sub(r'w1(q[7][7])([a-f])', r'w1_kessler-\2', v)
  for k, v in meyer_col_names.items()}
  
# kessler, wave 2: w1_q84a-84f
meyer_col_names = {k: 
  re.sub(r'w2(q[8][4])([a-f])', r'w2_kessler-\2', v)
  for k, v in meyer_col_names.items()}

# kessler, wave 3: w1_q64a-64f
meyer_col_names = {k: 
  re.sub(r'w3(q[6][4])([a-f])', r'w3_kessler-\2', v)
  for k, v in meyer_col_names.items()}
  
# do another pass to add the a-f text
# STRAYS FROM THE PATTERN BCZ SECOND PASS!
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([a])', r'\1_kessler_nervous-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([b])', r'\1_kessler_hopeless-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([c])', r'\1_kessler_restless_fidgety-\2', v)
  for k, v in meyer_col_names.items()}

meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([d])', r'\1_kessler_so_depressed-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([e])', r'\1_kessler_everything_effort-\2', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_kessler-([f])', r'\1_kessler_worthless-\2', v)
  for k, v in meyer_col_names.items()}

# composite kessler
meyer_col_names = {k: 
  re.sub(r'(w[123])kessler6', r'\1_kessler', v)
  for k, v in meyer_col_names.items()}

# alcohol use, wave 1 & 2: w12_q85-87
meyer_col_names = {k: 
  re.sub(r'(w[12])(q[8][5-7])', r'\1_alcohol-\2', v)
  for k, v in meyer_col_names.items()}
  
# alcohol use, wave 3: w3_q65-67
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[6][5-7])', r'\1_alcohol-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite alochol use
meyer_col_names = {k: 
  re.sub(r'(w[123])auditc', r'\1_alcohol', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 1, part 1: w1_q90-99
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[9][0-9])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 1, part 2: w1_q100
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][0][0])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 2, part 1: w2_q89
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[8][9])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 2, part 2: w2_q90-99
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[9][0-9])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 3, part 1: w3_q70-79
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[7][0-9])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# drug use, wave 3, part 2: w3_q80
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[8][0])', r'\1_drugs-\2', v)
  for k, v in meyer_col_names.items()}

# composite drug use
meyer_col_names = {k: 
  re.sub(r'(w[1-3])dudit', r'\1_drugs', v)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 1: w1_q125-127
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][2][5-7])', r'\1_stigma-\2', v)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 2, part 1: w2_q108-109
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][0][8-9])', r'\1_stigma-\2', v)
  for k, v in meyer_col_names.items()}

# felt stigma, wave 2, part 2: w2_q110
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][0])', r'\1_stigma-\2', v)
  for k, v in meyer_col_names.items()}
  
# felt stigma, wave 3: w3_q90-92
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[9][0-2])', r'\1_stigma-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite felt stigma
meyer_col_names = {k: 
  re.sub(r'(w[1-3])feltstigma', r'\1_stigma', v)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 1, part 1: w1_q128-129
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][2][8-9])', r'\1_int_homo-\2', v)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 1, part 1: w1_q130-132
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][3][0-2])', r'\1_int_homo-\2', v)
  for k, v in meyer_col_names.items()}

# internalized homophobia, wave 2: w2_q111-115
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][1-5])', r'\1_int_homo-\2', v)
  for k, v in meyer_col_names.items()}
  
# internalized homophobia, wave 3: w1_q93-97
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[9][3-7])', r'\1_int_homo-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite internalized homophobia
meyer_col_names = {k: 
  re.sub(r'(w[123])internalized', r'\1_int_homo', v)
  for k, v in meyer_col_names.items()}
  
# bi stigma, wave 2 (only), part 1: w2_q117-119
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][1][7-9])', r'\1_bi_stigma-\2', v)
  for k, v in meyer_col_names.items()}

# bi stigma, wave 2 (only), part 2: w2_q120-121
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][2][0-1])', r'\1_bi_stigma-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite bi stigma
meyer_col_names = {k: 
  re.sub(r'(w[2])bistigma', r'\1_bostwick_bi_stigma', v)
  for k, v in meyer_col_names.items()}

# change them all to disc-q#a-i  
# everyday discrimination, wave 1: w1_q144A-I
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][4][4][a-i])', r'\1_disc-\2', v)
  for k, v in meyer_col_names.items()}

# everyday discrimination, wave 2: w2_q131A-I  
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][3][1][a-i])', r'\1_disc-\2', v)
  for k, v in meyer_col_names.items()}
  
# everyday discrimination, wave 3: w3_q126A-I  
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[1][2][6][a-i])', r'\1_disc-\2', v)
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
  re.sub(r'(w[123])everyday', r'\1_disc', v)
  for k, v in meyer_col_names.items()}
  
# chronic strains, wave 1: w1q146A-w1q146L
# a = taking on too much
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][a])', r'\1_chronic_strain_taking_on_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# b = don't have enough money to make ends meet
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][b])', r'\1_chronic_strain_money_not_ends_meet-\2', v)
  for k, v in meyer_col_names.items()}
  
# c = job often leaves you physically and emotionally tired
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][c])', r'\1_chronic_strain_job_phys_emo_tired-\2', v)
  for k, v in meyer_col_names.items()}

# d = looking for a job and can't find one you want
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][d])', r'\1_chronic_strain_cant_find_job_want-\2', v)
  for k, v in meyer_col_names.items()}

# e = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][e])', r'\1_chronic_strain_conflict_with_partner-\2', v)
  for k, v in meyer_col_names.items()}

# f = parents don't approve of your partner
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][f])', r'\1_chronic_strain_parents_dont_approve_partner-\2', v)
  for k, v in meyer_col_names.items()}

# g = alone too much
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][g])', r'\1_chronic_strain_alone_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# h = you wonder if you will ever find a partner or spouse
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][h])', r'\1_chronic_strain_wonder_ever_marry-\2', v)
  for k, v in meyer_col_names.items()}
  
# i = relationship with parents is strained or conflicted
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][i])', r'\1_chronic_strain_conflict_with_parents-\2', v)
  for k, v in meyer_col_names.items()}

# j = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][j])', r'\1_chronic_strain_loved_one_bad_phys_emo_health-\2', v)
  for k, v in meyer_col_names.items()}
  
# k = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][k])', r'\1_chronic_strain_want_kids_but_cant-\2', v)
  for k, v in meyer_col_names.items()}
  
# l = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[1])_disc-(q[1][4][6][l])', r'\1_chronic_strain_concerned_childs_behav_mood-\2', v)
  for k, v in meyer_col_names.items()}
  
# chronic strains, wave 2: w2q133A-w1q133L
# a = taking on too much
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][a])', r'\1_chronic_strain_taking_on_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# b = don't have enough money to make ends meet
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][b])', r'\1_chronic_strain_money_not_ends_meet-\2', v)
  for k, v in meyer_col_names.items()}
  
# c = job often leaves you physically and emotionally tired
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][c])', r'\1_chronic_strain_job_phys_emo_tired-\2', v)
  for k, v in meyer_col_names.items()}

# d = looking for a job and can't find one you want
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][d])', r'\1_chronic_strain_cant_find_job_want-\2', v)
  for k, v in meyer_col_names.items()}

# e = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][e])', r'\1_chronic_strain_conflict_with_partner-\2', v)
  for k, v in meyer_col_names.items()}

# f = parents don't approve of your partner
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][f])', r'\1_chronic_strain_parents_dont_approve_partner-\2', v)
  for k, v in meyer_col_names.items()}

# g = alone too much
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][g])', r'\1_chronic_strain_alone_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# h = you wonder if you will ever find a partner or spouse
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][h])', r'\1_chronic_strain_wonder_ever_marry-\2', v)
  for k, v in meyer_col_names.items()}
  
# i = relationship with parents is strained or conflicted
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][i])', r'\1_chronic_strain_conflict_with_parents-\2', v)
  for k, v in meyer_col_names.items()}

# j = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][j])', r'\1_chronic_strain_loved_one_bad_phys_emo_health-\2', v)
  for k, v in meyer_col_names.items()}
  
# k = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][k])', r'\1_chronic_strain_want_kids_but_cant-\2', v)
  for k, v in meyer_col_names.items()}
  
# l = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[2])_disc-(q[1][3][3][l])', r'\1_chronic_strain_concerned_childs_behav_mood-\2', v)
  for k, v in meyer_col_names.items()}
  
# chronic strains, wave 2: w2q128A-w1q128L
# a = taking on too much
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][a])', r'\1_chronic_strain_taking_on_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# b = don't have enough money to make ends meet
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][b])', r'\1_chronic_strain_money_not_ends_meet-\2', v)
  for k, v in meyer_col_names.items()}
  
# c = job often leaves you physically and emotionally tired
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][c])', r'\1_chronic_strain_job_phys_emo_tired-\2', v)
  for k, v in meyer_col_names.items()}

# d = looking for a job and can't find one you want
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][d])', r'\1_chronic_strain_cant_find_job_want-\2', v)
  for k, v in meyer_col_names.items()}

# e = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][e])', r'\1_chronic_strain_conflict_with_partner-\2', v)
  for k, v in meyer_col_names.items()}

# f = parents don't approve of your partner
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][f])', r'\1_chronic_strain_parents_dont_approve_partner-\2', v)
  for k, v in meyer_col_names.items()}

# g = alone too much
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][g])', r'\1_chronic_strain_alone_too_much-\2', v)
  for k, v in meyer_col_names.items()}
  
# h = you wonder if you will ever find a partner or spouse
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][h])', r'\1_chronic_strain_wonder_ever_marry-\2', v)
  for k, v in meyer_col_names.items()}
  
# i = relationship with parents is strained or conflicted
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][i])', r'\1_chronic_strain_conflict_with_parents-\2', v)
  for k, v in meyer_col_names.items()}

# j = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][j])', r'\1_chronic_strain_loved_one_bad_phys_emo_health-\2', v)
  for k, v in meyer_col_names.items()}
  
# k = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][k])', r'\1_chronic_strain_want_kids_but_cant-\2', v)
  for k, v in meyer_col_names.items()}
  
# l = You have a lot of conflict with your partner/boyfriend/girlfriend.
meyer_col_names = {k: 
  re.sub(r'(w[3])_disc-(q[1][2][8][l])', r'\1_chronic_strain_concerned_childs_behav_mood-\2', v)
  for k, v in meyer_col_names.items()}
  

# childhood gender conformity

# childhood gender conformity, wave 1 (only), part 1: w1_q147-149
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][4][7-9])', r'\1_child_gnc-\2', v)
  for k, v in meyer_col_names.items()}
  
# childhood gender conformity, wave 1 (only), part 1: w1_q150
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][5][0])', r'\1_child_gnc-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite childhood gender conformity
meyer_col_names = {k: 
  re.sub(r'(w[1])childgnc', r'\1_child_gnc', v)
  for k, v in meyer_col_names.items()}
  

# adverse childhood experiences (ace)

# ace, wave 1 (only), part 1: w1_q151-159
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][5][1-9])', r'\1_ace_raw-\2', v)
  for k, v in meyer_col_names.items()}

# ace, wave 1 (only), part 2: w1_q160-161
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][6][0-1])', r'\1_ace_raw-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite ace, subscales and total (1st pass)
meyer_col_names = {k: 
  re.sub(r'(w[1])ace', r'\1_ace', v)
  for k, v in meyer_col_names.items()}

# 2nd pass -- should catch raw and _i
# emotional abuse
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_emo', r'\1_ace_emo_abuse', v)
  for k, v in meyer_col_names.items()}
  
# physical abuse
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_phy', r'\1_ace_phys_abuse', v)
  for k, v in meyer_col_names.items()}

# sexual abuse
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_sex', r'\1_ace_sex_abuse', v)
  for k, v in meyer_col_names.items()}
  
# ipv -- fine as is

# substance use
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_sub', r'\1_ace_sub_use', v)
  for k, v in meyer_col_names.items()}

# mental illness
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_men', r'\1_ace_ment_ill', v)
  for k, v in meyer_col_names.items()}

# parental separation or divorce
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_sep', r'\1_ace_parent_sep', v)
  for k, v in meyer_col_names.items()}
  
# incarcerated household member
meyer_col_names = {k: 
  re.sub(r'(w[1])_ace_inc', r'\1_ace_fam_jail', v)
  for k, v in meyer_col_names.items()}


# social support, pass 1, wave 1: w1q164a-l
meyer_col_names = {k: 
  re.sub(r'(w[1])(q[1][6][4][a-l])', r'\1_soc_supp-\2', v)
  for k, v in meyer_col_names.items()}

# social support, pass 1, wave 2: w2q135a-l
meyer_col_names = {k: 
  re.sub(r'(w[2])(q[1][3][5][a-l])', r'\1_soc_supp-\2', v)
  for k, v in meyer_col_names.items()}
  
# social support, pass 1, wave 3: w3q129a-l
meyer_col_names = {k: 
  re.sub(r'(w[3])(q[1][2][9][a-l])', r'\1_soc_supp-\2', v)
  for k, v in meyer_col_names.items()}
  
# social support, pass 2: a-l
# a = There is a special person who is around when I am in need.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][a])', r'\1_soc_supp_special_person_im_in_need-\2', v)
  for k, v in meyer_col_names.items()}

# b = There is a special person with whom I can share my joys and sorrows.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][b])', r'\1_soc_supp_special_person_share_feelings-\2', v)
  for k, v in meyer_col_names.items()}
  
# c = My family really tries to help me.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][c])', r'\1_soc_supp_special_fam_tries_help-\2', v)
  for k, v in meyer_col_names.items()}

# d = I get the emotional help and support I need from my family.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][d])', r'\1_soc_supp_get_emo_supp_fam-\2', v)
  for k, v in meyer_col_names.items()}

# e = I have a special person who is a real source of comfort to me.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][e])', r'\1_soc_supp_special_person_comfort-\2', v)
  for k, v in meyer_col_names.items()}

# f = My friends really try to help me.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][f])', r'\1_soc_supp_friends_try_help-\2', v)
  for k, v in meyer_col_names.items()}

# g = I can count on my friends when things go wrong.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][g])', r'\1_soc_supp_count_on_friends-\2', v)
  for k, v in meyer_col_names.items()}

# h = I can talk about my problems with my family.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][h])', r'\1_soc_supp_fam_talk_problems-\2', v)
  for k, v in meyer_col_names.items()}

# i = I have friends with whom I can share my joys and sorrows.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][i])', r'\1_soc_supp_friends_share_feelings-\2', v)
  for k, v in meyer_col_names.items()}

# j = There is a special person in my life who cares about my feelings.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][j])', r'\1_soc_supp_special_person_cares_feelings-\2', v)
  for k, v in meyer_col_names.items()}

# k = My family is willing to help me make decisions.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][k])', r'\1_soc_supp_fam_help_decisions-\2', v)
  for k, v in meyer_col_names.items()}

# l = I can talk about my problems with my friends.
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp-(q[1][236][459][l])', r'\1_soc_supp_friends_talk_problems-\2', v)
  for k, v in meyer_col_names.items()}
  
# composite social support, 1st pass
meyer_col_names = {k: 
  re.sub(r'(w[123])socsupport', r'\1_soc_supp', v)
  for k, v in meyer_col_names.items()}
  
# composite social support, 2nd pass
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp_fr$', r'\1_soc_supp_from_friends', v)
  for k, v in meyer_col_names.items()}

# list the i separately because I have to anchor fr$ 
# if I don't anchor it, it catches on all the 'friends' ones
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp_fr_i$', r'\1_soc_supp_from_friends_i', v)
  for k, v in meyer_col_names.items()}
  
# same for fam
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp_fam$', r'\1_soc_supp_from_fam', v)
  for k, v in meyer_col_names.items()}
  
meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp_fam_i$', r'\1_soc_supp_from_fam_i', v)
  for k, v in meyer_col_names.items()}

meyer_col_names = {k: 
  re.sub(r'(w[123])_soc_supp_so', r'\1_soc_supp_from_sig_other', v)
  for k, v in meyer_col_names.items()}





# THIS is the pdf that I'm working through with the variable names:
# file:///C:/Users/emily/Git_Stuff/General_Assembly/04_Projects/project-capstone/potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/37166-Documentation-methodology.pdf
# and look at the documentation crosswalk (in original folder) to cross ref between waves
# October 30th: I'm up to "social support matrix questions," page 31/88




# see it pretty
print(json.dumps(meyer_col_names, indent = 2))
  

# Display the n per wave; note that 3 = waves 1 and 2, but not wave 3, & 4 = all 3 waves
# meyer['waveparticipated'].value_counts(dropna = False).sort_index()





