# Composite Scale Calculations

# In this script, I need to go back to `feat_eng_dict`, that list I made in 
# `2024-05-23_thru_2024-05-30_exploring_Meyer_2023_dataset.py`, and use it to 
# combine some of these columns into composite columns and drop the rest.

unaltered_col_names = [
  c.replace('_r', '').replace('_ei', '') for c in list(meyer.columns)]
  
for k, v in feat_eng_dict.items():
  a = v[1:]
  for j in a:
    if ((j not in unaltered_col_names) & (j not in list(meyer.columns))):
      print(k, j)

# redefine it here without those
feat_eng_dict = {'pers_well_being': ['sum', 'w1q01'],
  'neighb_welcoming': ['mean', 'w1q19a', 'w1q19b', 'w1q19c', 'w1q19d'],
  'age_awakening': ['min','w1q45', 'w1q46', 'w1q47', 'w1q48'],
  'age_out': ['min', 'w1q49', 'w1q50', 'w1q51'],
  'health_insurance': ['binarize', 'w1q64_1', 'w1q64_2', 'w1q64_3', 'w1q64_4', 
    'w1q64_5', 'w1q64_6', 'w1q64_7', 'w1q64_8', 'w1q64_9', 'w1q64_10', 
    'w1q64_11', 'w1q64_12', 'w1q64_13', 'w1q64_t_num'], 
  'serious_health_cond': ['binarize', 'w1q74_5', 'w1q74_6', 'w1q74_10', 
    'w1q74_11', 'w1q74_14', 'w1q74_17', 'w1q74_18', 'w1q74_20'], 
  'disabled': ['binarize', 'w1q75', 'w1q76'],
  'suicidal_ideation': ['sum', 'w1q101', 'w1q105', 'w1q109'], 
  'suicide_attempts': ['recode', 'w1q113', 'w1q114'],
  'outness': ['sum', 'w1q123a', 'w1q123b', 'w1q123c', 'w1q123d', 'w1q124'],
  'abusive_treatment': ['sum', 'w1q135a', 'w1q135b', 
    'w1q135c', 'w1q135d', 'w1q135e', 'w1q135f'],
  'work_neg_outcomes': ['recode', 'w1q137', 'w1q138'], # account for age
  'abus_treat_non_queer': ['binarize', 'w1q136_1', 'w1q136_5', 'w1q136_6', 
    'w1q136_8', 'w1q136_9', 'w1q136_10'],
  'stress_past_year_gen': ['recode', 'w1q142a', 'w1q142h', 'w1q142i'],
  'stress_past_year_work': ['recode', 'w1q142b', 'w1q142c', 'w1q142e'],
  'stress_past_year_interpersonal': ['recode', 'w1q142d', 'w1q142f', 'w1q142g'],
  'stress_past_year_crime': ['recode', 'w1q142j', 'w1q142k'],
  'work_disc_non_queer': ['binarize', 'w1q139_1', 'w1q139_5', 'w1q139_6', 
    'w1q139_8', 'w1q139_9', 'w1q139_10'],
  'housing_disc_non_queer': ['binarize', 'w1q141_1', 'w1q141_5', 'w1q141_6', 
    'w1q141_8', 'w1q141_9', 'w1q141_10'],
  'stress_past_year_non_queer': ['binarize', 'w1q143_1', 'w1q143_5', 'w1q143_6', 
    'w1q143_8', 'w1q143_9', 'w1q143_10'],
  'daily_discr_non_queer': ['binarize', 'w1q145_1', 'w1q145_5', 'w1q145_6'],
  'childhd_bullying_non_queer': ['binarize', 'w1q163_1', 'w1q163_5', 'w1q163_6', 
    'w1q163_8', 'w1q163_9', 'w1q163_10'],
  'abus_treat_sex_gender': ['binarize', 'w1q136_2', 'w1q136_3', 'w1q136_4'],
  'work_disc_sex_gender': ['binarize', 'w1q139_2', 'w1q139_3', 'w1q139_4'],
  'housing_disc_sex_gender': ['binarize', 'w1q141_2', 'w1q141_3', 'w1q141_4'],
  'stress_past_year_sex_gender': ['binarize', 'w1q143_2', 'w1q143_3', 'w1q143_4'],
  'daily_discr_sex_gender': ['binarize', 'w1q145_2', 'w1q145_3', 'w1q145_4', 
    'w1q145_8', 'w1q145_9', 'w1q145_10'],
  'childhd_bullying_sex_gender': ['binarize', 'w1q163_2', 'w1q163_3', 'w1q163_4'],
  'religiosity': ['recode', 'w1q179', 'w1q180', 'w1q181'], 
  'chronic_strain': ['sum', 'w1q146a', 'w1q146b', 'w1q146c', 'w1q146d', 'w1q146e', 
    'w1q146f', 'w1q146g', 'w1q146h', 'w1q146i', 'w1q146j', 'w1q146k', 'w1q146l']}

