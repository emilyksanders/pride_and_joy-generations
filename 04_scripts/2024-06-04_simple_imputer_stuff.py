# Written Tuesday, June 4, 2024
# FOR Wednesday, June 5, 2024

# from the backup
os.getcwd()
meyer = pd.read_csv('2024-06-05_meyer_much_imputation_done_but_not_si_yet.csv',
  sep = ',', low_memory=False, na_values = ' ')
  
# THERE WAS MORE STUFF ON THAT SCRIPT AFTER SAVING THE CSV

# Much of this was copied from impt_misc

# The simple imputer stuff

s_median = ["w1q50", "w1q48", "w1q51", "w1q112", 
  "w1q49", "w1q47", "w1q46", "w1q45", "w1q146c", 
  "w1q162", "w1q181", "w1q146f", "w1q146g", "w1q146e", # original ^ added V
  "w1q103", "w1q104", "w1q106", "w1q107", "w1q108", 
  "w1q111", "w1q115", "w1q116", "w1q117", "w1q134", 
  "w1q146a", "w1q146h", "w1q146i", "w1q146j", "w1q146k", 
  "w1q146l", "w1q169"]

s_mode = ["w1q175", "w1q72", "w1q142d", "w1q65", "w1q52", 
  "w1q142i", "w1q142g", "w1q180", "w1q69", "w1q135d", 
  "w1q142h", "w1q135b", "w1q135c", "w1q135e", "w1q142b", 
  "w1q142e", "w1q142f", "w1q142j", "w1q142a", "w1q142k", 
  "w1q19c", "w1q19d", "w1q19b", "w1q19a", "w1q75", 
  "w1q78", "w1q79", "w1q76",                    # original ^ added V
  "w1q135a", "w1q135f", "w1q142c", "w1q35", "w1q36", 
  "w1q37", "w1q38", "w1q124", "w1q89"]

# agh I found more

s_median_2 = '''
w1q103
w1q104
w1q106
w1q107
w1q108
w1q111
w1q115
w1q116
w1q117
w1q134
w1q146a
w1q146h
w1q146i
w1q146j
w1q146k
w1q146l
w1q169'''

s_mode_2 = '''
w1q135a
w1q135f
w1q142c
w1q35
w1q36
w1q37
w1q38
w1q124
w1q89'''

print(s_median_2.replace('\n', '", "'))
print(s_mode_2.replace('\n', '", "'))

s_97s = []
s_98s = []
s_99s = []
for i in s_median:
  a = list(meyer[i].unique())
  if ((97 in a) | (97. in a)):
    s_97s.append(i)
  if ((98 in a) | (98. in a)):
    s_98s.append(i)
  if ((99 in a) | (99. in a)):
    s_99s.append(i)
    
s_97s.sort()
s_98s.sort()
s_99s.sort()

for i in s_mode:
  a = list(meyer[i].unique())
  if ((97 in a) | (97. in a)):
    s_97s.append(i)
  if ((98 in a) | (98. in a)):
    s_98s.append(i)
  if ((99 in a) | (99. in a)):
    s_99s.append(i)

s_97s = ['w1q102', 'w1q103', 'w1q104', 
  'w1q106', 'w1q107', 'w1q108', 'w1q110', 'w1q111', 'w1q112',   # impute to 0s; 
  'w1q114', 'w1q115', 'w1q116', 'w1q117', 'w1q134']    # these are (mostly) age Qs
s_98s = ['w1q45', 'w1q46', 'w1q47', 'w1q48', 'w1q49', 'w1q50', 'w1q51']  # NA
s_99s = ['w1q45', 'w1q46', 'w1q47', 'w1q48', 'w1q49', 'w1q50', 'w1q51']  # age + 2

s_median_new = [''.join([x, '_ei']) for x in s_median]
s_mode_new = [''.join([x, '_ei']) for x in s_mode]

s_97s_new = [''.join([x, '_ei']) for x in s_97s]
s_98s_new = [''.join([x, '_ei']) for x in s_98s]
s_99s_new = [''.join([x, '_ei']) for x in s_99s]

# Replace these 97s with 0s
meyer.loc[:, s_97s_new] = np.where(meyer.loc[:, s_97s]==97, 0, meyer.loc[:, s_97s])

# Take a peek
meyer[['w1q102', 'w1q103', 'w1q102_ei', 'w1q103_ei']]


# Replace these 98s with NAs
meyer.loc[:, s_98s_new] = np.where(meyer.loc[:, s_98s]==98, np.nan, meyer.loc[:, s_98s])

# Take a peek
meyer[['w1q45', 'w1q46', 'w1q45_ei', 'w1q46_ei']]


# Replace these 99s with NAs
meyer.loc[:, s_99s_new] = np.where(meyer.loc[:, s_99s]==99, np.nan, meyer.loc[:, s_99s_new])

# Take a peek
meyer[['w1q45', 'w1q46', 'w1q45_ei', 'w1q46_ei']]


xs_97s = []
xs_98s = []
xs_99s = []

# for i in s_97s_new:
# for i in s_98s_new:
for i in s_99s_new:
  a = list(meyer[i].unique())
  if ((97 in a) | (97. in a)):
    xs_97s.append(i)
  if ((98 in a) | (98. in a)):
    xs_98s.append(i)
  if ((99 in a) | (99. in a)):
    xs_99s.append(i)
# none left!

