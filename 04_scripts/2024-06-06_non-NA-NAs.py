# Thursday, June 6, 2024
# "Imputation" of non-NA NAs (97s, etc.)

# Wait, why did I make problem_children a list rather than a dictionary?

s = """
('w1q01_ei', [98]), ('w1q02_ei', [98]), 
  ('w1q33_ei', [97]), ('w1q34_ei', [97]), ('w1q35_ei', [97]), 
  ('w1q36_ei', [97]), ('w1q45_ei', [98, 99]), ('w1q46_ei', [98, 99]), 
  ('w1q47_ei', [98, 99]), ('w1q48_ei', [98, 99]), ('w1q49_ei', [98, 99]), 
  ('w1q50_ei', [98, 99]), ('w1q51_ei', [98, 99]), ('w1q89_ei', [7]), 
  ('w1q102_ei', [97]), ('w1q103_ei', [97]), ('w1q104_ei', [97]), 
  ('w1q106_ei', [97]), ('w1q107_ei', [97]), ('w1q108_ei', [97]),
  ('w1q110_ei', [97]), ('w1q111_ei', [0, 97]), ('w1q112_ei', [97]),
  ('w1q114_ei', [6, 7, 8, 9, 97]), ('w1q115_ei', [97]), ('w1q116_ei', [97]),
  ('w1q117_ei', [97]), ('w1q120_ei', [97]), ('w1q121_ei', [97]),
  ('w1q122_ei', [97]), ('w1q123a_ei', [5]), ('w1q123b_ei', [5]), 
  ('w1q123c_ei', [5]), ('w1q123d_ei', [5]), ('w1q134_ei', [97]), 
  ('w1q168_ei', [97]), ('w1q136_10_ei', [7, 97]), ('w1q136_1_ei', [7, 97]), 
  ('w1q136_2_ei', [7, 97]), ('w1q136_3_ei', [7, 97]), 
  ('w1q136_4_ei', [7, 97]), ('w1q136_5_ei', [7, 97]), 
  ('w1q136_6_ei', [7, 97]), ('w1q136_7_ei', [7, 97]), 
  ('w1q136_8_ei', [7, 97]), ('w1q136_9_ei', [7, 97]), 
  ('w1q139_10_ei', [7, 97]), ('w1q139_1_ei', [7, 97]), 
  ('w1q139_2_ei', [7, 97]), ('w1q139_3_ei', [7, 97]), 
  ('w1q139_4_ei', [7, 97]), ('w1q139_5_ei', [7, 97]), 
  ('w1q139_6_ei', [7, 97]), ('w1q139_7_ei', [7, 97]), 
  ('w1q139_8_ei', [7, 97]), ('w1q139_9_ei', [7, 97]), 
  ('w1q141_10_ei', [7, 97]), ('w1q141_1_ei', [7, 97]), 
  ('w1q141_2_ei', [7, 97]), ('w1q141_3_ei', [7, 97]), 
  ('w1q141_4_ei', [7, 97]), ('w1q141_5_ei', [7, 97]), 
  ('w1q141_6_ei', [7, 97]), ('w1q141_7_ei', [7, 97]), 
  ('w1q141_8_ei', [7, 97]), ('w1q141_9_ei', [7, 97]), 
  ('w1q143_10_ei', [7, 97]), ('w1q143_1_ei', [7, 97]), 
  ('w1q143_2_ei', [7, 97]), ('w1q143_3_ei', [7, 97]), 
  ('w1q143_4_ei', [7, 97]), ('w1q143_5_ei', [7, 97]), 
  ('w1q143_6_ei', [7, 97]), ('w1q143_7_ei', [7, 97]), 
  ('w1q143_8_ei', [7, 97]), ('w1q143_9_ei', [7, 97]), 
  ('w1q145_10_ei', [7, 97]), ('w1q145_1_ei', [7, 97]), 
  ('w1q145_2_ei', [7, 97]), ('w1q145_3_ei', [7, 97]), 
  ('w1q145_4_ei', [7, 97]), ('w1q145_5_ei', [7, 97]), 
  ('w1q145_6_ei', [7, 97]), ('w1q145_7_ei', [7, 97]), 
  ('w1q145_8_ei', [7, 97]), ('w1q145_9_ei', [7, 97]), 
  ('w1q163_10_ei', [7, 97]), ('w1q163_1_ei', [7, 97]), 
  ('w1q163_2_ei', [7, 97]), ('w1q163_3_ei', [7, 97]), 
  ('w1q163_4_ei', [7, 97]), ('w1q163_5_ei', [7, 97]), 
  ('w1q163_6_ei', [7, 97]), ('w1q163_7_ei', [7, 97]), 
  ('w1q163_8_ei', [7, 97]), ('w1q163_9_ei', [7, 97])"""
  