# then go back up and check again
# got them all!

# Now I'm going to go through and find which ones have NOT been altered
for k, v in feat_eng_dict.items():
  a = v[1:]
  for j in a:
    if j in list(meyer.columns):
      print(k, j)

# oh dear just one
for k, v in feat_eng_dict.items():
  a = v[:1]
  b = ['_'.join([x, 'ei']) for x in v[1:]]
  c = a + b
  feat_eng_dict[k] = c
  
# manually fix this one
feat_eng_dict['health_insurance'] = ['binarize', 'w1q64_1_ei', 
  'w1q64_2_ei', 'w1q64_3_ei', 'w1q64_4_ei', 'w1q64_5_ei', 'w1q64_6_ei', 
  'w1q64_7_ei', 'w1q64_8_ei', 'w1q64_9_ei', 'w1q64_10_ei', 
  'w1q64_11_ei', 'w1q64_12_ei', 'w1q64_13_ei', 'w1q64_t_num']
  
# and these
feat_eng_dict['suicide_attempts'] = ['recode', 'w1q113_ei', 'w1q114_ei_r']
feat_eng_dict['outness'] = ['sum', 'w1q123a_ei_r', 
  'w1q123b_ei_r', 'w1q123c_ei_r', 'w1q123d_ei_r', 'w1q124_ei']
  
# check again
for k, v in feat_eng_dict.items():
  a = v[1:]
  for j in a:
    if j not in list(meyer.columns):
      print(k, j)
      
      
for k, v in feat_eng_dict.items():
  print(k, v)
  print('')

feat_eng_dict['health_insurance'] = ['binarize', 'w1q64_2_ei', 
  'w1q64_3_ei', 'w1q64_4_ei', 'w1q64_5_ei', 'w1q64_6_ei', 
  'w1q64_7_ei', 'w1q64_8_ei', 'w1q64_9_ei', 'w1q64_10_ei', 
  'w1q64_11_ei', 'w1q64_12_ei', 'w1q64_13_ei', 'w1q64_t_num']

# cut
drop_items = ['pers_well_being', 'age_awakening', 'age_out', 'neighb_welcoming']
drop_cols = ['w1q45_ei', 'w1q46_ei', 'w1q47_ei', 'w1q48_ei', 'w1q49_ei', 'w1q50_ei', 
  'w1q51_ei']




# mess with the columns before computing

def recode(dictry, name, cols):
  '''cols is a list of columns that need to be recoded.  
  name is the name I want to give the composite column based on cols
  dict is the STRING name of the dictionary (I need that for the func to modify it)
    this function will spit out the appropriate syntax, but only for THIS df.'''
  for i in cols[1:]:
    print(f"meyer[['{i}_r']] = meyer[['{i}']]")
  print('')
  for i in cols[1:]:
    print(f"meyer['{i}'].value_counts(dropna = False).sort_index()")
    print(f"meyer['{i}_r'].value_counts(dropna = False).sort_index()")
  print('')
  print(f"meyer.drop(columns = {cols[1:]}).shape")
  print(f"meyer.drop(columns = {cols[1:]}, inplace = True)")
  print('')
  cols_r = cols[:1] + [''.join([x, '_r']) for x in cols[1:]]
  print(f"{dictry}['{name}'] = {cols_r}")
# I then ran this a bunch of times in the console

