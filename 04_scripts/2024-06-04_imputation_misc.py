# Tuesday, June 4, 2024
# More Imputation!

# w1q64_t_verb
meyer['w1q64_t_verb'].value_counts(dropna = False)
meyer.shape # 250 columns - gonna add one then delete the original
# meyer['w1q64_t_num'] = meyer['w1q64_t_verb'].fillna('0')
# I got a weird warning here ^, so for future runs V
meyer[['w1q64_t_num']] = meyer[['w1q64_t_verb']].fillna('0')
# for right now V
meyer_c = meyer.copy(deep = True)
meyer = meyer_c.copy(deep = True)
meyer.shape
# thanks to this SO article for advice
# https://stackoverflow.com/questions/68292862/performancewarning-dataframe-is-highly-fragmented-this-is-usually-the-result-o

# reduce to 0s and 1s
meyer.loc[:, 'w1q64_t_num'] = np.where(meyer.loc[:, 'w1q64_t_num']!='0', 1, 0)

# check
meyer['w1q64_t_num'].value_counts(dropna = False)
meyer['w1q64_t_verb'].value_counts(dropna = False)

# drop the original
meyer.drop(columns = ['w1q64_t_verb'], inplace = True)


# gmilesaway2
meyer['gmilesaway2'].value_counts(dropna = False)

meyer[['gmilesaway2_ei']] = meyer[['gmilesaway2']].fillna(0)
meyer['gmilesaway2'].value_counts(dropna = False)
meyer['gmilesaway2_ei'].value_counts(dropna = False)

# reverse code so 1=close
meyer[['gmilesaway2_ei_r']] = 1-meyer[['gmilesaway2_ei']]
meyer['gmilesaway2'].value_counts(dropna = False)
meyer['gmilesaway2_ei'].value_counts(dropna = False)
meyer['gmilesaway2_ei_r'].value_counts(dropna = False)

# drop
meyer.drop(columns = ['gmilesaway2', 'gmilesaway2_ei'], inplace = True)
meyer.shape


# w1q123d & w1q123c
# These guys had some missing values, but also had an option (5)
# for "don't know/doesn't apply."  I don't know what the truth
# is for these missing values, so I'm recoding them to "don't know."

# What to do with the 5s 
# will be a question for the next round of cleaning.

meyer[['w1q123d_ei', 'w1q123c_ei']] = meyer[['w1q123d', 'w1q123c']].fillna(5)
meyer[['w1q123d_ei', 'w1q123c_ei', 'w1q123d', 'w1q123c']]

meyer.drop(columns = ['w1q123d', 'w1q123c'], inplace = True)


# w1q179
# impute as "nothing in particular", seems logical
meyer[['w1q179_ei']] = meyer[['w1q179']].fillna(13)
meyer[['w1q179', 'w1q179_ei']]

meyer.drop(columns = 'w1q179', inplace = True)


# all right!  real imputer time!!

# I'm going to go ahead and do this on the full dataset, 
# because screw it.
# If I have time, I can go back and re-run it with
# a train test split.  But for now I'm just going to do it
# all at once, with the justification that for an 
# inferential model, the TTS isn't that important.
# This data was gathered at a specific moment in history,
# and it covers some sensitive topics.  There is no 
# reason to design this process to accommodate for novel
# data extending into the future, because there is no
# reason to assume that these values wouldn't change
# over time.  (Which does kind of invalidate everything
# I'm doing on this 2016 dataset but SHHHHHHHHH.)

from sklearn.impute import SimpleImputer

si_med = SimpleImputer(strategy = 'median')
si_mode = SimpleImputer(strategy = 'most_frequent')

s_median = '''
w1q50
w1q48
w1q51
w1q112
w1q49
w1q47
w1q46
w1q45
w1q146c
w1q162
w1q181
w1q146f
w1q146g
w1q146e'''

