# 5/23/24

# check out this dataset from Ilan Meyer, my beloved

# Import Data
meyer = pd.read_csv('./potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', sep = '\t', low_memory=False)
meyer.shape #(1518, 1329), but we can cut that down.
og_columns = list(meyer.columns)

# for RIGHT NOW, I think I'm only going to look at wave 1
# the wave stuff is REALLY COOL, but i don't think I understand
# time series well enough to get into it for this project
# if I get a model working based on wave 1, and write it up
# and all that "good enough," then I'll come back and add 
# some time series stuff
# oh it can even just be another phase of the project!
# no need to replace anything!  just section B.

meyer['WAVEPARTICIPATED'].value_counts(dropna =False)
# matches what's in the documentation

# ok, so, for now, I am going to drop all the variables marked W2 and W3.  
cols = list(meyer.columns)
w1_cols = [c for c in cols if c[:2]!='W2']
w1_cols = [c for c in w1_cols if c[:2]!='W3']
len(w1_cols)

# drop columns
meyer = meyer[w1_cols]
meyer.shape

# NAs?
meyer.isna().sum().sum()
# it says 0, but it's not 0
# they must have imputed it with an empty string or something
# when I do .value_counts(), a lot of columns have a blank row, e.g.,
#                      14
# where there absolutely should not be a blank.
# so that's fun!  gonna have to clean that up!

# i originally thought they only included the base variables
# and I would have to compute the scale scores myself, but
# OMG THEY DID INCLUDE THE CALC'D SCALES!!!!!!
# I JUST COULDN'T FIND THEM BECAUSE ALL CAPS!!

meyer.columns = [c.lower() for c in list(meyer.columns)]

# GOAL: drop the columns that contributed to combination scores

# Make lists of the items that comprise scales
soc_supp_items = ['w1q164a', 'w1q164b', 'w1q164c', 
  'w1q164d', 'w1q164e', 'w1q164f', 'w1q164g', 'w1q164h', 
  'w1q164i', 'w1q164j', 'w1q164k', 'w1q164l']

ace_items = ['w1q151', 'w1q152', 'w1q153', 
  'w1q154', 'w1q155', 'w1q156', 'w1q157', 
  'w1q158', 'w1q159', 'w1q160', 'w1q161']

childhd_gnc_items = [
  'w1q147', 'w1q148', 'w1q149', 'w1q150']

############# NOT CONDENSED (YET) #############
# strain_items = ['w1q146a', 'w1q146b', 
#   'w1q146c', 'w1q146d', 'w1q146e', 'w1q146f', 
#   'w1q146g', 'w1q146h', 'w1q146i', 'w1q146j', 
#   'w1q146k', 'w1q146l']
############# NOT CONDENSED (YET) #############

daily_discr_items = ['w1q144a', 'w1q144b', 
  'w1q144c','w1q144d', 'w1q144e', 'w1q144f', 
  'w1q144g', 'w1q144h', 'w1q144i']

# bi_stigma_items = [  # only in wave 2
#   'w2q117', 'w2q118', 'w2q119', 'w2q120']

int_homo_items = ['w1q128', 'w1q129', 
  'w1q130', 'w1q131', 'w1q132']

felt_stigma_items = ['w1q125', 'w1q126', 'w1q127']

drug_items = ['w1q90', 'w1q91', 'w1q92', 
  'w1q93', 'w1q94', 'w1q95', 'w1q96', 
  'w1q97', 'w1q98', 'w1q99', 'w1q100']

alc_items = ['w1q85', 'w1q86', 'w1q87']

ment_dis_items = ['w1q77a', 'w1q77b', 
  'w1q77c', 'w1q77d', 'w1q77e', 'w1q77f']

hc_ster_threat_items = [
  'w1q60', 'w1q61', 'w1q62', 'w1q63']

comm_conn_items = ['w1q53', 'w1q54', 
  'w1q55', 'w1q56', 'w1q57', 'w1q58', 'w1q59']

lgbis_items = [
  'w1q40', 'w1q41', 'w1q42', 'w1q43', 'w1q44']

meim_items = [
  'w1q21', 'w1q22', 'w1q23', 'w1q24', 'w1q25', 'w1q26']

swl_items = [
  'w1q186', 'w1q187', 'w1q188', 'w1q189', 'w1q190']

swb_items = ['w1q04', 'w1q05', 'w1q06', 'w1q07', 
  'w1q08', 'w1q09', 'w1q10', 'w1q11', 'w1q12', 
  'w1q13', 'w1q14', 'w1q15', 'w1q16', 'w1q17', 'w1q18']

drop_cols = (soc_supp_items + ace_items + childhd_gnc_items + 
  daily_discr_items + int_homo_items + felt_stigma_items + 
  drug_items + alc_items + ment_dis_items + hc_ster_threat_items + 
  comm_conn_items + lgbis_items + meim_items + swl_items + swb_items)
len(drop_cols)

meyer.drop(columns = drop_cols, inplace = True)
meyer.shape