# reverse code these so that 1=bad neighborhood and 0=fine
meyer[['w1q19a_ei_r']] = meyer[['w1q19a_ei']]-1
meyer[['w1q19b_ei_r']] = meyer[['w1q19b_ei']]-1
meyer[['w1q19c_ei_r']] = meyer[['w1q19c_ei']]-1
meyer[['w1q19d_ei_r']] = meyer[['w1q19d_ei']]-1
meyer.drop(columns = ['w1q19a_ei', 'w1q19b_ei', 'w1q19c_ei', 'w1q19d_ei']).shape
meyer.drop(columns = ['w1q19a_ei', 'w1q19b_ei', 'w1q19c_ei', 'w1q19d_ei'], inplace = True)
feat_eng_dict['bad_neighbhd'] = ['sum', 'w1q19a_ei_r', 'w1q19b_ei_r', 'w1q19c_ei_r', 'w1q19d_ei_r']

# reverse code these so that 1=disabled, 0=non-disabled
# currently it's 1=disabled, 2=non-disabled
# (1-2)*(-1)==1, (2-2)*(-1)==0
meyer[['w1q75_ei_r']] = abs(meyer[['w1q75_ei']]-2)
meyer[['w1q76_ei_r']] = abs(meyer[['w1q76_ei']]-2)

meyer['w1q75_ei'].value_counts(dropna = False, sort = True, ascending = True)
meyer['w1q75_ei_r'].value_counts(dropna = False, sort = True, ascending = True)
meyer['w1q76_ei'].value_counts(dropna = False, sort = True, ascending = True)
meyer['w1q76_ei_r'].value_counts(dropna = False, sort = True, ascending = True)

meyer.drop(columns = ['w1q75_ei', 'w1q76_ei']).shape
meyer.drop(columns = ['w1q75_ei', 'w1q76_ei'], inplace = True)

feat_eng_dict['disabled'] = ['binarize', 'w1q75_ei_r', 'w1q76_ei_r']

# recode these to eliminate the 0 (created during imputation), then 0-base
meyer[['w1q101_ei_r']] = meyer[['w1q101_ei']]
meyer[['w1q105_ei_r']] = meyer[['w1q105_ei']]
meyer[['w1q109_ei_r']] = meyer[['w1q109_ei']]

for i in ['sum', 'w1q101_ei', 'w1q105_ei', 'w1q109_ei']:
  print(f"cond = meyer['{i}']==0")
cond1 = meyer['w1q101_ei']==0
cond2 = meyer['w1q105_ei']==0
cond3 = meyer['w1q109_ei']==0

meyer.loc[cond1, 'w1q101_ei_r'] = 1
meyer.loc[cond2, 'w1q105_ei_r'] = 1
meyer.loc[cond3, 'w1q109_ei_r'] = 1

meyer['w1q101_ei'].value_counts(dropna = False).sort_index()
meyer['w1q101_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q105_ei'].value_counts(dropna = False).sort_index()
meyer['w1q105_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q109_ei'].value_counts(dropna = False).sort_index()
meyer['w1q109_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q101_ei', 'w1q105_ei', 'w1q109_ei']).shape
meyer.drop(columns = ['w1q101_ei', 'w1q105_ei', 'w1q109_ei'], inplace = True)

feat_eng_dict['suicidal_ideation'] = ['sum', 'w1q101_ei_r', 'w1q105_ei_r', 'w1q109_ei_r']

# ack I forgot to 0-base
# recode these to eliminate the 0 (created during imputation), then 0-base
meyer[['w1q101_ei_r']] = meyer[['w1q101_ei_r']]-1
meyer[['w1q105_ei_r']] = meyer[['w1q105_ei_r']]-1
meyer[['w1q109_ei_r']] = meyer[['w1q109_ei_r']]-1

# same for these
# actually, do I need both of these?

cond1 = meyer['w1q113_ei']>1
cond2 = meyer['w1q114_ei_r']==0

check = meyer.loc[(cond1 & cond2), ['w1q113_ei', 'w1q114_ei_r']]
# both times it's 3, 0
# I'm guessing they didn't want to say how many
# I'm going to impute 2 for them.
meyer.loc[(cond1 & cond2), 'w1q114_ei_r'] = 2

