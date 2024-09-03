# Friday, June 7, 2024
# EDA

# As usual, we're starting with my beloved autoplots - now with new arguments!

autoplots(meyer, 'w1kessler6_i', qqplots=True, transform=True, line=False, verbose=True)
autoplots(meyer, 'kessler6_sqrt', qqplots=True, transform=True, line=False, verbose=True)

# There are a few more that I need to OHE, 0-base, or otherwise tinker with, but I'm going
# to try to resist the urge to do that until I have SOME kind of model fit.

pd.set_option('display.max_rows', None)
meyer.info()

# I hate spending the time on this, but I need the column names to have meaning.
for i in list(meyer.columns):
  print(f"'{i}': '{i}', ")

# I'm trying to both at once and it's not working
# This list is for whether to screw with them some more.
for i in list(meyer.columns):
  print(f"'{i}': _, ")

meyer['w1kessler6_i'].value_counts(dropna = False).sort_index()
col_bi.append('') # abus_treat_non_queer?

col_names = {
  'studyid': 'studyid', 
  'w1kessler6_i': 'kessler6_orig', 
  'kessler6_sqrt': 'kessler6_sqrt', 
  
  'abus_treat_non_queer': 'abus_treat_non_queer', 
  'abus_treat_sex_gender': 'abus_treat_sex_gender', 
  'abusive_treatment': 'abusive_treatment', 
  'bad_neighbhd': 'bad_neighbhd', 
  'childhd_bullying_non_queer': 'childhd_bullying_non_queer', 
  'childhd_bullying_sex_gender': 'childhd_bullying_sex_gender', 
  'chronic_strain': 'chronic_strain', 
  'cohort': 'cohort', 
  'daily_discr_non_queer': 'daily_discr_non_queer', 
  'daily_discr_sex_gender': 'daily_discr_sex_gender', 
  'disabled': 'disabled', 
  'gcendiv': 'gcendiv', 
  'gcenreg': 'gcenreg', 
  'geduc1': 'geduc1', 
  'geduc2': 'geduc2', 
  'geducation': 'geducation', 
  'gmilesaway2_ei_r': 'gmilesaway2_ei_r', 
  'gurban_i': 'gurban_i', 
  'health_insurance': 'health_insurance', 
  'housing_disc_non_queer': 'housing_disc_non_queer', 
  'housing_disc_sex_gender': 'housing_disc_sex_gender', 
  'outness': 'outness', 
  'screen_race': 'screen_race', 
  'serious_health_cond': 'serious_health_cond', 
  'stress_past_year_crime': 'stress_past_year_crime', 
  'stress_past_year_gen': 'stress_past_year_gen', 
  'stress_past_year_interpersonal': 'stress_past_year_interpersonal', 
  'stress_past_year_non_queer': 'stress_past_year_non_queer', 
  'stress_past_year_sex_gender': 'stress_past_year_sex_gender', 
  'stress_past_year_work': 'stress_past_year_work', 
  'suicidality': 'suicidality', 
  'w1ace_emo_i': 'w1ace_emo_i', 
  'w1ace_i': 'w1ace_i', 
  'w1ace_inc_i': 'w1ace_inc_i', 
  'w1ace_ipv_i': 'w1ace_ipv_i', 
  'w1ace_men_i': 'w1ace_men_i', 
  'w1ace_phy_i': 'w1ace_phy_i', 
  'w1ace_sep_i': 'w1ace_sep_i', 
  'w1ace_sex_i': 'w1ace_sex_i', 
  'w1ace_sub_i': 'w1ace_sub_i', 
  'w1age': 'w1age', 
  'w1auditc_i': 'w1auditc_i', 
  'w1childgnc_i': 'w1childgnc_i', 
  'w1connectedness_i': 'w1connectedness_i', 
  'w1conversion': 'w1conversion', 
  'w1conversionhc': 'w1conversionhc', 
  'w1conversionrel': 'w1conversionrel', 
  'w1dudit_i': 'w1dudit_i', 
  'w1everyday_i': 'w1everyday_i', 
  'w1feltstigma_i': 'w1feltstigma_i', 
  'w1gender': 'w1gender', 
  'w1hcthreat_i': 'w1hcthreat_i', 
  'w1hinc_i': 'w1hinc_i', 
  'w1idcentral_i': 'w1idcentral_i', 
  'w1internalized_i': 'w1internalized_i', 
  'w1lifesat_i': 'w1lifesat_i', 
  'w1meim_i': 'w1meim_i', 
  'w1pinc_i': 'w1pinc_i', 
  'w1poverty_i_ei': 'w1poverty_i_ei', 
  'w1povertycat_i_ei': 'w1povertycat_i_ei', 
  'w1q01_ei': 'w1q01_ei', 
  'w1q03_ei': 'w1q03_ei', 
  'w1q119_ei': 'w1q119_ei', 
  'w1q136_7_ei': 'w1q136_7_ei', 
  'w1q139_7_ei': 'w1q139_7_ei', 
  'w1q140_ei': 'w1q140_ei', 
  'w1q141_7_ei': 'w1q141_7_ei', 
  'w1q143_7_ei': 'w1q143_7_ei', 
  'w1q145_7_ei': 'w1q145_7_ei', 
  'w1q162_ei': 'w1q162_ei', 
  'w1q163_7_ei': 'w1q163_7_ei', 
  'w1q166_ei': 'w1q166_ei', 
  'w1q167_ei': 'w1q167_ei', 
  'w1q168_ei': 'w1q168_ei', 
  'w1q169_ei': 'w1q169_ei', 
  'w1q171_1_ei': 'w1q171_1_ei', 
  'w1q171_2_ei': 'w1q171_2_ei', 
  'w1q171_3_ei': 'w1q171_3_ei', 
  'w1q171_4_ei': 'w1q171_4_ei', 
  'w1q171_5_ei': 'w1q171_5_ei', 
  'w1q171_6_ei': 'w1q171_6_ei', 
  'w1q171_7_ei': 'w1q171_7_ei', 
  'w1q171_8_ei': 'w1q171_8_ei', 
  'w1q171_9_ei': 'w1q171_9_ei', 
  'w1q175_ei': 'w1q175_ei', 
  'w1q179_ei_r_relig_christ': 'w1q179_ei_r_relig_christ', 
  'w1q179_ei_r_relig_other': 'w1q179_ei_r_relig_other', 
  'w1q180_ei_r_relig_christ': 'w1q180_ei_r_relig_christ', 
  'w1q180_ei_r_relig_other': 'w1q180_ei_r_relig_other', 
  'w1q181_ei_r': 'w1q181_ei_r', 
  'w1q30_1_ei': 'w1q30_1_ei', 
  'w1q30_2_ei': 'w1q30_2_ei', 
  'w1q30_3_ei': 'w1q30_3_ei', 
  'w1q30_4_ei': 'w1q30_4_ei', 
  'w1q30_5_ei': 'w1q30_5_ei', 
  'w1q32_ei': 'w1q32_ei', 
  'w1q33_ei': 'w1q33_ei', 
  'w1q34_ei': 'w1q34_ei', 
  'w1q35_ei': 'w1q35_ei', 
  'w1q36_ei': 'w1q36_ei', 
  'w1q37_ei': 'w1q37_ei', 
  'w1q38_ei': 'w1q38_ei', 
  'w1q52_ei': 'w1q52_ei', 
  'w1q64_1_ei': 'w1q64_1_ei', 
  'w1q65_ei': 'w1q65_ei', 
  'w1q69_ei': 'w1q69_ei', 
  'w1q72_ei': 'w1q72_ei', 
  'w1q74_21_ei': 'w1q74_21_ei', 
  'w1q74_22_ei': 'w1q74_22_ei', 
  'w1q74_23_ei': 'w1q74_23_ei', 
  'w1q78_ei': 'w1q78_ei', 
  'w1q79_ei': 'w1q79_ei', 
  'w1q89_ei': 'w1q89_ei', 
  'w1race': 'w1race', 
  'w1sex': 'w1sex', 
  'w1sex_gender': 'w1sex_gender', 
  'w1sexminid': 'w1sexminid', 
  'w1sexualid': 'w1sexualid', 
  'w1socialwb_i': 'w1socialwb_i', 
  'w1socsupport_fam_i': 'w1socsupport_fam_i', 
  'w1socsupport_fr_i': 'w1socsupport_fr_i', 
  'w1socsupport_i': 'w1socsupport_i', 
  'w1socsupport_so_i': 'w1socsupport_so_i', 
  'w1survey_yr': 'w1survey_yr', 
  'w1weight_full': 'w1weight_full', 
  'waveparticipated': 'waveparticipated', 
  'work_disc_non_queer': 'work_disc_non_queer', 
  'work_disc_sex_gender': 'work_disc_sex_gender', 
  'work_neg_outcomes': 'work_neg_outcomes'
}


meyer_corr = meyer.corr()

meyer.shape
meyer.to_csv(f'{my_date()}_end-of-day.csv', index = False)

