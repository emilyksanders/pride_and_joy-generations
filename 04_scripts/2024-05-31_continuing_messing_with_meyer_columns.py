meyer.shape
meyer.columns


# Before we do this next bit, let's preserve these guys
keep_cols = combo_imputed + keep_cols + keep_cols_good_on_own + keep_cols_ohe_done

# Now I need to handle the columns in the dictionary

# did I duplicate any names?
for i in feat_eng_dict.keys():
  if i in keep_cols:
    print(i)

# nope!

# meyer_test = pd.read_csv('./potential_datasets/2024_05_23_download_ICPSR_Meyer_2023_generations_data_attempt_2/ICPSR_37166/DS0007/37166-0007-Data.tsv', sep = '\t', low_memory=False, na_values = ' ')
# meyer_test_nas = pd.DataFrame(data = meyer_test.isna().sum())

# check again because I figured out how to handle the "NAs" as strings
meyer.isna().sum().sum()
for i in list(zip(list(meyer.dtypes), list(meyer.columns))):
  print(i)

# drop these guys
meyer.drop(columns = drop_cols_2_again, inplace = True)

# I want to fill all my NAs with 0s, so I can do math on things.
# Can I do that?  Do any of these columns have natural 0s?

for i in list(meyer.columns):
  a = list(meyer[i].unique())
  if 0 in a:
    print(i)
