from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import train_test_split


import numpy as np

# Off by 600k on average
def linear_regression(df):
    
    # Without Cross Validation
    
    x = df.iloc[:, 0:3]
    y = df.iloc[:,3:]

    x_train, x_test, y_train, y_test = train_test_split(x,y)

    scalar = StandardScaler()

    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test)

    linear_reg = LinearRegression()

    linear_reg.fit(x_train, y_train)

    y_pred = linear_reg.predict(x_test)

    r2 = r2_score(y_pred, y_test)
    
    print('\nLinear Regression Results without Cross Validation:')
    
    print(f'MAE in $ (Millions): {mean_absolute_error(y_pred, y_test)}')

    print(f'MSE in $ (Millions): {mean_squared_error(y_pred, y_test)}')

    print(f'R2 Coeff: {r2}')

    linear_regression_cv(x,y, scalar)


def linear_regression_cv(x,y, scalar):
    print('\nLinear Regression Results with Cross Validation')

    scaled_x = scalar.fit_transform(x)
    linear_reg = LinearRegression()
    y_pred = cross_val_predict(linear_reg, scaled_x, y, cv=5)
    r2 = cross_val_score(linear_reg, scaled_x,y, cv=5, scoring='r2')

    print(f'MAE in $ (Millions): {mean_absolute_error(y_pred, y)}')

    print(f'MSE in $ (Millions): {mean_squared_error(y_pred, y)}')

    print(f'R2 Coeff: {np.mean(r2)}')






