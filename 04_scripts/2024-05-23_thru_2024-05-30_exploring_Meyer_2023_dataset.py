# 5/23/24 AND 5/29/24

# check out this dataset from Ilan Meyer, my beloved

# Import Data
#meyer = pd.read_csv('./potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', sep = '\t', low_memory=False)
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
  'w1q29', 'w1q29_t_verb', 
  # kept all ed columns
  'gruca', 'gruca_i', 'gurban', 'gzipstate',  'gzipcode', 
  'w1hinc', 'w1poverty', 'w1povertycat', 
  'w1q133', 'w1q133_1', 'w1q133_2', 'w1q133_3', 
  # from here I'm just going thru the 831 page documentation and picking stuff out
  'w1weight_orig', 
  'gmsaname', 'gmethod_type', 'gmethod_type_w2', 'gmethod_type_w3', 
  'w1cumulative_wt_nr1', 'w1cumulative_wt_nr2', 'w1cumulative_wt_nr3', 
  'w1cumulative_wt_sampling', 'w1weighting_cell_nr1', 'w1weighting_cell_nr2and3', 
  'w1frame_wt', 
]

keep_cols = ['studyid', 'waveparticipated', 'w1survey_yr', 
  'w1age', 'cohort', 'w1sex', 'w1gender', 'w1sex_gender', 
  'screen_race', 'w1race',
  'w1sexualid', 'w1sexminid', 
  'geduc1', 'geduc2', 'geducation', 
  'gurban_i', 'gcendiv', 'gcenreg', 'gmilesaway', 'gmilesaway2', 
  'w1hinc_i', 'w1poverty_i', 'w1povertycat_i', 
  'w1conversion', 'w1conversionhc', 'w1conversionrel', 
  'w1weight_full', 'gemployment2010', 
]

check_cols = [
  # no age, sex stuff
  'w1q20_t_verb', # I suspect this is part of q20 and got rolled into w1race, but I'm not sure off the top of my head
]

# can I weed out the redacted ones quickly?

x = list(meyer.columns)
x_redacted = [c for c in x if meyer[c].nunique()==1]
# it works!  but I already caught these guys


# I finished all the variables that were easy to parse out and assigned
# them to a list above.  I am now going to drop the ones that I indicated,
# and then I will go through the 831 page documentation to make sense 
# of what's left and try to drop more.

meyer.drop(columns = drop_cols_2, inplace = True) # (1518, 337)

suicidal_idea_beh = [
  'w1q101', 'w1q102', 'w1q103', 'w1q104', 'w1q105', 'w1q106', 'w1q107', 
  'w1q108', 'w1q109', 'w1q110', 'w1q111', 'w1q112', 'w1q113', 'w1q114', 
  'w1q115', 'w1q116', 'w1q117', 'w1q118', 'w1q119', 'w1q120', 'w1q121',
  'w1q122']

drop_cols_2_again = [
  'w1q31a', 'w1q31b', 'w1q31c', 'w1q31d', # redundant with sexual identity
  'w1q66_1', 'w1q66_2', 'w1q66_3', 'w1q66_4', 'w1q66_5', 'w1q66_t_verb', # interesting to compare 
  #ER to Dr ofc, but not for this study.  too many columns already ^
  'w1q67', 'w1q68_1', 'w1q68_2', 'w1q68_3', 'w1q70', 'w1q71', 'w1q73', # <- same ^ and V
  'w1q74_1', 'w1q74_2', 'w1q74_3', 'w1q74_4', 'w1q74_7', 'w1q74_8', 'w1q74_9', 
  'w1q74_12', 'w1q74_13', 'w1q74_15', 'w1q74_16', 'w1q74_19', 'w1q80', 'w1q81',
  'w1q82', 'w1q83', 'w1q84', 'w1q88', 'w1q118', 'w1q170_1', 'w1q170_2', 
  'w1q170_3', 'w1q170_4', 'w1q172', 'w1q173', 'w1q174', 'w1q176', 'w1q177_1', 
  'w1q177_2', 'w1q177_3', 'w1q177_4', 'w1q177_5', 'w1q177_6', 'w1q177_7', 
  'w1q177_8', 'w1q177_9', 'w1q177_10', 'w1q177_11', 'w1q177_12', 'w1q178', 
  'w1q182', 'w1q183', 'w1q184', 'w1q185',  'w1sample',  'w1pinc', 
  'grespondent_date_w2', 'gsurvey', 'gp2', 'grace', 'grespondent_date_w3', 
  'wave3', 'nopolicecontact']