d = s.replace("(", "").replace(")", "").replace("', [", "': [").replace(' \n', '').replace('\n', '')
d

# w1q120 is the only one without an _ei
problem_children = {'w1q01_ei': [98], 'w1q02_ei': [98],  'w1q33_ei': [97], 
  'w1q34_ei': [97], 'w1q35_ei': [97],  'w1q36_ei': [97], 'w1q45_ei': [98, 99], 
  'w1q46_ei': [98, 99],  'w1q47_ei': [98, 99], 'w1q48_ei': [98, 99], 
  'w1q49_ei': [98, 99],  'w1q50_ei': [98, 99], 'w1q51_ei': [98, 99], 
  'w1q89_ei': [7],  'w1q102_ei': [97], 'w1q103_ei': [97], 'w1q104_ei': [97],  
  'w1q106_ei': [97], 'w1q107_ei': [97], 'w1q108_ei': [97],  'w1q110_ei': [97], 
  'w1q111_ei': [0, 97], 'w1q112_ei': [97],  'w1q114_ei': [6, 7, 8, 9, 97], 
  'w1q115_ei': [97], 'w1q116_ei': [97],  'w1q117_ei': [97], 'w1q120': [97], 
  'w1q121_ei': [97],  'w1q122_ei': [97], 'w1q123a_ei': [5], 'w1q123b_ei': [5],  
  'w1q123c_ei': [5], 'w1q123d_ei': [5], 'w1q134_ei': [97],  'w1q168_ei': [97], 
  'w1q136_10_ei': [7, 97], 'w1q136_1_ei': [7, 97],  'w1q136_2_ei': [7, 97], 
  'w1q136_3_ei': [7, 97],  'w1q136_4_ei': [7, 97], 'w1q136_5_ei': [7, 97],  
  'w1q136_6_ei': [7, 97], 'w1q136_7_ei': [7, 97],  'w1q136_8_ei': [7, 97], 
  'w1q136_9_ei': [7, 97],  'w1q139_10_ei': [7, 97], 'w1q139_1_ei': [7, 97],  
  'w1q139_2_ei': [7, 97], 'w1q139_3_ei': [7, 97],  'w1q139_4_ei': [7, 97], 
  'w1q139_5_ei': [7, 97],  'w1q139_6_ei': [7, 97], 'w1q139_7_ei': [7, 97],  
  'w1q139_8_ei': [7, 97], 'w1q139_9_ei': [7, 97],  'w1q141_10_ei': [7, 97], 
  'w1q141_1_ei': [7, 97],  'w1q141_2_ei': [7, 97], 'w1q141_3_ei': [7, 97],  
  'w1q141_4_ei': [7, 97], 'w1q141_5_ei': [7, 97],  'w1q141_6_ei': [7, 97], 
  'w1q141_7_ei': [7, 97],  'w1q141_8_ei': [7, 97], 'w1q141_9_ei': [7, 97],  
  'w1q143_10_ei': [7, 97], 'w1q143_1_ei': [7, 97],  'w1q143_2_ei': [7, 97], 
  'w1q143_3_ei': [7, 97],  'w1q143_4_ei': [7, 97], 'w1q143_5_ei': [7, 97],  
  'w1q143_6_ei': [7, 97], 'w1q143_7_ei': [7, 97],  'w1q143_8_ei': [7, 97], 
  'w1q143_9_ei': [7, 97],  'w1q145_10_ei': [7, 97], 'w1q145_1_ei': [7, 97],  
  'w1q145_2_ei': [7, 97], 'w1q145_3_ei': [7, 97],  'w1q145_4_ei': [7, 97], 
  'w1q145_5_ei': [7, 97],  'w1q145_6_ei': [7, 97], 'w1q145_7_ei': [7, 97],  
  'w1q145_8_ei': [7, 97], 'w1q145_9_ei': [7, 97],  'w1q163_10_ei': [7, 97], 
  'w1q163_1_ei': [7, 97],  'w1q163_2_ei': [7, 97], 'w1q163_3_ei': [7, 97],  
  'w1q163_4_ei': [7, 97], 'w1q163_5_ei': [7, 97],  'w1q163_6_ei': [7, 97], 
  'w1q163_7_ei': [7, 97],  'w1q163_8_ei': [7, 97], 'w1q163_9_ei': [7, 97]}

