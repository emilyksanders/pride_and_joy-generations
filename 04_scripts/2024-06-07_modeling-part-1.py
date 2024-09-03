# Friday, June 7, 2024
# Modeling!

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

# I'm just going to eyeball some features from the scatterplots
good_ones = ['chronic_strain', 'suicidality', 'w1age', 'w1auditc_i', 
    'w1connectedness_i', 'w1conversion', 'w1dudit_i', 'w1everyday_i', 
  'w1feltstigma_i', 'w1idcentral_i', 'w1internalized_i', 'w1lifesat_i', 
  'w1meim_i', 'w1pinc_i', 'w1poverty_i_ei', 'w1q03_ei', 'w1q33_ei', 
  'w1q52_ei', 'w1q72_ei', 'w1q74_22_ei', 'w1q74_21_ei', 'w1q140_ei', 
  'w1q166_ei', 'w1q167_ei', 'w1q171_8_ei', 'w1q181_ei_r', 'w1socialwb_i', 
  'w1socsupport_i']

# Make X and y
X = meyer[good_ones]
y = meyer['kessler6_sqrt']

# Very small testing set because this is an inferential model
X_train, X_test, y_train, y_test = train_test_split(X, y, 
  test_size = 0.1, random_state = 6)
  
for i in [X_train, X_test, y_train, y_test]:
  print(i.shape)

# Instantiate the model
lr = LinearRegression()

# Cross validation just for funsies
cross_val_score(lr, X_train, y_train)

# Fit the model
model_1 = lr.fit(X_train, y_train)

# Make some predictions
model_1_train_preds = model_1.predict(X_train)
model_1_test_preds = model_1.predict(X_test)

# Score the model
print('Training Set')
model_1.score(X_train, y_train)
mean_squared_error(y_train, model_1_train_preds)
mean_squared_error(y_train, model_1_train_preds, squared = False)
mean_absolute_error(y_train, model_1_train_preds)
print('='*20)
print('Testing Set')
model_1.score(X_test, y_test)
mean_squared_error(y_test, model_1_test_preds)
mean_squared_error(y_test, model_1_test_preds, squared = False)
mean_absolute_error(y_test, model_1_test_preds)







