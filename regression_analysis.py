import db_utils
import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

GRID_SEARCH = False
BEST_PARAMS_ALPHA = 0
BEST_PARAMS_ETA0 = 0.0003

conn = db_utils.create_db_connection()

sql = 'SELECT price, make, odometer_km, year, colours, area, dealer, "engine_power_max_kW", engine_size_l, engine_fuel_type, engine_fuel_tank_l, engine_transmission, performace_0_to_100_s, performace_speed_max_kmph, economy_fuel_consumption_lpkm, economy_fuel_range_km, "economy_CO2_gpkm", "safety_ABS", "safety_EBD", safety_brake_assist, safety_driver_airbag, safety_passenger_airbag, safety_airbag_quantity, features_bluetooth, features_aircon, specs_doors, specs_seats, specs_kerb_weight, specs_central_locking FROM cars;'

data = pd.read_sql(sql, conn)

conn.close()

print('dataset shape before cleaning:', data.shape)

# show percentage of rows with missing values for each column
# print(data.isnull().sum()*100/data.shape[0])

# for now we will just keep columns with 80% non-null values
data.dropna(axis='columns', thresh=data.shape[0]*0.80, inplace=True)

# drop all rows which still have null values
data.dropna(inplace=True)

# drop columns which look less helpful or hard to deal with properly
data.drop(columns=['colours', 'dealer', 'area'], inplace=True)

# area is always western cape
# print(data['area'].describe())

# there are too many different dealers
# if we one-hot encode it we will get too many features and end up over-fitting

# colours sometimes has multiple colours available
# I want to do the one hot encoding properly (set multiple colours to 1 when a car has multiple colours available)
# Will get to this later

print('dataset shape after cleaning:', data.shape)

x = data.drop(columns=['price'])
y = data['price'].to_numpy().reshape(-1, 1)


# create one hot encodings for categorical columns
one_hot_columns = pd.get_dummies(x.select_dtypes(exclude=['number', 'bool']))

# remove original categorical columns and replace with their one hot encodings
x = x.select_dtypes(include=['number', 'bool']).join(one_hot_columns)

print('dataset shape after one hot encodings:', x.shape)

x_scaler = StandardScaler()
x_scaler.fit(x)

y_scaler = StandardScaler()
y_scaler.fit(y)

x_normalised = x_scaler.transform(x)
y_normalised = y_scaler.transform(y).ravel()

if GRID_SEARCH:
    params = {
        'alpha': [0, 0.00001, 0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01],  # regularisation
        'eta0': [0.00003, 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1],  # initial learning rate
    }
    grid_reg = GridSearchCV(SGDRegressor(), params, n_jobs=-1, verbose=1)
    grid_reg.fit(x_normalised, y_normalised)
    print('best parameters: ', grid_reg.best_params_)
    print('validation score: ', grid_reg.best_score_)
    results_df = pd.DataFrame.from_dict(grid_reg.cv_results_)
    reg = grid_reg.best_estimator_
else:
    reg = SGDRegressor(alpha=BEST_PARAMS_ALPHA, eta0=BEST_PARAMS_ETA0)
    reg.fit(x_normalised, y_normalised)

print('R^2 value:', reg.score(x_normalised, y_normalised))

print('coefficients:')
for i in reversed(np.argsort(reg.coef_)):
    print('%+.2f' % reg.coef_[i], x.columns[i], sep='\t')