# Right here I need to figure out how to deal with the 97s-99s.
# Ok here's hoping that's settled!

# put them in order.  checking them made me crazy otherwise
s_mode.sort()
s_mode_new.sort()
s_median.sort()
s_median_new.sort()

# make sure they're in order
for i, j in list(zip(s_mode, s_mode_new)):
  print(i, j)
for i, j in list(zip(s_median, s_median_new)):
  print(i, j)

# They are!  Ok!  Let's go again!!

# Safety first
# meyer.to_csv('2024-06-05_meyer_much_imputation_done_but_not_si_yet.csv', index = False)

# I think the cleanest way to do this without it breaking everything is to
# break the dataframe apart, use the 2 SIs separately, then re-merge.
# Let me check that the studyID will be suitable for merging on.

meyer.shape # (1507, 271)
# ah crap gotta drop the original 97s-99s

drop_90s = s_97s + s_98s # s_99s = s_98s
meyer.drop(columns = drop_90s, inplace = True)


meyer.shape # 1507 rows (250 columns)
meyer['studyid'].nunique() # 1507 unique values

# update the lists of columns
med_cols = [c if c in list(meyer.columns) else ''.join([c, '_ei']) for c in s_median]
mode_cols = [c if c in list(meyer.columns) else ''.join([c, '_ei']) for c in s_mode]

# split the df up for imputing
meyer_median = meyer[med_cols+['studyid']]
meyer_mode = meyer[mode_cols+['studyid']]

# new column names
s_median_new.append('studyid')
s_mode_new.append('studyid')
meyer_median.columns = s_median_new
meyer_mode.columns = s_mode_new

# Instantiate
from sklearn.impute import SimpleImputer

si_med = SimpleImputer(strategy = 'median')
si_mode = SimpleImputer(strategy = 'most_frequent')

# do the imputation!
meyer_median = pd.DataFrame(
  si_med.fit_transform(meyer_median), columns = si_med.get_feature_names_out())

meyer_mode = pd.DataFrame(
  si_mode.fit_transform(meyer_mode), columns = si_mode.get_feature_names_out())

# is it really that easy?
meyer_median.isna().sum().sum()
meyer_mode.isna().sum().sum()

mme = meyer_median.describe()
mmo = meyer_mode.describe()

# Yes!  It is!  (This time.)

# BUT because I imputed the 97s to be 0s, and there were so many 97s, that made the 
# median and mode 0.  So most of these guys just ended up imputed with 0s.
# It's not exactly what I wanted (the true missings are people who DID have the 
# relevant thoughts, but just wouldn't say when), but given that there are so few 
# true missings, and that this has already eaten up a ton of time, I think it'll
# be fine to leave for this iteration.  Put it in the next steps.

# OK LAST THING RE-MERGE WOOHOO!
meyer.shape # full thing has 250 columns
len(s_median) # 31, including ID
len(s_mode) # 37, including ID

# also let me check some stuff
# are the column names what I think they are?
s_median_new==list(meyer_median.columns) # True
s_mode_new==list(meyer_mode.columns) # True
# is studyid the only column name that doesn't end in _ei
[c for c in list(meyer_median.columns) if c.split('_')[-1]!='ei']
[c for c in list(meyer_mode.columns) if c.split('_')[-1]!='ei']

# ok let's GOOOO
# I'm just going to combine all the possible columns that I might
# now need to drop, rather than trying to remember which is which.
# And then I'll filter it down to only the ones actually in meyer.columns.

# drop_cols = s_median + s_mode + s_median_new + s_mode_new
# len(drop_cols) # 138
# 
# drop_cols = [c for c in drop_cols if c in list(meyer.columns)]
# drop_cols = list(set(drop_cols))
# drop_cols.remove('studyid')
# len(drop_cols) # 68
# ((len(s_median_new)-1) + (len(s_mode_new)-1)) # 66
# # ooooh right I added some other suicide questions in and fixed their 97s
# x = [c for c in drop_cols if c not in s_mode]
# x = [c for c in x if c not in s_mode_new]
# x = [c for c in x if c not in s_median_new]
# x = [c for c in x if c not in s_median]
# x # empty
# x = [c for c in drop_cols if c not in s_mode_new]
# x = [c for c in x if c not in s_median_new]
# x

# oh. duh. new approach
drop_cols = med_cols + mode_cols
len(drop_cols) # 68
compare = [c for c in drop_cols if c in list(meyer.columns)]
len(compare) # 68
len(list(meyer_median.columns) + list(meyer_mode.columns)) # 70

# safety first
# meyer.to_csv('2024-06-05_pre-si-remerging.csv', index = False)
# meyer_median.to_csv('2024-06-05_values-imputed-with-median.csv', index = False)
# meyer_mode.to_csv('2024-06-05_values-imputed-with-mode.csv', index = False)

# drop cols
meyer.drop(columns = drop_cols, inplace = True) # [1507 rows x 182 columns]

# merge
meyer_m = meyer.merge(
  meyer_median, left_on = 'studyid', right_on = 'studyid', how = 'left').merge(
    meyer_mode, left_on = 'studyid', right_on = 'studyid', how = 'left')

meyer_m.shape # (1507, 250)

meyer_m.isna().sum()

meyer = meyer_m.copy(deep = True)

del meyer_m

# meyer.to_csv('2024-06-05_si-imputation-done_remerged.csv', index = False)

