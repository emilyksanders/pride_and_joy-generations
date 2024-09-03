# Tuesday, June 4, 2024
# Imputation, Take 2

# Ok, so yesterday I made an excel spreadsheet list of all of NAs
# and decided what to do with them.  There are a bunch of different 
# methods (I chose what I thought was best for each type of data), 
# and I think the neatest way to handle all of them without making
# a giant mess is to break up the dataframe (include the ID in 
# each subset so that they can be cleanly re-merged), use a 
# real, official imputer, and then put it back together again.

# Oooh boy this could be dangerous.  I'd have to drop them from
# the original to avoid overwriting or otherwise losing stuff.
# Let me see what the shape is now.

# REMEMBER TO DROP THE STRAIGHTS! IT'S THE ONLY THING I NEED 
# FROM THE 2024-06-03 IMPUTATION SCRIPT!

meyer.shape # (1507, 267)
# So that it is the shape I want to get back at the end,
# minus any that I consciously, deliberately drop.


# lmao ok let's start by dropping

s = '''
w1q20_t_verb
w1q39_7
w1q39_12
w1q39_t_verb
w1q39_6
w1q39_5
w1q39_2
w1q39_3
w1q39_4
w1q39_1
w1q39_9
w1q39_8
w1q39_10
w1q39_11
gp1
gemployment2010
gmilesaway'''

print(s.replace('\n', '", "'))

drop_cols_3 = ["w1q20_t_verb", "w1q39_7", "w1q39_12", 
  "w1q39_t_verb", "w1q39_6", "w1q39_5", "w1q39_2", "w1q39_3", 
  "w1q39_4", "w1q39_1", "w1q39_9", "w1q39_8", "w1q39_10", 
  "w1q39_11", "gp1", "gemployment2010", "gmilesaway"]

len(drop_cols_3)

# Ok I started with 267 and dropped 17. Should now be 250.
meyer.drop(columns = drop_cols_3).shape # Yep, (1507, 250)!
meyer.drop(columns = drop_cols_3, inplace = True)
meyer.shape


# Alrighty! Now we're just imputing 0s!
# Then changing everything that's not 1 to 0.

s = '''
w1q145_3
w1q163_3
w1q136_3
w1q145_9
w1q143_3
w1q136_10
w1q145_10
w1q136_9
w1q163_10
w1q163_9
w1q143_9
w1q143_4
w1q136_6
w1q143_10
w1q143_5
w1q145_4
w1q136_5
w1q143_8
w1q163_5
w1q136_4
w1q163_6
w1q145_6
w1q136_1
w1q143_7
w1q163_1
w1q143_2
w1q143_1
w1q145_5
w1q143_6
w1q163_2
w1q163_4
w1q136_8
w1q145_8
w1q145_1
w1q145_7
w1q163_7
w1q136_2
w1q145_2
w1q139_3
w1q136_7
w1q139_9
w1q139_10
w1q139_5
w1q139_4
w1q139_8
w1q139_6
w1q139_2
w1q139_1
w1q139_7
w1q163_8
w1q141_3
w1q141_9
w1q141_10
w1q141_8
w1q141_4
w1q141_1
w1q141_5
w1q141_2
w1q141_7
w1q141_6'''


print(s.replace('\n', '", "'))

diy_ohe_part_1 = ["w1q145_3", "w1q163_3", "w1q136_3", "w1q145_9", 
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
  "w1q141_6"]

# Let me just check that these really are all 1s.

for i in diy_ohe_part_1:
  meyer[i].value_counts(dropna = False)

# Nope!  They're not! Ok let's combine them, screw it.
del diy_ohe_part_1

s = '''
w1q64_12
w1q64_5
w1q74_5
w1q74_6
w1q74_20
w1q64_11
w1q64_10
w1q74_18
w1q74_14
w1q74_17
w1q171_8
w1q30_3
w1q64_13
w1q64_7
w1q30_4
w1q171_6
w1q171_4
w1q64_8
w1q74_10
w1q74_21
w1q64_6
w1q74_11
w1q171_5
w1q64_3
w1q64_1
w1q171_9
w1q30_5
w1q171_3
w1q74_22
w1q64_9
w1q171_2
w1q171_7
w1q74_23
w1q64_4
w1q64_2
w1q30_1
w1q171_1
w1q30_2'''