# # testing syntax to make sure I understand it
# for i in ['cat', 'dog', 'bird', 'goose', 'ostrich', 'oliphaunt']:
#   for j in i:
#     if j != 'o':
#       print(j)
#       break
#   print(f'finished {i}')

column_jail = []
for c, v in problem_children.items():
  a = list(meyer[c].unique())
  for i in v:
    if i in a:
      column_jail.append((c, v, i))
      break

for i in column_jail:
  if i[0]=='w1q02_ei':
    continue
  meyer[i[0]].value_counts(dropna = False)
  meyer[i[0]].value_counts(dropna = False, normalize = True)
  print('')
  print('='*20)
  print('')

# Here are the remaining values, and what I intend to do about them.

# [('w1q01_ei', [98], 98), 98.0      2      0.001327
# For only 2 values, imputing the median seems fine.

# Because I *already* imputed values, RE-fitting the si may well end up with a DIFFERENT 
# median.  If I have time, I should just go back and skip si, and instead use .fillna() 
# to put in the POPULATED median, which is provided in the documentation (and I could 
# easily verify myself).  I'm not going to take the time NOW to go back and change all 
# that, but I am going to do it for these 2 values.
cond = meyer['w1q01_ei']==98.0
meyer.loc[cond, 'w1q01_ei']=7

# ('w1q02_ei', [98], 98), 98.0     48    0.031851
# I'm just going to drop this column. I've done SO MUCH imputation and it's really making
#  me nervous.  I'm not planning to really hone in deep on optimism for the future or 
# whatever (THIS TIME), so I'm just going to chuck it for now.
meyer.drop(columns = 'w1q02_ei', inplace = True)

# ('w1q33_ei', [97], 97), 
# The Q is how long someone's been with their partner, and the 97s are people who said
# they don't have partners.  The logical imputation is 0.  There are no natural 0s.
cond = meyer['w1q33_ei']==97.0
meyer.loc[cond, 'w1q33_ei']=0


# ('w1q89_ei', [7], 7), 
# This is the question about how often people smoke cigarettes, and the 7s are people
# who said on the previous question that they do not smoke (or failed to answer the 
# question, whom I (think I) imputed as no). Therefore, I'll impute "not at all" here.
cond = meyer['w1q89_ei']==7.0
meyer.loc[cond, 'w1q89_ei']=3