keep_cols_good_on_own = ['w1q01', 'w1q02', 'w1q03', 'w1q32', 
  'w1q33', 'w1q34', 'w1q35', 'w1q36', 'w1q37', 'w1q38', 'w1q52', 
  'w1q65',  'w1q69', 'w1q72', 'w1q74_21', 'w1q74_22', 'w1q74_23', 
  'w1q78', 'w1q79', 'w1q89', 'w1q119', 'w1q134', 'w1q136_7', 'w1q139_7', 
  'w1q140', 'w1q141_7', 'w1q143_7', 'w1q145_7', 'w1q162',  'w1q163_7', 
  'w1q166', 'w1q167', 'w1q168', 'w1q169', 'w1q175', 'gp1', 'w1pinc_i']

keep_cols_ohe_done = ['w1q30_1', 'w1q30_2', 'w1q30_3', 'w1q30_4', 'w1q30_5', 
  'w1q39_1', 'w1q39_2', 'w1q39_3', 'w1q39_4', 'w1q39_5', 'w1q39_6', 'w1q39_7', 
  'w1q39_8', 'w1q39_9', 'w1q39_10', 'w1q39_11', 'w1q39_12', 'w1q39_t_verb',
  'w1q171_1', 'w1q171_2', 'w1q171_3', 'w1q171_4', 'w1q171_5', 'w1q171_6', 
  'w1q171_7', 'w1q171_8', 'w1q171_9']

# manually combine columns in ways that *I* think make sense
# here I am creating a dictionary where the keys are the new column names I want
# and the values are lists, wherein the first value on the list is the method 
# of combination, and the remainder are the columns to be combined
# if the method is 'recode', then I probably need to give it more direct attn
# but all the others I am hoping to be able to automate
# the end goal is to use this dictionary to either generate or directly run
# the code to create the new columns and drop the ones no longer needed
# before dropping the columns, I should check them against keep_cols
# to make sure I'm not hoping to keep them individually in addition to combo'ing