print(s.replace('\n', '", "'))

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

sorted(value_list)[-1]-97 # = nan!

test = pd.DataFrame(sorted(value_list))-97
test[0].unique()

# This works!
# OK, here's the breakdown
# Subtract 97 from everything, because that's the designated expected-NA value
# 97-97=0, which is what I'm going to set the NAs to, so it's basically NA=NA
# NA-97 = NA, then I just need to fill the NAs
# some_number - 97 = some_other_number
# So now all I have to do is convert the remaining NAs to 0, 
# and then convert everything that's not 0 to 1.

# Let me check one more thing before proceeding.
i=diy_ohe[12]
for i in diy_ohe:
  if len(list(meyer[i].unique()))!=3:
    print(i)
    print(meyer[i].value_counts(dropna = False))
    print('='*20)
# The only ones printing out are ones where there are only *2* values
# the target one, and NaN.  We're good to proceed.

# I think the most efficient way to do this is probably with a .map()


diy_ohe_new = [''.join([x, '_ei']) for x in diy_ohe]

meyer.shape # (1507, 250)
len(diy_ohe) # 98
len(diy_ohe_new) # 98
meyer.loc[:, diy_ohe_new] = meyer.loc[:, diy_ohe].apply(lambda x: float(x)-97)
meyer.shape # (1507, 348) huzzah!

# check this again, should be no more 97s, but nothing else weird
value_list = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)

# Nope, it's all nans now

def nan_97_fixer(x):
  if float(x) == 97.0:
    x = np.nan
  else:
    x = x
  return x

meyer.loc[:, diy_ohe_new] = meyer.loc[:, diy_ohe].map(nan_97_fixer)

# check this again, should be no more 97s, but nothing else weird
value_list = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)

# Still all nans???????

# ok BASIC test
meyer.loc[:, diy_ohe_new] = meyer.loc[:, diy_ohe]

value_list = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)

# I just checked the original columns and they're fine.

# let me test this
pd.notna(98)

# try again

def nan_97_fixer(x):
  if pd.isna(x)==True:
    return 0
  else: # meaning it's NOT NA
    if float(x)==97.:
      return 0
    elif ((float(x)>0) & (float(x)<97)):
      return 1
    else:
      return 1_000_000_000

nan_97_fixer(5.) # it works.

meyer.loc[:, diy_ohe_new] = meyer.loc[:, diy_ohe].map(nan_97_fixer)

# check this again, should be no more 97s, but nothing else weird
value_list = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)

# oh ffs
meyer.loc[:, diy_ohe_new] = meyer.loc[:, diy_ohe].replace(97, np.nan)

# check this again, should be no more 97s, but nothing else weird
value_list = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list += a
value_list = list(set(value_list))
sorted(value_list)


# oh ffs
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe]==97, 0, meyer.loc[:, diy_ohe])

# check this again, should be no more 97s, but nothing else weird
value_list_2 = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list_2 += a
value_list_2 = list(set(value_list_2))
sorted(value_list_2)

[x for x in value_list if x not in value_list_2]  # 97
[x for x in value_list_2 if x not in value_list]  # 0

# OH THANK GOODNESS.  FINALLY!

# check this again because I'm losing my mind
meyer.shape

# ok!  on we go!
meyer[diy_ohe_new] = meyer[diy_ohe_new].fillna(0)

# should be short now!
value_list_3 = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list_3 += a
value_list_3 = list(set(value_list_3))
sorted(value_list_3)

# AHAAHAHAAAAA I'M SO EXCITED I'M HYPERVENTILATING!!!!!!!
meyer.loc[:, diy_ohe_new] = np.where(meyer.loc[:, diy_ohe_new]!=1, 0, meyer.loc[:, diy_ohe_new])

# one more time???
value_list_4 = []
for i in diy_ohe_new:
  a = list(meyer[i].unique())
  value_list_4 += a
value_list_4 = list(set(value_list_4))
sorted(value_list_4)

# YAAAAAAAAAAASSSSSSSSSSSS!!!!!

meyer.drop(columns = diy_ohe, inplace = True)
meyer.shape

# ok, I actually probably should have done this before dropping those columns
# but whatever, I can check it against the documentation
for i in diy_ohe_new:
  meyer[i].value_counts(dropna = False)
  print('='*20)
