# ('w1q111_ei', [0, 97], 0), 
# Ok, truly F these age-when columns.  They are way too complicated to get into in the 
# time I have.  They're colinear(ish) with the current-age column, or at least not
# independent.  It is not possible for a 19 year old person to have made their first
# suicide attempt at 25.  Plus, I highly doubt the relationship between age of attempt(s)
# and overall mental health is linear.  I'd be way more worried about someone who made 
# their first suicide attempt at 11 OR at 35 than I would be about someone who made their
# first attempt at 19.  A lot of people have suicidal ideation in their late teens/early
# 20s, because they're old enough to feel the weight of the world but not old enough for 
# their brains to be done cooking.  I'd have to do a ton of research and reading to be sure
# (and I don't have time for that either), but my intuition says it's probably a parabolic
# relationship between the age of attempt and the redness of the flag.  PLUS, imputating
# these guys has been the bane of my existence for over a week.  I think what I did already
# was impute the missings and 97s as 0s, but now I'm thinking that was a bad idea!  A true
# value of 0 (if it were even psychologically possible, which it isn't - I HIGHLY doubt a
# baby can understand the concept of suicide well enough to have suicidal ideation, but
# even if they did, there's no way that person would remember it as an adult), would be 
# EXTREMELY alarming, in a way that a linear model is just not equipped to deal with.  
# Furthermore, getting back to the point about the curvilinear nature of this, I don't think
# there's really ANY good value to impute here!  If one wanted to look at age effects, one 
# would really have to limit the sample to people who have made attempts.  

# I also considered a scheme wherein I would subtract the min age from the max age to get a 
# range of time that they were suicidal, and if the min and max were both populated but
# neither was 0 (i.e., they made multiple attempts at the same age) I would sub in a 1 (for
# that 1 year of suicidality), and if one or the other (but not both!) was 0, or they only 
# answered the "how old were you?" question (i.e., they indicated that they'd only made one 
# attempt), I would also sub in 1, for that 1 year where they were feeling that way, but if
# neither was populated or they were both 0 or whatever (i.e., for people who made no 
# attempts ever) I would keep a 0 - so it'd be 0 for people who never attempted, and a 
# minimum of 1 for people who did ever attempt - but in addition to being way too complicated
# and messy for the amount of time I have left, that runs the risk of dramatically 
# misrepresenting people's actual relationship with suicidality.  Someone who made one attempt
# at 17 because of teen stuff and another, more or less completely unrelated, attempt at 47 
# because they were going through a messy divorce would be indicated to have been suicidal 
# for THIRTY YEARS, which isn't true, and would make it look like they were 6x more impacted 
# by sucidality than someone who made their first attempt 18 at their last attempt at 23, 
# even if the latter person made 20 attempts in that time, and they were all due to the same
# ongoing issues.  I know I'm probably overthinking this, but to do a range seems so reductive
# as to be practically meaningless - and definitely not worth the time, effort, and 
# dimensionality it would take to accomplish it.  I am going to just drop these age columns.
age_cols = ['w1q102_ei', 'w1q103_ei', 'w1q104_ei',  # these are the suicide/nssh age Qs
  'w1q106_ei', 'w1q107_ei', 'w1q108_ei', 'w1q110_ei', 'w1q111_ei', 'w1q112_ei', 
  'w1q115_ei', 'w1q116_ei', 'w1q117_ei', 'w1q120', 'w1q121_ei', 'w1q122_ei',
  'w1q134_ei']  # this how old were you when you got conversion therapy 
len(age_cols)
meyer.drop(columns = age_cols, inplace = True)


# ('w1q114_ei', [6, 7, 8, 9, 97], 6), 
# This is the one asking how many suicide attempts people made, and they used a messy scale.
# I get why they did it, I probably would have done the same, but it still makes it ordinal
# rather than truly linear.  I could leave it as is, or change these values to the minimum
# in their range (or something like that).  I could also make it categorical, like
# 0 attempts, 1 attempt, multiple attempts.
np.linspace(6, 21, 4) # oh it's exactly what they have.

# I'm going to make columns for all of those options and see which one correlates best.
# Oh wait no I'm not!  All I'm doing with these is adding them up into a composite score.
# I'm going to reassign those values to the minimum value in their range so that it's 
# sort of linear, but then that's enough.  That's fine.
cond7 = meyer['w1q114_ei']==7.0
meyer.loc[cond7, 'w1q114_ei']=11

cond8 = meyer['w1q114_ei']==8.0
meyer.loc[cond8, 'w1q114_ei']=16

cond9 = meyer['w1q114_ei']==9.0
meyer.loc[cond9, 'w1q114_ei']=21