# And with that done, the first column is redundant!
# This entry in the dictionary now only has one column in its
# composite, and I actually think it would be better to combine
# it with the previous one, for an overall 'suicidality' column

meyer.shape
meyer[['w1q113_ei_r']] = meyer[['w1q113_ei']]
# meyer[['w1q114_ei_r_r']] = meyer[['w1q114_ei_r']]

meyer['w1q113_ei'].value_counts(dropna = False).sort_index()
# w1q113_ei
# 0.0       9
# 1.0    1122
# 2.0     251
# 3.0     112

# meyer['w1q113_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q114_ei_r'].value_counts(dropna = False).sort_index()
# w1q114_ei_r
# 0.0     1131
# 1.0      251
# [etc.]   112   # I manually added them up

# meyer['w1q114_ei_r_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q113_ei']).shape
meyer.drop(columns = ['w1q113_ei'], inplace = True)

# feat_eng_dict['suicide_attempts'] = ['recode', 'w1q113_ei_r', 'w1q114_ei_r_r']
drop_items.append('suicidal_ideation')
drop_items.append('suicide_attempts')
feat_eng_dict['suicidality'] = ['sum', 'w1q101_ei_r', 'w1q105_ei_r', 'w1q109_ei_r', 'w1q114_ei_r']


# I already got the 123s, but I need to reverse code 124
# here's what it is now -> what I want it to be
# MOST VISIBLE
# 1 -> 
# 2 -> 
# 3 -> 
# 4 -> 1
# 5 -> 0
# LEAST VISIBLE
# oh it's just 5 minus thing

meyer[['w1q124_ei_r']] = 5-meyer[['w1q124_ei']]

meyer['w1q123a_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q123b_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q123c_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q123d_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q124_ei'].value_counts(dropna = False).sort_index()
meyer['w1q124_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q124_ei']).shape
meyer.drop(columns = ['w1q124_ei'], inplace = True)

feat_eng_dict['outness'] = ['mean', 'w1q123a_ei_r', 'w1q123b_ei_r', 
  'w1q123c_ei_r', 'w1q123d_ei_r', 'w1q124_ei_r']

# these guys I just need to 0-base
meyer[['w1q135a_ei_r']] = meyer[['w1q135a_ei']]-1
meyer[['w1q135b_ei_r']] = meyer[['w1q135b_ei']]-1
meyer[['w1q135c_ei_r']] = meyer[['w1q135c_ei']]-1
meyer[['w1q135d_ei_r']] = meyer[['w1q135d_ei']]-1
meyer[['w1q135e_ei_r']] = meyer[['w1q135e_ei']]-1
meyer[['w1q135f_ei_r']] = meyer[['w1q135f_ei']]-1

meyer['w1q135a_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135a_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q135b_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135b_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q135c_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135c_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q135d_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135d_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q135e_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135e_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q135f_ei'].value_counts(dropna = False).sort_index()
meyer['w1q135f_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q135a_ei', 'w1q135b_ei', 'w1q135c_ei', 'w1q135d_ei', 'w1q135e_ei', 'w1q135f_ei']).shape
meyer.drop(columns = ['w1q135a_ei', 'w1q135b_ei', 'w1q135c_ei', 'w1q135d_ei', 'w1q135e_ei', 'w1q135f_ei'], inplace = True)

feat_eng_dict['abusive_treatment'] = ['sum', 'w1q135a_ei_r', 'w1q135b_ei_r', 'w1q135c_ei_r', 'w1q135d_ei_r', 'w1q135e_ei_r', 'w1q135f_ei_r']

# same 
meyer[['w1q137_ei_r']] = meyer[['w1q137_ei']]-1
meyer[['w1q138_ei_r']] = meyer[['w1q138_ei']]-1

meyer['w1q137_ei'].value_counts(dropna = False).sort_index()
meyer['w1q137_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q138_ei'].value_counts(dropna = False).sort_index()
meyer['w1q138_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q137_ei', 'w1q138_ei']).shape
meyer.drop(columns = ['w1q137_ei', 'w1q138_ei'], inplace = True)