s_mode = '''
w1q175
w1q72
w1q142d
w1q65
w1q52
w1q142i
w1q142g
w1q180
w1q69
w1q135d
w1q142h
w1q135b
w1q135c
w1q135e
w1q142b
w1q142e
w1q142f
w1q142j
w1q142a
w1q142k
w1q19c
w1q19d
w1q19b
w1q19a
w1q75
w1q78
w1q79
w1q76'''

print(s_median.replace('\n', '", "'))
print(s_mode.replace('\n', '", "'))

s_median = ["w1q50", "w1q48", "w1q51", "w1q112", 
  "w1q49", "w1q47", "w1q46", "w1q45", "w1q146c", 
  "w1q162", "w1q181", "w1q146f", "w1q146g", "w1q146e"]
  
s_mode = ["w1q175", "w1q72", "w1q142d", "w1q65", "w1q52", 
  "w1q142i", "w1q142g", "w1q180", "w1q69", "w1q135d", 
  "w1q142h", "w1q135b", "w1q135c", "w1q135e", "w1q142b", 
  "w1q142e", "w1q142f", "w1q142j", "w1q142a", "w1q142k", 
  "w1q19c", "w1q19d", "w1q19b", "w1q19a", "w1q75", 
  "w1q78", "w1q79", "w1q76"]

s_median_new = [''.join([x, '_ei']) for x in s_median]
s_mode_new = [''.join([x, '_ei']) for x in s_mode]

# # Safety first
# meyer.to_csv('meyer_much_imputation_done_but_not_si_yet.csv', index = False)
# 
# # I think the cleanest way to do this without it breaking everything is to
# # break the dataframe apart, use the 2 SIs separately, then re-merge.
# # Let me check that the studyID will be suitable for merging on.
# 
# meyer.shape # 1507 rows (250 columns)
# meyer['studyid'].nunique() # 1507 unique values
# 
# # split the df up for imputing
# meyer_median = meyer[s_median+['studyid']]
# meyer_mode = meyer[s_mode+['studyid']]
# 
# # new column names
# s_median_new.append('studyid')
# s_mode_new.append('studyid')
# meyer_median.columns = s_median_new
# meyer_mode.columns = s_mode_new
# 
# # do the imputation!
# meyer_median = pd.DataFrame(
#   si_med.fit_transform(meyer_median), columns = si_med.get_feature_names_out())
# 
# meyer_mode = pd.DataFrame(
#   si_mode.fit_transform(meyer_mode), columns = si_mode.get_feature_names_out())
# 
# # is it really that easy?
# meyer_median.isna().sum().sum()
# meyer_mode.isna().sum().sum()
# 
# mme = meyer_median.describe()
# mmo = meyer_mode.describe()
# 
# # No!  No, it is not!!
# # The stupid 97s, 98s, and 99s are at it again!


# Suicide and NSSH Qs

s = '''
w1q119
w1q109
w1q105
w1q113
w1q101'''

print(s.replace('\n', '", "'))

s = ["w1q119", "w1q109", "w1q105", "w1q113", "w1q101"]

s_ei = [''.join([x, '_ei']) for x in s]

meyer[s_ei] = meyer[s].fillna(0)

for i, j in zip(s, s_ei):
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')

meyer.drop(columns = s, inplace = True)

# RIGHT NOW THESE ARE 0S
# ONLY 1-3 IS DEFINED IN THE SCALE 
# (these are the suicide and nssh Qs)
# TOMORROW, plot it, and see how the 0 column
# compares to the others
# and reassign accordingly


# w1q32
# right or wrong these guys were TREATED as "no" in the survey
# so I'm going to code them that way.

meyer['w1q32'].value_counts(dropna = False)
meyer['w1q32'].fillna(2).value_counts(dropna = False)

meyer[['w1q32_ei']] = meyer[['w1q32']].fillna(2)

meyer[['w1q32_ei']].value_counts(dropna = False)

meyer.drop(columns = ['w1q32'], inplace = True)

meyer.shape
list(meyer.columns)