# these are the scales
combo_features = ['w1socialwb', 'w1socialwb_i', 
  'w1lifesat', 'w1lifesat_i', 'w1meim', 'w1meim_i', 
  'w1idcentral', 'w1idcentral_i', 'w1connectedness',
  'w1connectedness_i', 'w1hcthreat', 'w1hcthreat_i', 
  'w1kessler6', 'w1kessler6_i', 'w1auditc', 
  'w1auditc_i', 'w1dudit', 'w1dudit_i', 'w1feltstigma', 
  'w1feltstigma_i', 'w1internalized', 'w1internalized_i', 
  'w1everyday', 'w1everyday_i', 'w1childgnc', 'w1childgnc_i',
  'w1ace', 'w1ace_i', 'w1ace_emo', 'w1ace_emo_i', 
  'w1ace_inc', 'w1ace_inc_i', 'w1ace_ipv', 'w1ace_ipv_i', 
  'w1ace_men', 'w1ace_men_i', 'w1ace_phy', 'w1ace_phy_i', 
  'w1ace_sep', 'w1ace_sep_i', 'w1ace_sex', 'w1ace_sex_i', 
  'w1ace_sub', 'w1ace_sub_i', 'w1socsupport', 
  'w1socsupport_fam', 'w1socsupport_fam_i', 
  'w1socsupport_fr', 'w1socsupport_fr_i', 
  'w1socsupport_i', 'w1socsupport_so', 'w1socsupport_so_i']

# split them up so I can check whether 
# the _i columns really are free of missing values
combo_imputed = [c for c in combo_features if c[-2:]=='_i']
combo_not_imputed = [c for c in combo_features if c[-2:]!='_i']

# check my splits
a = [c for c in combo_imputed if c in combo_not_imputed]
b = [c for c in combo_not_imputed if c in combo_imputed]
if len(a)==len(b)==0:
  print('no overlap')
  del (a, b)
if (len(combo_imputed)+len(combo_not_imputed))==len(combo_features):
  print('all accounted for')
  
# check for "missing" values
for i in combo_imputed:
  print('')
  print(f'{i}, {meyer[i].isna().sum()} NAs')
  print(meyer[i].value_counts(dropna = False).sort_values())

# see how bad it was in the original
for i in combo_not_imputed:
  print('')
  print(f'{i}, {meyer[i].isna().sum()} NAs')
  print(meyer[i].value_counts(dropna = False).sort_values())
missing_values = [('w1ace_sex', 75), ('w1ace_phy', 61), 
  ('w1ace_ipv', 139), ('w1ace_emo', 91), ('w1ace', 277), 
  ('w1everyday', 40), ('w1dudit', 66), ('w1connectedness', 51), 
  ('w1socialwb', 59), ('most others', '15-35')]

# very grim and not at all surprising that column with the most missings is IPV
# (from the ACE survey - so IPV among parents, not participants themselves)
# >>> meyer['w1ace_ipv'].value_counts(dropna = False)
# w1ace_ipv
# 0    950
# 1    429
#      139
# Name: count, dtype: int64
# >>> meyer['w1ace_ipv_i'].value_counts(dropna = False)
# w1ace_ipv_i
# 0    1024
# 1     494
# Name: count, dtype: int64
# >>> 1024-950
# 74
# >>> 139-74
# 65

# ok.  their imputation method seems really solid, but that is sus af.
# of the people who declined to answer about IPV, you think the majority 
# of them would have said NO!?!??!??????
# I'd be tempted to put every one of those guys down as a yes!!!!
# let me see the overlap with other stigmatized stuff
len(meyer[(meyer['w1ace_ipv']==' ') & (meyer['w1ace_sex']==' ')])
# 30 huh damn I would have thought like all of them
# wait.
len(meyer[(meyer['w1ace_ipv']=='1') & (meyer['w1ace_sex']==' ')])  # 19
len(meyer[(meyer['w1ace_ipv']==' ') & (meyer['w1ace_sex']=='1')])  # 51
# ok! that actually lends credibility to their imputation though
# if people were too ashamed to admit IPV, they'd probably decline to answer
# about CSA too.  these people, at least, really could go either way on IPV.

# This is all actually moot 
# because I don't have a better idea for imputation than what they did.
# I think the thing to do, if I can, is to model it on the imputed data
# then model it again on the subsample where I've dropped all these NAs
# at least the ACE NAs, where there's really a lot.
# could also try modeling it just without those columns
# a random forest would probably be good, 
# make sure the whole thing isn't hinging on imputed data
# Meyer also probably ran some tests in his paper to make sure this is ok

# OK SO.

# I've gotta reduce my dimensions
# the imputation methods they used seem very reasonable
# (see p. 37 of 37166-Documentation-methodology.pdf)
# so I'm going to drop the non-imputed ones
meyer.drop(columns = combo_not_imputed, inplace = True)
meyer.shape  #(1518, 373)

# ok!  love that!  let's see what else I can chuck.
cols_to_check = [c for c in list(meyer.columns) if c not in combo_imputed]
print(cols_to_check)

# I am looking thru the documentation and making 2 lists
# the variables should ROUGHLY correspond to each other
# maybe I'll do some line breaks or whatever.
drop_cols_2 = [
  'w1q165', 'w1q27', 'w1q28', 
  'w1q20_1', 'w1q20_2', 'w1q20_3', 'w1q20_4', 'w1q20_5', 'w1q20_6', 'w1q20_7', 
]

keep_cols = [
  'w1age', 'cohort', 'w1sex', 'w1gender', 'w1sex_gender', 
  'screen_race', 'w1race',
]

check_cols = [
  # no age, sex stuff
  'w1q20_t_verb', # I suspect this is part of q20 and got rolled into w1race, but I'm not sure off the top of my head
]

# KEEP GOING ON THESE ON FRIDAY
# I JUST FINISHED SEX AND GENDER
# PICK UP WITH SEXUAL IDENTITY, PAGE 14 (16) OF THE DOCUMENTATION
# 37166-Documentation-methodology.pdf

