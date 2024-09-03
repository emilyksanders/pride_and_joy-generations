# June 3, 2024
# Imputation

# This is continuing some work I started last week.
# I have defined a dictionary full of columns that I
# want to combine one way or another.  I can't do that
# if they're full of NAs.  Imputing 0s would be the 
# easiest way to do it, but I don't want to introduce
# unreasonable amounts of error into my data.

# I'm going to use _ei to indicate "Emily imputed."
# The original authors used _i for their imputations.

# Last week I made a list of all the columns with 
# naturally occurring 0s in them. Today I want a 
# list of all remaining NAs.

pd.set_option('display.max_rows', None)
meyer.isna().sum().sort_values(ascending = False)

# Re-Import Data for clean copy
mey = pd.read_csv(
  './potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', 
  sep = '\t', low_memory=False, na_values = ' ') # Thanks to ibrahim rupawala for highlighting the na_values argument
  # https://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas/47105408#47105408

mey.shape
mey.columns = [c.lower() for c in list(mey.columns)]

# I am going to try to find related columns for logical 
# imputation if possible, or at least to justify 0s.
# (I'm going to try very hard not to get too derailed.)

# Friends of gmilesaway2
gmilesaway2 = mey[mey['gmilesaway2'].isna()]
gmilesaway2['w1q67'].value_counts(dropna = False)
mey['gmilesaway2'].groupby(mey['w1q67']).value_counts(dropna = False, normalize = True)
# w1q67  gmilesaway2
# 1.0    0.0            0.882353
#        1.0            0.094118
#        NaN            0.023529
# 2.0    0.0            0.838710
#        1.0            0.153226
#        NaN            0.008065
# 3.0    0.0            0.714844
#        1.0            0.273438
#        NaN            0.011719

mey['gmilesaway2'].groupby(mey['gurban']).value_counts(dropna = False, normalize = True)
# gurban  gmilesaway2
# 0.0     1.0            0.675824
#         0.0            0.313187
#         NaN            0.010989
# 1.0     0.0            0.801370
#         1.0            0.197108
#         NaN            0.001522

# It's actually not a very good assumption that they live
# more than 60 miles away. 73.5% of people live w/i 60m!
# And yet, most people have never gone.  
# I think the thing to impute here is a 0 under the original 
# meaning, that is, within 60 miles.


# OK ACTUALLY

# I've made a list of the NAs and I'm looking at THOSE
# for how to impute.  THAT'S what this next section is.

# w1q101
# subset investigation
s = mey.loc[cond, suicidal_idea_beh]
s = s[['w1q101',  'w1q105', 'w1q109', 'w1q118', 'w1q119', 'w1q121']]

# row condition
cond = mey['w1q101'].isna()

# column conditions
y1 = meyer[((meyer['w1q105'].notna()) & (meyer['w1q105']!=1))]
y2 = meyer[((meyer['w1q109'].notna()) & (meyer['w1q109']!=1))]
y3 = meyer[((meyer['w1q113'].notna()) & (meyer['w1q113']!=1))]

# In another pass I'd love to match the numbers
# but for now we're just going to impute "once."
# It is at least not overcounting.
meyer.loc[[(y1 | y2 | y3) & cond], 'w1q101'] = 2
len(meyer[y1])

# check these age columns
cond = mey['w1q102'].isna() # none!
cond = mey['w1q103'].isna()
# ok this would take forever. n<10 -> impute median
cond = mey['w1q112'].isna()
s = mey.loc[cond, suicidal_idea_beh]

# nssh
cond = mey['w1q119'].isna()
s = mey.loc[cond, suicidal_idea_beh]

# hey, is it just a few rows with a ton of missing data?
# I hate to lose data but if they truly didn't fill out anything...
meyer.iloc[10,:].isna().sum()
# oh right, there are all those OHE columns with planned missing
# so I need to start imputing first, then recheck these
# then decide whether to drop anything

# why are there straight people in here?
cond = mey['w1sexminid'].isna()
s = mey[cond]
s['w1sexualid']

# begone, straights!
meyer.shape # (1518, 267)
meyer = meyer[meyer['w1sexualid']!=1]
meyer.shape # (1507, 267)

# ugh I really wish I had done that before!!
# let's look at this again
pd.set_option('display.max_rows', None)
meyer.isna().sum().sort_values(ascending = False)