feat_eng_dict['work_neg_outcomes'] = ['sum', 'w1q137_ei_r', 'w1q138_ei_r']

# recode code these guys so 1=stress and 0=not
meyer[['w1q142a_ei_r']] = abs(meyer[['w1q142a_ei']]-2)
meyer[['w1q142h_ei_r']] = abs(meyer[['w1q142h_ei']]-2)
meyer[['w1q142i_ei_r']] = abs(meyer[['w1q142i_ei']]-2)

meyer['w1q142a_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142a_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142h_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142h_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142i_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142i_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q142a_ei', 'w1q142h_ei', 'w1q142i_ei']).shape
meyer.drop(columns = ['w1q142a_ei', 'w1q142h_ei', 'w1q142i_ei'], inplace = True)

feat_eng_dict['stress_past_year_gen'] = ['sum', 'w1q142a_ei_r', 'w1q142h_ei_r', 'w1q142i_ei_r']

# these too
meyer[['w1q142b_ei_r']] = abs(meyer[['w1q142b_ei']]-2)
meyer[['w1q142c_ei_r']] = abs(meyer[['w1q142c_ei']]-2)
meyer[['w1q142e_ei_r']] = abs(meyer[['w1q142e_ei']]-2)

meyer['w1q142b_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142b_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142c_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142c_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142e_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142e_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q142b_ei', 'w1q142c_ei', 'w1q142e_ei']).shape
meyer.drop(columns = ['w1q142b_ei', 'w1q142c_ei', 'w1q142e_ei'], inplace = True)

feat_eng_dict['stress_past_year_work'] = ['sum', 'w1q142b_ei_r', 'w1q142c_ei_r', 'w1q142e_ei_r']

# and these
meyer[['w1q142d_ei_r']] = abs(meyer[['w1q142d_ei']]-2)
meyer[['w1q142f_ei_r']] = abs(meyer[['w1q142f_ei']]-2)
meyer[['w1q142g_ei_r']] = abs(meyer[['w1q142g_ei']]-2)

meyer['w1q142d_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142d_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142f_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142f_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142g_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142g_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q142d_ei', 'w1q142f_ei', 'w1q142g_ei']).shape
meyer.drop(columns = ['w1q142d_ei', 'w1q142f_ei', 'w1q142g_ei'], inplace = True)

feat_eng_dict['stress_past_year_interpersonal'] = ['sum', 'w1q142d_ei_r', 'w1q142f_ei_r', 'w1q142g_ei_r']

# and these
meyer[['w1q142j_ei_r']] = abs(meyer[['w1q142j_ei']]-2)
meyer[['w1q142k_ei_r']] = abs(meyer[['w1q142k_ei']]-2)

meyer['w1q142j_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142j_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q142k_ei'].value_counts(dropna = False).sort_index()
meyer['w1q142k_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q142j_ei', 'w1q142k_ei']).shape
meyer.drop(columns = ['w1q142j_ei', 'w1q142k_ei'], inplace = True)

feat_eng_dict['stress_past_year_crime'] = ['sum', 'w1q142j_ei_r', 'w1q142k_ei_r']

# religiosity 

# here's what 179 is now; 1 and 2 are massive in 180
# 1 Protestant (for example, Baptist, Methodist) 295 19.4 %
# 2 Roman Catholic 133 8.8 %
# 3 Mormon (Church of Jesus Christ of Latter-day Saints or LDS) 10 0.7 %
# 4 Orthodox (Greek, Russian, or another Orthodox church) 6 0.4 %

# 5 Jewish 38 2.5 %
# 6 Muslim 3 0.2 %
# 7 Buddhist 30 2.0 %
# 8 Hindu 1 0.1 %
# 11 Spiritual 262 17.3 %
# 12 Something else 95 6.3 %

# 9 Atheist (do not believe in God) 192 12.6 %
# 10 Agnostic (not sure if there is a God) 156 10.3 %
# 13 Nothing in particular 273 18.0 %

# collapse 3-8 into "other organized"
# .... actually collapse more, bcz this needs to be OHE'd

# 1-4 christian-influenced religious     1
# 5-8, 11-12  non-christian religious    5
# 9-10, 13 not religious                 make this 0, because it's literally none

