# Wednesday, June 5, 2024
# Imputation Regrouping

# Most of my imputation is now done!  
# I really messed up my spreadsheet though, so I'm
# just going to make a new one.

os.getcwd()

meyer = pd.read_csv('2024-06-05_si-imputation-done_remerged.csv')

remaining_nas = pd.DataFrame(meyer.isna().sum())
original_nas = pd.read_excel('./dsb318-capstone/04_scratch_work/01_notes/imputation_plan.xlsx')
  
remaining_nas.shape
original_nas.shape

nas = remaining_nas.merge(
  original_nas, left_on = remaining_nas.index, right_on = 'column_name', how = 'left')

nas.index = list(remaining_nas.index)

nas = nas[nas[0]!=0]  # that column is the most up to date count
# if it's currently 0, drop it


# my spreadsheet got messed up, so I'm going back around on some of these

for i in nas['column_name']:
  print(f"meyer[['{i}_ei']] = meyer[['{i}']].fillna(_)")


# The easy-er ones

meyer[['w1q01_ei']] = meyer[['w1q01']].fillna(7)
meyer[['w1q02_ei']] = meyer[['w1q02']].fillna(8)
meyer[['w1q33_ei']] = meyer[['w1q33']].fillna(0)
meyer[['w1q123a_ei']] = meyer[['w1q123a']].fillna(5)
meyer[['w1q123b_ei']] = meyer[['w1q123b']].fillna(5)
meyer[['w1q114_ei']] = meyer[['w1q114_ei']].fillna(0) # note that this guy already existed
meyer[['w1q34_ei']] = meyer[['w1q34']].fillna(0) 
# I was originally going to impute this ^ from other info, but a 0 is fine and faster
meyer[['w1q121_ei']] = meyer[['w1q121']].fillna(0) # nssh age
meyer[['w1q122_ei']] = meyer[['w1q122']].fillna(0) # nssh age
meyer.shape # (1507, 258)

drop_cols = ['w1q01', 'w1q02', 'w1q33', 'w1q123a', 
  'w1q123b', 'w1q34', 'w1q121', 'w1q122']

meyer.drop(columns = drop_cols, inplace = True)
meyer.shape

# ooh boy here we go

# impute 2 if sum(139)>0, else mode
s = ''
for i in list(range(1, 11)):
  s += f'meyer["w1q139_{i}_ei"] + '

meyer['sum_w1q139'] = meyer["w1q139_1_ei"] + meyer[
  "w1q139_2_ei"] + meyer["w1q139_3_ei"] + meyer[
  "w1q139_4_ei"] + meyer["w1q139_5_ei"] + meyer[
  "w1q139_6_ei"] + meyer["w1q139_7_ei"] + meyer[
  "w1q139_8_ei"] + meyer["w1q139_9_ei"] + meyer["w1q139_10_ei"]

meyer['sum_w1q139'].value_counts(dropna = False)

meyer[['w1q137_ei']] = meyer[['w1q137']]
meyer[['w1q138_ei']] = meyer[['w1q138']]

cond1 = meyer['w1q137'].isna()
cond2 = meyer['w1q138'].isna()

meyer.loc[cond1, 'w1q137_ei'] = np.where(meyer.loc[cond1, 'sum_w1q139']>0, 2, 1)
meyer.loc[cond2, 'w1q138_ei'] = np.where(meyer.loc[cond2, 'sum_w1q139']>0, 2, 1)

meyer['w1q137'].value_counts(dropna = False)
meyer['w1q137_ei'].value_counts(dropna = False)
meyer['w1q138'].value_counts(dropna = False)
meyer['w1q138_ei'].value_counts(dropna = False)

# nice
meyer.drop(columns = ['w1q137', 'w1q138', 'sum_w1q139'], inplace = True)
meyer.shape


# impute 2 if sum(141)>0, else mode
meyer['sum_w1q141'] = meyer["w1q141_1_ei"] + meyer[
  "w1q141_2_ei"] + meyer["w1q141_3_ei"] + meyer[
  "w1q141_4_ei"] + meyer["w1q141_5_ei"] + meyer[
  "w1q141_6_ei"] + meyer["w1q141_7_ei"] + meyer[
  "w1q141_8_ei"] + meyer["w1q141_9_ei"] + meyer["w1q141_10_ei"]

