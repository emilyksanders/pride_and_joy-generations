# Tuesday, June 4, 2024
# Imputation, Take 3

# This script is a re-write of the other, earlier 
# script from today.  I tried a bunch of different
# ways to deal with the 97s, and it took a while
# to get one to work.

meyer.shape # (1507, 267)

# drop some columns
drop_cols_3 = ["w1q20_t_verb", "w1q39_7", "w1q39_12", 
  "w1q39_t_verb", "w1q39_6", "w1q39_5", "w1q39_2", "w1q39_3", 
  "w1q39_4", "w1q39_1", "w1q39_9", "w1q39_8", "w1q39_10", 
  "w1q39_11", "gp1", "gemployment2010", "gmilesaway"]

len(drop_cols_3)

# Ok I started with 267 and dropped 17. Should now be 250.
meyer.drop(columns = drop_cols_3).shape # Yep, (1507, 250)!
meyer.drop(columns = drop_cols_3, inplace = True)
meyer.shape

diy_ohe = ["w1q145_3", "w1q163_3", "w1q136_3", "w1q145_9", 
  "w1q143_3", "w1q136_10", "w1q145_10", "w1q136_9", "w1q163_10", 
  "w1q163_9", "w1q143_9", "w1q143_4", "w1q136_6", "w1q143_10", 
  "w1q143_5", "w1q145_4", "w1q136_5", "w1q143_8", "w1q163_5", 
  "w1q136_4", "w1q163_6", "w1q145_6", "w1q136_1", "w1q143_7", 
  "w1q163_1", "w1q143_2", "w1q143_1", "w1q145_5", "w1q143_6", 
  "w1q163_2", "w1q163_4", "w1q136_8", "w1q145_8", "w1q145_1", 
  "w1q145_7", "w1q163_7", "w1q136_2", "w1q145_2", "w1q139_3", 
  "w1q136_7", "w1q139_9", "w1q139_10", "w1q139_5", "w1q139_4", 
  "w1q139_8", "w1q139_6", "w1q139_2", "w1q139_1", "w1q139_7", 
  "w1q163_8", "w1q141_3", "w1q141_9", "w1q141_10", "w1q141_8", 
  "w1q141_4", "w1q141_1", "w1q141_5", "w1q141_2", "w1q141_7", 
  "w1q141_6", "w1q64_12", "w1q64_5", "w1q74_5", "w1q74_6", 
  "w1q74_20", "w1q64_11", "w1q64_10", "w1q74_18", "w1q74_14", 
  "w1q74_17", "w1q171_8", "w1q30_3", "w1q64_13", "w1q64_7", 
  "w1q30_4", "w1q171_6", "w1q171_4", "w1q64_8", "w1q74_10", 
  "w1q74_21", "w1q64_6", "w1q74_11", "w1q171_5", "w1q64_3", 
  "w1q64_1", "w1q171_9", "w1q30_5", "w1q171_3", "w1q74_22", 
  "w1q64_9", "w1q171_2", "w1q171_7", "w1q74_23", "w1q64_4", 
  "w1q64_2", "w1q30_1", "w1q171_1", "w1q30_2"]

value_list = []
for i in diy_ohe:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)

# create some new column names
diy_ohe_new = [''.join([x, '_ei']) for x in diy_ohe]

# let's see if this replaces the 97s right
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe]==97, 0, meyer.loc[:, diy_ohe])

# check this
for i, j in list(zip(diy_ohe, diy_ohe_new))[50:]:
  print(i)
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  print(j)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')
  print('='*20)

# I'm looking for valid 7s.
# It seems like 7 was also used as an NA code
# because why be consistent lolololol!!!!!!!!

nat_7s = ['w1q143_7', 'w1q145_7', 'w1q163_7', 'w1q136_7', 
  'w1q139_7', 'w1q141_7', 'w1q64_7', 'w1q171_7']
  
nat_7s == [c for c in diy_ohe if c.split('_')[-1]=='7']
# True.

nat_7s_ei = [''.join([x, '_ei']) for x in nat_7s]

# let's turn those 7s into 1s, and then the rest into 0s
meyer.loc[:, nat_7s_ei] = np.where(meyer.loc[:, nat_7s]==7, 1, meyer.loc[:, nat_7s])

# check this
for i in nat_7s_ei:
  meyer[i].value_counts(dropna = False)
  print('='*20)

# check one against the documentation
meyer['w1q141_7'].value_counts(dropna = False)

# check this again, should be no more 97s, but nothing else weird
remaining_7s = []
value_list_2 = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  if 7 in a:
    remaining_7s.append(i)
  value_list_2 += a
value_list_2 = list(set(value_list_2))
sorted(value_list_2)

remaining_7s_qs = [x.split('_')[0] for x in remaining_7s]
sorted(set(remaining_7s_qs))
# I went through VERY CAREFULLY and confirmed that all the 
# remaining 7s are "planned missings."

# let's see if this replaces the 97s right
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe_new]==7, 0, meyer.loc[:, diy_ohe_new])

# check this
for i, j in list(zip(diy_ohe, diy_ohe_new))[:50]:
  print(i)
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  print(j)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')
  print('='*20)

meyer[diy_ohe_new] = meyer[diy_ohe_new].fillna(0)

# check again!
for i, j in list(zip(diy_ohe, diy_ohe_new))[:50]:
  print(i)
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  print(j)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')
  print('='*20)

# wait, some of them still have 97s??

# let's see if this replaces the 97s right
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe_new]==97.0, 0, meyer.loc[:, diy_ohe_new])

for i, j in list(zip(diy_ohe, diy_ohe_new))[:50]:
  print(i)
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  print(j)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')
  print('='*20)
  
# this again too
remaining_7s_2 = []
remaining_97s = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  if 7 in a:
    remaining_7s_2.append(i)
  if 97 in a:
    remaining_97s.append(i)
sorted(set(remaining_7s_2))
sorted(set(remaining_97s))

# check AGAIN
value_list_x = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list_x += a
value_list_x = list(set(value_list_x))
sorted(value_list_x)

# make a backup
os.getcwd()
meyer.to_csv('2024-06-05_meyer_backup_diy_ohe_no_97s_7s.csv', index = False)


# reduce to 0s and 1s
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe_new]!=0, 1, meyer.loc[:, diy_ohe_new])

for i, j in list(zip(diy_ohe, diy_ohe_new))[:50]:
  print(i)
  meyer[i].value_counts(dropna = False)
  print('-'*20)
  print(j)
  meyer[j].value_counts(dropna = False)
  print('='*20)
  print('')
  print('='*20)

# no NAs?
meyer[diy_ohe_new].isna().sum().sum()
# no NAs!

# drop the old versions
meyer.drop(columns = diy_ohe, inplace = True)

# check the dtypes
pd.set_option('display.max_rows', None)
meyer.dtypes

# should be VERY short now!
value_list_3 = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list_3 += a
value_list_3 = list(set(value_list_3))
sorted(value_list_3)