# All of the 123 questions are about outness, but they're coded weird. It's are you out to...
# 1 = All, 2 = Most, 3 = Some, 4 = None, 5 = don't know/does not apply/[missing value]
# So firstly, it's counter-intuitive.  Higher numbers = less out.  Sort of.  Secondly, 5 is
# in a weird place on the scale  I think I'm going to recode it like this:
# 4 -> 0 = I can confidently say I am out to "None" of these people. (LOWEST OUTNESS)
# 5 -> 1 = I'm being wishy-washy about how out I am to these people.
# 3 -> 2 = Some
# 2 -> 3 = Most
# 1 -> 4 = All (HIGHEST OUTNESS)
# ('w1q123a_ei', [5], 5), ('w1q123b_ei', [5], 5), ('w1q123c_ei', [5], 5), ('w1q123d_ei', [5], 5)]

meyer[['w1q123a_ei_r', 'w1q123b_ei_r', 'w1q123c_ei_r', 'w1q123d_ei_r']] = meyer[[
  'w1q123a_ei', 'w1q123b_ei', 'w1q123c_ei', 'w1q123d_ei']]

recode_123s = {4: 0, 5: 1, 3: 2, 2: 3, 1: 4}

old_cols = ['w1q123a_ei', 'w1q123b_ei', 'w1q123c_ei', 'w1q123d_ei']
new_cols = ['w1q123a_ei_r', 'w1q123b_ei_r', 'w1q123c_ei_r', 'w1q123d_ei_r']

for old, new in list(zip(old_cols, new_cols)):
  meyer[new] = meyer[old].map(recode_123s)

check = meyer[['w1q123a_ei', 'w1q123a_ei_r', 'w1q123b_ei', 'w1q123b_ei_r', 
  'w1q123c_ei', 'w1q123c_ei_r', 'w1q123d_ei', 'w1q123d_ei_r']]
# Yeah checks out!

meyer.drop(columns = old_cols, inplace = True)
meyer.shape


# I don't remember if I actually *executed* all that code, so let me test it again. I reran 
# the code to define problem_children just to be safe, and now I'm going to modify the loop.
column_jail = []
columns_done = []
z = 0 # I'm a little hazy on `continue` so this is just a check
for c, v in problem_children.items():

  # if that column name isn't in the list, find out why
  if c not in list(meyer.columns):
    if c=='w1q02_ei':
      columns_done.append(c)
      z+=1
      continue
  
    elif c in age_cols:
      columns_done.append(c)
      z+=1
      continue
    
    # if neither of those work, try renaming it
    c_r = ''.join([c, '_r'])
    if c_r not in list(meyer.columns):
      print(c)
      columns_done.append(c)
      z+=1
      continue
    elif c_r in list(meyer.columns): 
      c = c_r # rename it and continue thru the loop

  # if that column name is in the list, or if c_r is, do this
  a = list(meyer[c].unique())
  for i in v:
    if i in a:
      column_jail.append((c, v, i))
      break
  columns_done.append(c)
  z+=1
z==len(problem_children.keys())

# huh = [c for c in list((problem_children.keys())) if c not in columns_done]
# fixed it ^

column_jail
# oh it's just [('w1q114_ei', [6, 7, 8, 9, 97], 6)]
meyer['w1q114_ei'].value_counts(dropna = False)
# w1q114_ei
# 0.0     1146
# 1.0      251
# 3.0       32
# 2.0       30
# 6.0       17
# 4.0       14
# 5.0        9
# 11.0       6
# 16.0       1
# 21.0       1
# Name: count, dtype: int64

# it's totally fine, I fixed the thing I wanted to fix with 6+
# I should probably indicate that I changed stuff though.

meyer.shape # (1507, 233)
meyer[['w1q114_ei_r']] = meyer[['w1q114_ei']]
meyer.shape
meyer.drop(columns = ['w1q114_ei'], inplace = True)
meyer.shape


# ok!  Woohoo!  Let's save another copy.
meyer.to_csv('2024-06-06_non-NA-NAs-fixed.csv', index = False)