meyer['sum_w1q141'].value_counts(dropna = False)

meyer[['w1q140_ei']] = meyer[['w1q140']]

cond1 = meyer['w1q140'].isna()

meyer.loc[cond1, 'w1q140_ei'] = np.where(meyer.loc[cond1, 'sum_w1q141']>0, 2, 1)

meyer['w1q140'].value_counts(dropna = False)
meyer['w1q140_ei'].value_counts(dropna = False)

# nice
meyer.drop(columns = ['w1q140', 'sum_w1q141'], inplace = True)
meyer.shape


# subset investigation; there were exactly 48 do not knows on q2

cond1 = meyer['w1q03'].isna()

test = meyer.loc[cond1, ['w1q02_ei', 'w1q03']]
test['w1q02_ei'].value_counts(dropna = False, normalize = True) # why so many 8s?
meyer['w1q02_ei'].value_counts(dropna = False, normalize = True)  # close enough for now

# I conducted that test to see if the 48 NAs in Q3 were the same
# people as the 48 "don't knows" in  Q2, or any other pattern.
# I did not find one, and therefore imputed the mode, which is 2.

meyer[['w1q03_ei']] = meyer[['w1q03']].fillna(2)

meyer.shape
meyer.drop(columns = 'w1q03', inplace = True)


# impute from 142b or .c=True and 142e=False; and/or w1q171_x
meyer['w1q142b_ei'].value_counts(dropna = False)
meyer['w1q142c_ei'].value_counts(dropna = False)
meyer['w1q146d'].value_counts(dropna = False)

jobless_142s = ((meyer['w1q142b_ei']==1) | (meyer['w1q142c_ei']==1))
cond1 = meyer['w1q146d'].isna()

meyer[['w1q146d_ei']] = meyer[['w1q146d']]

# meyer.loc[cond1, 'w1q146d_ei'] = np.where(meyer.loc[cond1, 'sum_w1q141']>0, 2, 1)

# trying to do the np.where is making my head hurt, so
for i in list(range(1507)):
  if pd.notna(meyer.loc[i, 'w1q146d_ei'])==True:
    continue
  elif meyer.loc[i, 'w1q142c_ei']==1:
    meyer.loc[i, 'w1q146d_ei']=1
  elif meyer.loc[i, 'w1q142b_ei']==1:
    meyer.loc[i, 'w1q146d_ei']=1
  else:
    meyer.loc[i, 'w1q146d_ei']=0

meyer['w1q142b_ei'].value_counts(dropna = False)
meyer['w1q142c_ei'].value_counts(dropna = False)
meyer['w1q146d'].value_counts(dropna = False)
meyer['w1q146d_ei'].value_counts(dropna = False)

meyer.drop(columns = 'w1q146d', inplace = True)
meyer.shape


# impute from poverty
meyer[['w1q146b_ei']] = meyer[['w1q146b']]

money_cols = ['w1q146b', 'w1poverty_i', # 'w1povertycat_i', 
  'w1q142h_ei', 'w1age', 'geducation', 'w1q175_ei']

[c for c in list(meyer.columns) if c.split('_')[-1] not in ['ei', 'i']]

# 142h: During the last year have you experienced a major financial crisis; 1=y, 2=n
# 175: under water w/ debt; 1=n, 2=y  --- student loans?  maybe but that's getting too bespoke

meyer['w1q175_ei'].value_counts()
meyer['w1q146b'].value_counts()

pd.set_option('display.max_columns', None)
meyer.loc[(meyer['w1q146b'].isna()), money_cols]

a = sorted(list(meyer.columns))

# I checked several columns that also have to do with money.
# The census questions can address most of these NAs. 
# I imputed a bunch of values for w1q175, so I'm hesitant
# to use it to impute others.  w1q142h_ei (major financial
# crisis) is a 2 (no) for all of the remaining NAs.
# For the rest I'm going to impute 0.  It's a close tie
# between 0 (not true that they don't have enough money
# to make ends meet) and 1+2 (somewhat or very true), and
# I'm tempted to impute a 1 (somewhat true that they don't
# have enough money to make ends meet), but it feels less
# presumptuous to impute a 0.

