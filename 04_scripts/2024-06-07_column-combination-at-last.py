# Friday, June 7, 2024
# Feature Engineering!  Whoo!

# In this script, I will finally execute my feat_eng_dict to create
# composite score columns and drop the individual parts.

# I want to look at the values in each variable and triple check 
# that they're ready to go and that the method is appropriate.
for k, v in feat_eng_dict.items():
  print('='*20)
  print(f'{k}: {v[0]}')
  print('-'*20)
  for i in v[1:]:
    if i not in list(meyer.columns):
      print(f'{i} not in columns')
    else:
      # print(f'Dtype: {meyer[[i]].dytpe}')
      meyer[i].value_counts(dropna = False).sort_index()
    print('-'*20)
  print('='*20, '\n'*2)
# All good!

# Now I want to see a list of all the methods of combination.
methods = []
for v in feat_eng_dict.values():
  if v[0] not in methods:
    methods.append(v[0])
methods

# I still have binarize, mean, and sum, but I think I already
# binarized the individual columns that will go into those
# binarized composite scores, meaning that taking the mean
# would accomplish the same thing.
for k, v in feat_eng_dict.items():
  if v[0]!='binarize':
    continue
  print('='*20)
  print(f'{k}: {v[0]}')
  print('-'*20)
  for i in v[1:]:
    if i not in list(meyer.columns):
      print(f'{i} not in columns')
    else:
      # print(f'Dtype: {meyer[[i]].dytpe}')
      meyer[i].value_counts(dropna = False).sort_index()
    print('-'*20)
  print('='*20, '\n'*2)
# Huzzah!  Yes!  I'm going to change those to means.


# Ok let's run this bad boy!!
# (I'm so freaking excited I'm so proud of myself for 
# coming up with this and I'm so clever)

meyer.shape # (1494, 228)
cols_added = 0
cols_done = []
for k, v in feat_eng_dict.items():
  # print('')
  # print(k)
  meyer[k] = meyer[v[1]]
  cols_done.append(v[1])
  cols_added += 1
  for i in v[2:]:
    # print('doing the sum')
    meyer[k] += meyer[i]
    cols_done.append(i)
  if v[0]=='mean':
    # print('doing the mean')
    meyer[k] = meyer[k]/len(v[1:])
  elif v[0]=='binarize': 
    # print('binarizing')
    meyer[k] = np.where(meyer[k]>1, 1, meyer[k])
  
cols_added + 228 # 253
meyer.shape # (1494, 253)
len(cols_done) # 121

# These aren't showing as correct
meyer['check_disabled'] = (meyer['w1q75_ei_r'] + meyer['w1q76_ei_r'])
meyer.loc[(meyer['check_disabled']==2), 'check_disabled'] = 1 # = np.round((meyer['check_disabled']/2), 0)
sum((meyer['check_disabled']-meyer['disabled'])!=0)
sum(meyer['check_disabled']!=meyer['disabled'])

# This works fine
meyer['check_disabled'] += meyer['studyid']

# let me see
test = meyer[['disabled', 'check_disabled']]
meyer['disabled'].describe()

# Ooooh cool cool cool, I just hadn't re-run the dictionary since 
# changing the 'binarize's to 'mean's, so the if statement wasn't 
# always getting triggered.  It's fine.  Let me check others.

# Also though, what was I thinking?  The mean of 0s and 1s isn't a 
# binary, it's a float.  So I need to change those back, edit the 
# code, and rerun it anyway.  
# I'm going to go back up and do that in place.
# Let me see how many bogus columns I've added though.
meyer.shape
# meyer.drop(columns = ['check_suicidality', ])
# Eh actually I'll just reimport the CSV.

# that all works upon re-running. 

# just a sum
meyer['check_suicidality'] = (meyer['w1q101_ei_r'] + meyer['w1q105_ei_r'] + meyer['w1q109_ei_r'] + meyer['w1q114_ei_r'])
meyer['check_suicidality']==meyer['suicidality']
(meyer['check_suicidality']-meyer['suicidality'])==0
# visually it looks like all Trues.  Let me see

sum(meyer['check_suicidality']!=meyer['suicidality'])
sum((meyer['check_suicidality']-meyer['suicidality'])!=0)
# both 0s!  huzzah!  
# this worked before, but upon rerunning, now it doesn't!
check = meyer.loc[(meyer['check_suicidality']!=meyer['suicidality']), ['w1q101_ei_r', 'w1q105_ei_r', 'w1q109_ei_r', 'w1q114_ei_r', 'suicidality', 'check_suicidality']]
check_index = list(check.index)
check_2 = meyer.loc[check_index, ['w1q101_ei_r', 'w1q105_ei_r', 'w1q109_ei_r', 'w1q114_ei_r', 'suicidality', 'check_suicidality']]
# ok now it works sometimes?????

# actually a mean
meyer['check_outness'] = (meyer['w1q123a_ei_r'] + meyer[
  'w1q123b_ei_r'] + meyer['w1q123c_ei_r'] + meyer[
    'w1q123d_ei_r'] + meyer['w1q124_ei_r'])/len([
      'mean', 'w1q123a_ei_r', 'w1q123b_ei_r', 'w1q123c_ei_r', 
      'w1q123d_ei_r', 'w1q124_ei_r'][1:])
meyer['check_outness']==meyer['outness']
(meyer['check_outness']-meyer['outness'])==0
# visually it looks like all Trues.  Let me see

sum(meyer['check_outness']!=meyer['outness'])
sum((meyer['check_outness']-meyer['outness'])!=0)

6!=4
# ok seems fine!
 
 
# save a backup
meyer.to_csv(f'{my_date()}_column-combination-done_no-drops_not-reordered_FIXED.csv', index = False)

# drop the component columns
cols_done.append('check_outness')
cols_done.append('check_suicidality')
cols_done.append('check_disabled')
228-121+25
meyer.drop(columns = cols_done).shape # goal is 132
meyer.drop(columns = cols_done, inplace = True)

ordered_cols = sorted(list(meyer.columns))
ordered_cols.remove('studyid')
ordered_cols.remove('kessler6_sqrt')
ordered_cols.remove('w1kessler6_i')
ordered_cols = ['studyid', 'w1kessler6_i', 'kessler6_sqrt'] + ordered_cols
ordered_cols

len(ordered_cols) # 132
meyer.shape # (1494, 132)

meyer = meyer[ordered_cols]
meyer.shape

# save again
meyer.to_csv(f'{my_date()}_column-combination-done_drops-done_reordered_FIXED.csv', index = False)




