jup = pd.read_csv('dsb318-capstone/02_data/df_after_data_preparation_part_2.csv')
rad = pd.read_csv('2024-06-07_h21-m19-s52_end-of-day_ISH_minus_sqrt_for_testing.csv')

jup.shape
rad.shape

sum(jup.index!=rad.index)
sum(jup.columns!=rad.columns)

jup.isna().sum().sum()
rad.isna().sum().sum()

# column 32 was the first discrepancy; it is now resolved
# np.where(jup.columns!=rad.columns)
# jup.columns[97]
# rad.columns[97]
# sum(jup['w1q32']!=rad['w1q32_ei'])

troublemakers = []
for i in list(rad.columns):
  if list(jup[i])!=list(rad[i]):
    # print(i)
    troublemakers.append(i)

c = ['studyid', 'original', 'jupyter']
for i in troublemakers:
  print(f"""
subset = rad[['studyid', '{i}']].merge(
  jup[['studyid', '{i}']], on = 'studyid', how = 'left')
subset.columns = c
test_{i} = subset.copy(deep = True)
  """)


subset = rad[['studyid', 'suicidality']].merge(
  jup[['studyid', 'suicidality']], on = 'studyid', how = 'left')
subset.columns = c
test_suicidality = subset.copy(deep = True)