relig_recode = {1: 1, 2: 1, 3: 1, 4: 1, # vaguely christian
  5: 5, 6: 5, 7: 5, 8: 5, 11: 5, 12: 5, # religious but not christian
  9: 0, 10: 0, 13: 0} # not religious

# 179 and 180 are the "are you religious / were you raised religious" Qs
meyer['w1q179_ei_r'] = meyer['w1q179_ei'].map(relig_recode)
meyer['w1q180_ei_r'] = meyer['w1q180_ei'].map(relig_recode)

meyer['w1q179_ei'].value_counts(dropna = False).sort_index()
meyer['w1q179_ei_r'].value_counts(dropna = False).sort_index()
meyer['w1q180_ei'].value_counts(dropna = False).sort_index()
meyer['w1q180_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q179_ei', 'w1q180_ei']).shape
meyer.drop(columns = ['w1q179_ei', 'w1q180_ei'], inplace = True)

# I actually cannot think of a meaningful way to combine these.I think the 
# thing to do is just leave them all in alone, then see what pops as meaningful.

# feat_eng_dict['religiosity'] = ['recode', 'w1q179_ei_r', 'w1q180_ei_r', 'w1q181_ei_r']
drop_items.append('religiosity')


# 181 is about how often you attend religious services
meyer[['w1q181_ei_r']] = 6-(meyer[['w1q181_ei']])

meyer['w1q181_ei'].value_counts(dropna = False).sort_index()
meyer['w1q181_ei_r'].value_counts(dropna = False).sort_index()

meyer.drop(columns = ['w1q181_ei']).shape
meyer.drop(columns = ['w1q181_ei'], inplace = True)

# woohoo!  save it to a csv
meyer.to_csv('2024-06-06_recodes-for-feat-eng-dict-done_not-ohe-yet.csv', index = False)

# just ohe them now while I'm thinking about it
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ohe = OneHotEncoder(drop = None, # I want to manually drop a specific one
  handle_unknown = 'ignore', sparse_output = False) 

ctx = ColumnTransformer(transformers=[('one_hot', ohe, ['w1q179_ei_r', 'w1q180_ei_r'])],
    remainder = 'passthrough', verbose_feature_names_out=False)

meyer_ohe = pd.DataFrame(data = ctx.fit_transform(meyer), 
  columns = ctx.get_feature_names_out())
meyer_ohe.shape

# drop the non-religious ones
meyer_ohe.drop(columns = ['w1q179_ei_r_0', 'w1q180_ei_r_0']).shape
meyer_ohe.drop(columns = ['w1q179_ei_r_0', 'w1q180_ei_r_0'], inplace = True)

relig_rename = {'w1q179_ei_r_1': 'w1q179_ei_r_relig_christ', 
  'w1q179_ei_r_5': 'w1q179_ei_r_relig_other', 
  'w1q180_ei_r_1': 'w1q180_ei_r_relig_christ', 
  'w1q180_ei_r_5': 'w1q180_ei_r_relig_other'}

meyer_ohe.rename(columns = relig_rename, inplace = True)

# put it back in the right name
meyer = meyer_ohe.copy(deep = True)

# drop the columns I set aside before
meyer.drop(columns = drop_cols, inplace = True)

# save to csv
meyer.to_csv('2024-06-06_recodes-for-feat-eng-dict-done_religious-ohe-done.csv', index = False)

# finish updating the feat_eng_list

# safety first
feat_eng_backup = feat_eng_dict.copy()

for i in drop_items:
  del feat_eng_dict[i]
# thanks to stack overflow for the knowledge that that's how to del dict entries
# https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary

# oh one more thing
# Reorder the columns
ordered_cols = sorted(list(meyer.columns))
ordered_cols.remove('studyid')
ordered_cols = ['studyid'] + ordered_cols
len(ordered_cols) # 228
len(list(meyer.columns)) # 228
meyer.shape # (1494, 228)

meyer = meyer[ordered_cols]
meyer.shape

# save to csv
meyer.to_csv('2024-06-06_recodes-for-feat-eng-dict-done_religious-ohe-done_reordered.csv', index = False)