# trying to do the np.where is making my head hurt, so
for i in list(range(1507)):
  if pd.notna(meyer.loc[i, 'w1q146b_ei'])==True:
    continue
  elif meyer.loc[i, 'w1poverty_i']==1:  # census poverty yes
    meyer.loc[i, 'w1q146b_ei']=1
  else:
    meyer.loc[i, 'w1q146b_ei']=0

meyer['w1q146b'].value_counts(dropna = False)
meyer['w1q146b_ei'].value_counts(dropna = False)

meyer.drop(columns = 'w1q146b', inplace = True)
meyer.shape



# subset investigation
# these are the Qs about US nativity

meyer = pd.read_csv('2024-06-05_most-imputation-done_midway-through-nativity.csv')

meyer[['w1q166_ei']] = meyer[['w1q166']]
meyer[['w1q167_ei']] = meyer[['w1q167']]
meyer[['w1q168_ei']] = meyer[['w1q168']]

test = meyer[['w1q166', 'w1q167', 'w1q168']]
test1 = test[test['w1q166'].isna()] # u born here?
test2 = test[test['w1q167'].isna()] # u live here 6-13?
test3 = test[test['w1q168'].isna()] # parents NOT born here?

# if they left all 3 blank, I'm imputing the mode
a = meyer['w1q166'].isna()
b = meyer['w1q167'].isna()
c = meyer['w1q168'].isna()

meyer.loc[(a & b & c), 'w1q166_ei'] = 1
meyer.loc[(a & b & c), 'w1q167_ei'] = 1
meyer.loc[(a & b & c), 'w1q168_ei'] = 3

# look again
test = meyer[['w1q166_ei', 'w1q167_ei', 'w1q168_ei']]
test1 = test[test['w1q166_ei'].isna()] # u born here?
test2 = test[test['w1q167_ei'].isna()] # u live here 6-13?
test3 = test[test['w1q168_ei'].isna()] # parents NOT born here?

# ok now the rest
# looking at the pattern of associated 167s and 168s, I think 
# it's safe to impute the remaining (n=5) NAs in 166 as 1 

meyer[['w1q166_ei']] = meyer[['w1q166_ei']].fillna(1)

# looking at the pattern of associated 166s and 168s, I think 
# it's safe to impute the remaining (n=5) NAs in 167 thusly:
a = meyer['w1q166']==2 # I wasn't born here
b = meyer['w1q167'].isna()
c = ((meyer['w1q168'].notna()) & (meyer['w1q168']<3)) # 1+ parent not born here

meyer.loc[(a & b & c), 'w1q167_ei'] = 2 # under those conditions, impute NO
meyer[['w1q167_ei']] = meyer[['w1q167_ei']].fillna(1) # otherwise yes

# looking at the pattern of associated 166s and 167s, I think 
# it's safe to impute the remaining (n=5) NAs in 168 as 1 

meyer[['w1q168_ei']] = meyer[['w1q168_ei']].fillna(1)

meyer.drop(columns = ['w1q166', 'w1q167', 'w1q168'], inplace = True)
meyer.shape

# let's back this guy up.  I'm getting nervous.
# meyer.to_csv('2024-06-05_most-imputation-done_midway-through-nativity.csv', index = False)

# let's back this guy up.  I'm getting nervous.
# meyer.to_csv('2024-06-05_all-imputation-except-poverty-done.csv', index = False)

# subset investigation
meyer[['w1poverty_i_ei']] = meyer[['w1poverty_i']].fillna(0)
meyer[['w1povertycat_i_ei']] = meyer[['w1povertycat_i']].fillna(4)

meyer.drop(columns = ['w1poverty_i', 'w1povertycat_i'], inplace = True)
meyer.shape

meyer.isna().sum().sum() # 0!

meyer.to_csv('2024-06-05_all-imputation-done.csv', index = False)

# Reorder the columns
ordered_cols = sorted(list(meyer.columns))
ordered_cols.remove('studyid')
ordered_cols = ['studyid'] + ordered_cols
len(ordered_cols) # 250

meyer = meyer[ordered_cols]
meyer.shape

meyer.to_csv('2024-06-05_all-imputation-done_reordered.csv', index = False)