subset = rad[['studyid', 'w1connectedness_i']].merge(
  jup[['studyid', 'w1connectedness_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1connectedness_i = subset.copy(deep = True)

subset = rad[['studyid', 'w1everyday_i']].merge(
  jup[['studyid', 'w1everyday_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1everyday_i = subset.copy(deep = True)

subset = rad[['studyid', 'w1feltstigma_i']].merge(
  jup[['studyid', 'w1feltstigma_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1feltstigma_i = subset.copy(deep = True)

subset = rad[['studyid', 'w1idcentral_i']].merge(
  jup[['studyid', 'w1idcentral_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1idcentral_i = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1internalized_i']].merge(
  jup[['studyid', 'w1internalized_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1internalized_i = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1lifesat_i']].merge(
  jup[['studyid', 'w1lifesat_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1lifesat_i = subset.copy(deep = True)

subset = rad[['studyid', 'w1meim_i']].merge(
  jup[['studyid', 'w1meim_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1meim_i = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1q119_ei']].merge(
  jup[['studyid', 'w1q119_ei']], on = 'studyid', how = 'left')
subset.columns = c
test_w1q119_ei = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1q34_ei']].merge(
  jup[['studyid', 'w1q34_ei']], on = 'studyid', how = 'left')
subset.columns = c
test_w1q34_ei = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1socialwb_i']].merge(
  jup[['studyid', 'w1socialwb_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1socialwb_i = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1socsupport_i']].merge(
  jup[['studyid', 'w1socsupport_i']], on = 'studyid', how = 'left')
subset.columns = c
test_w1socsupport_i = subset.copy(deep = True)
  
subset = rad[['studyid', 'w1weight_full']].merge(
  jup[['studyid', 'w1weight_full']], on = 'studyid', how = 'left')
subset.columns = c
test_w1weight_full = subset.copy(deep = True)



for i in troublemakers:
  print(f"np.where(test_{i}['original']!=test_{i}['jupyter'])")
  print('')

np.where(test_suicidality['original']!=test_suicidality['jupyter'])
np.where(test_w1connectedness_i['original']!=test_w1connectedness_i['jupyter'])
np.where(test_w1everyday_i['original']!=test_w1everyday_i['jupyter'])
np.where(test_w1feltstigma_i['original']!=test_w1feltstigma_i['jupyter'])
np.where(test_w1idcentral_i['original']!=test_w1idcentral_i['jupyter'])
np.where(test_w1internalized_i['original']!=test_w1internalized_i['jupyter'])
np.where(test_w1lifesat_i['original']!=test_w1lifesat_i['jupyter'])
np.where(test_w1meim_i['original']!=test_w1meim_i['jupyter'])
np.where(test_w1q119_ei['original']!=test_w1q119_ei['jupyter'])
np.where(test_w1q34_ei['original']!=test_w1q34_ei['jupyter'])
np.where(test_w1socialwb_i['original']!=test_w1socialwb_i['jupyter'])
np.where(test_w1socsupport_i['original']!=test_w1socsupport_i['jupyter'])
np.where(test_w1weight_full['original']!=test_w1weight_full['jupyter'])

for i in troublemakers:
  print(f"test_{i}['diff'] = test_{i}['original'] - test_{i}['jupyter']")

test_suicidality['diff'] = test_suicidality['original'] - test_suicidality['jupyter']
test_w1connectedness_i['diff'] = test_w1connectedness_i['original'] - test_w1connectedness_i['jupyter']
test_w1everyday_i['diff'] = test_w1everyday_i['original'] - test_w1everyday_i['jupyter']
test_w1feltstigma_i['diff'] = test_w1feltstigma_i['original'] - test_w1feltstigma_i['jupyter']
test_w1idcentral_i['diff'] = test_w1idcentral_i['original'] - test_w1idcentral_i['jupyter']
test_w1internalized_i['diff'] = test_w1internalized_i['original'] - test_w1internalized_i['jupyter']
test_w1lifesat_i['diff'] = test_w1lifesat_i['original'] - test_w1lifesat_i['jupyter']
test_w1meim_i['diff'] = test_w1meim_i['original'] - test_w1meim_i['jupyter']
test_w1q119_ei['diff'] = test_w1q119_ei['original'] - test_w1q119_ei['jupyter']
test_w1q34_ei['diff'] = test_w1q34_ei['original'] - test_w1q34_ei['jupyter']
test_w1socialwb_i['diff'] = test_w1socialwb_i['original'] - test_w1socialwb_i['jupyter']
test_w1socsupport_i['diff'] = test_w1socsupport_i['original'] - test_w1socsupport_i['jupyter']
test_w1weight_full['diff'] = test_w1weight_full['original'] - test_w1weight_full['jupyter']

for i in troublemakers:
  print(f"test_{i}['diff'].value_counts(dropna = False)")

test_suicidality['diff'].value_counts(dropna = False)
test_w1connectedness_i['diff'].value_counts(dropna = False)
test_w1everyday_i['diff'].value_counts(dropna = False)
test_w1feltstigma_i['diff'].value_counts(dropna = False)
test_w1idcentral_i['diff'].value_counts(dropna = False)
test_w1internalized_i['diff'].value_counts(dropna = False)
test_w1lifesat_i['diff'].value_counts(dropna = False)
test_w1meim_i['diff'].value_counts(dropna = False)
test_w1q119_ei['diff'].value_counts(dropna = False)
test_w1q34_ei['diff'].value_counts(dropna = False)
test_w1socialwb_i['diff'].value_counts(dropna = False)
test_w1socsupport_i['diff'].value_counts(dropna = False)
# test_w1weight_full['diff'].value_counts(dropna = False)
test_w1weight_full['diff'].describe()

# # WHAT IS THE PROBLEM
# suicidality         | 1 cell was imputed better |
# w1connectedness_i   | rounding error            |
# w1everyday_i        | rounding error            |
# w1feltstigma_i      | rounding error            |
# w1idcentral_i       | rounding error            |
# w1internalized_i    | rounding error            |
# w1lifesat_i         | rounding error            |
# w1meim_i            | rounding error            |
# w1q119_ei           | 16 NAs imputed to 1 in J rather than 0 in R (improvement)  |
# w1q34_ei            | 579 7s imputed in Jupyter (improvement) |
# w1socialwb_i        | rounding error            |
# w1socsupport_i      | rounding error            |
# w1weight_full       | rounding error            |


joe = meyer_orig[meyer_orig['STUDYID']==159917392]
joe = joe[['W1Q101', 'W1Q105', 'W1Q109', 'W1Q113', 'W1Q114']]

joe_jup = jup.loc[jup['studyid']==159917392, 'suicidality']


# Is the y1 y2 y3 logic ok?
# jup is what this file was a minute ago.  jup2 is when i reran it with that logic
jup2 = pd.read_csv('dsb318-capstone/02_data/df_after_data_preparation_part_2.csv')

jup.shape
jup2.shape

sum(jup.index!=jup2.index)
sum(jup.columns!=jup2.columns)

jup.isna().sum().sum()
jup2.isna().sum().sum()

# column 32 was the first discrepancy; it is now resolved
# np.where(jup.columns!=rad.columns)
# jup.columns[97]
# rad.columns[97]
# sum(jup['w1q32']!=rad['w1q32_ei'])

troublemakers = []
for i in list(jup2.columns):
  if list(jup[i])!=list(jup2[i]):
    print(i)
    #troublemakers.append(i)

subset = jup2[['studyid', 'suicidality']].merge(
  jup[['studyid', 'suicidality']], on = 'studyid', how = 'left')
subset.columns = ['studyid', 'jup2', 'jup']
test_suicidality2 = subset.copy(deep = True)

np.where(test_suicidality2['jup2']!=test_suicidality2['jup'])

x = test_suicidality2.iloc[[ 920, 1422],:]




