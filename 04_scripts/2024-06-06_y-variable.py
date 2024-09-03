# Thursday, June 6, 2024

# I should probably also choose a y variable.  [several hours latere]  Let's go with
# Kessler6!  It's a general mental health scale.  According to the documentation, there were
# 1491 complete cases of this, and honestly I'd be fine just dropping the rest.  Let me see
# how many missing values there were per row in the imputed versions.  If it's only 1, I 
# might let it slide.


# Reimport the data to get a look at the unimputed columns
og_meyer = pd.read_csv(
  './potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv',
  sep = '\t', low_memory=False, na_values = ' ') # Thanks to ibrahim rupawala for highlighting the na_values argument

# Pull some stuff out
og_meyer_kessler = og_meyer[['STUDYID', 'W1Q77A', 'W1Q77B', 'W1Q77C', 'W1Q77D', 'W1Q77E', 'W1Q77F', 'W1KESSLER6', 'W1KESSLER6_I']]
og_meyer_kessler = og_meyer_kessler[og_meyer_kessler['W1KESSLER6'].isna()]

# Find the rows that have multiple NAs
kes_cols = ['W1Q77A', 'W1Q77B', 'W1Q77C', 'W1Q77D', 'W1Q77E', 'W1Q77F']
drop_rows = []
for i in og_meyer_kessler.index:
  if og_meyer_kessler.loc[i, kes_cols].isna().sum() > 1:
    drop_rows.append(og_meyer_kessler.loc[i, 'STUDYID'])

# get rid of those rows
meyer.shape # (1507, 233)
len(drop_rows) # 13
# meyer_d = meyer.loc[(meyer['studyid'] not in drop_rows), :]  # goal is (1494, 233)
# not working ^

drop_index = []
for i in drop_rows:
  drop_index.append(meyer[meyer['studyid']==i].index[0])
check = meyer.loc[drop_index, ['studyid', 'w1kessler6_i']]

meyer.drop(index = drop_index, inplace = True)

meyer.shape

meyer.to_csv('2024-06-06_bad-y-rows-dropped.csv', index = False)

# thanks to pandas documentation for this syntax
meyer.reset_index(drop = True, inplace = True)
meyer.to_csv('2024-06-06_bad-y-rows-dropped_reindexed.csv', index = False)
# I checked in the terminal and this version and the previous csv are exactly the same.

meyer['w1kessler6_i'].describe()


# oh no is it skewed
# Plot a histogram of it
plt.figure(figsize = (16, 9));
plt.hist(meyer['w1kessler6_i'], bins = 'auto', color = 'purple');
plt.suptitle(f'Distribution of {Y}', size = 24)
# plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
plt.xlabel('w1kessler6_i', size = 20);
plt.ylabel('Frequency', size = 20);
plt.xticks(size = 16, rotation = 60);
plt.yticks(size = 16)
#plt.tight_layout()
# plt.savefig(f'./{a}/{i}_histogram.png')
plt.show()
plt.close()

# Plot a histogram of it
plt.figure(figsize = (16, 9));
plt.hist(meyer['w1kessler6_i']**(1/2), bins = 'auto', color = 'purple');
plt.suptitle(f'Distribution of {Y}', size = 24)
# plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
plt.xlabel('w1kessler6_i', size = 20);
plt.ylabel('Frequency', size = 20);
plt.xticks(size = 16, rotation = 60);
plt.yticks(size = 16)
#plt.tight_layout()
# plt.savefig(f'./{a}/{i}_histogram.png')
plt.show()
plt.close()

# Plot a histogram of it
plt.figure(figsize = (16, 9));
plt.hist(meyer['w1kessler6_i']**(1/3), bins = 'auto', color = 'purple');
plt.suptitle(f'Distribution of {Y}', size = 24)
# plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
plt.xlabel('w1kessler6_i', size = 20);
plt.ylabel('Frequency', size = 20);
plt.xticks(size = 16, rotation = 60);
plt.yticks(size = 16)
#plt.tight_layout()
# plt.savefig(f'./{a}/{i}_histogram.png')
plt.show()
plt.close()

# Plot a histogram of it

# log transformation gets a div by 0 warning
# plt.figure(figsize = (16, 9));
# plt.hist(np.log(meyer['w1kessler6_i']), bins = 'auto', color = 'purple');
# plt.suptitle(f'Distribution of {Y}', size = 24)
# # plt.title(f'Based on {n} Observations out of {n_grand}', size = 18)
# plt.xlabel('w1kessler6_i', size = 20);
# plt.ylabel('Frequency', size = 20);
# plt.xticks(size = 16, rotation = 60);
# plt.yticks(size = 16)
# #plt.tight_layout()
# # plt.savefig(f'./{a}/{i}_histogram.png')
# plt.show()
# plt.close()

import statsmodels.api as sm

# QQplot of raw kessler
sm.qqplot(meyer['w1kessler6_i'], line='45');
plt.suptitle(f'QQ-Plot of kessler6_i', size = 20);
plt.xticks(size = 14, rotation = 60);
plt.yticks(size = 14);
plt.tight_layout();
# plt.savefig('./03_images/output/dropout_rate_qqplot.png')
plt.show()
plt.close()

# QQplot of sqrt kessler
sm.qqplot((meyer['w1kessler6_i']**0.5), line='45');
plt.suptitle(f'QQ-Plot of kessler6_i', size = 20);
plt.xticks(size = 14, rotation = 60);
plt.yticks(size = 14);
plt.tight_layout();
# plt.savefig('./03_images/output/dropout_rate_qqplot.png')
plt.show()
plt.close()

# QQplot of cbrt kessler
sm.qqplot((meyer['w1kessler6_i']**(1/3)), line='45');
plt.suptitle(f'QQ-Plot of kessler6_i', size = 20);
plt.xticks(size = 14, rotation = 60);
plt.yticks(size = 14);
plt.tight_layout();
# plt.savefig('./03_images/output/dropout_rate_qqplot.png')
plt.show()
plt.close()

# Ok, I'll square root it.

meyer['kessler6_sqrt'] = (meyer['w1kessler6_i']**0.5)
meyer.shape

# let's get a copy of that too
meyer.to_csv('2024-06-06_sqrt-kessler.csv', index = False)