feat_eng_dict = {'pers_well_being': ['sum', 'w1q01', 'w1q02'],
  'neighb_welcoming': ['mean', 'w1q19a', 'w1q19b', 'w1q19c', 'w1q19d'],
  'age_awakening': ['min','w1q45', 'w1q46', 'w1q47', 'w1q48'],
  'age_out': ['min', 'w1q49', 'w1q50', 'w1q51'],
  'health_insurance': ['binarize', 'w1q64_1', 'w1q64_2', 'w1q64_3', 'w1q64_4', 
    'w1q64_5', 'w1q64_6', 'w1q64_7', 'w1q64_8', 'w1q64_9', 'w1q64_10', 
    'w1q64_11', 'w1q64_12', 'w1q64_13', 'w1q64_t_verb'], 
  'serious_health_cond': ['binarize', 'w1q74_5', 'w1q74_6', 'w1q74_10', 
    'w1q74_11', 'w1q74_14', 'w1q74_17', 'w1q74_18', 'w1q74_20'], 
  'disabled': ['binarize', 'w1q75', 'w1q76'],
  'suicidal_ideation': ['sum', 'w1q101', 'w1q105', 'w1q109'], 
  'suicide_attempts': ['recode', 'w1q113', 'w1q114'],
  'sui_idea_age_first': ['min', 'w1q102', 'w1q103', 'w1q104', 
    'w1q106', 'w1q107', 'w1q108', 'w1q110', 'w1q111', 'w1q112'],
  'sui_idea_age_recent': ['max', 'w1q102', 'w1q103', 'w1q104', 
    'w1q106', 'w1q107', 'w1q108', 'w1q110', 'w1q111', 'w1q112'],
  'sui_attem_age_first': ['min', 'w1q115', 'w1q116', 'w1q117'], 
  'sui_attem_age_recent': ['max', 'w1q115', 'w1q116', 'w1q117'], 
  'nssh_age_first': ['min', 'w1q120', 'w1q121', 'w1q122'],
  'nssh_age_recent': ['max', 'w1q120', 'w1q121', 'w1q122'],
  'closeted': ['sum', 'w1q123a', 'w1q123b', 'w1q123c', 'w1q123d', 'w1q124'],
  'abusive_treatment': ['sum', 'w1q135a', 'w1q135b', 
    'w1q135c', 'w1q135d', 'w1q135e', 'w1q135f'],
  'work_neg_outcomes': ['recode', 'w1q137', 'w1q138'], # account for age
  'abus_treat_non_queer': ['binarize', 'w1q136_1', 'w1q136_5', 'w1q136_6', 
    'w1q136_8', 'w1q136_9', 'w1q136_10'],
  'stress_past_year_gen': ['recode', 'w1q142a', 'w1q142h', 'w1q142i'],
  'stress_past_year_work': ['recode', 'w1q142b', 'w1q142c', 'w1q142e'],
  'stress_past_year_interpersonal': ['recode', 'w1q142d', 'w1q142f', 'w1q142g'],
  'stress_past_year_crime': ['recode', 'w1q142j', 'w1q142k'],
  'work_disc_non_queer': ['binarize', 'w1q139_1', 'w1q139_5', 'w1q139_6', 
    'w1q139_8', 'w1q139_9', 'w1q139_10'],
  'housing_disc_non_queer': ['binarize', 'w1q141_1', 'w1q141_5', 'w1q141_6', 
    'w1q141_8', 'w1q141_9', 'w1q141_10'],
  'stress_past_year_non_queer': ['binarize', 'w1q143_1', 'w1q143_5', 'w1q143_6', 
    'w1q143_8', 'w1q143_9', 'w1q143_10'],
  'daily_discr_non_queer': ['binarize', 'w1q145_1', 'w1q145_5', 'w1q145_6'],
  'childhd_bullying_non_queer': ['binarize', 'w1q163_1', 'w1q163_5', 'w1q163_6', 
    'w1q163_8', 'w1q163_9', 'w1q163_10'],
  'abus_treat_sex_gender': ['binarize', 'w1q136_2', 'w1q136_3', 'w1q136_4'],
  'work_disc_sex_gender': ['binarize', 'w1q139_2', 'w1q139_3', 'w1q139_4'],
  'housing_disc_sex_gender': ['binarize', 'w1q141_2', 'w1q141_3', 'w1q141_4'],
  'stress_past_year_sex_gender': ['binarize', 'w1q143_2', 'w1q143_3', 'w1q143_4'],
  'daily_discr_sex_gender': ['binarize', 'w1q145_2', 'w1q145_3', 'w1q145_4', 
    'w1q145_8', 'w1q145_9', 'w1q145_10'],
  'childhd_bullying_sex_gender': ['binarize', 'w1q163_2', 'w1q163_3', 'w1q163_4'],
  'religiosity': ['recode', 'w1q179', 'w1q180', 'w1q181'], 
  'chronic_strain': ['sum', 'w1q146a', 'w1q146b', 'w1q146c', 'w1q146d', 'w1q146e', 
    'w1q146f', 'w1q146g', 'w1q146h', 'w1q146i', 'w1q146j', 'w1q146k', 'w1q146l']}


