from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split, GridSearchCV


import numpy as np

# Off by 600k on average
def linear_regression(df):
    
    # Without Cross Validation
    
    x = df.iloc[:, 0:3]
    y = df.iloc[:,3:]

    scalar = StandardScaler()

    x = scalar.fit_transform(x)

    linear_reg = LinearRegression()

    linear_reg.fit(x, y)

    y_pred = linear_reg.predict(x)

    r2 = r2_score(y, y_pred)

    print('\nLinear Regression Results without Cross Validation:')
    
    print(f'MAE in $ (Millions): {mean_absolute_error(y_pred, y)}')

    print(f'MSE in $ (Millions): {mean_squared_error(y_pred, y)}')

    print(f'R2 Coeff: {r2}')

    linear_regression_cv(x,y, scalar)

    linear_regression_ridge_cv(x,y, scalar)

    linear_regression_lasso_cv(x,y, scalar)

    print('\nLasso Model Results with 10 Test Train Splits:')

    lasso_result_list = list()
    for i in range(0,10):
        lasso_result_list.append(linear_regression_lasso_model(x,y,scalar))

    mae = list()
    mse = list()

    for result in lasso_result_list:
        mae.append(result['MAE'])
        mse.append(result['MSE'])

    print(f'MAE in Sales (Millions): {np.mean(mae)}')
    print(f'MSE in Sales (Millions): {np.mean(mse)}')
    print('\nTest by Test Results:')

    for counter in range(0,len(lasso_result_list)):
        print(f'Test {counter+1}:\n\tMAE: {mae[counter]}\n\tMSE: {mse[counter]}')

def linear_regression_cv(x,y, scalar):
    print('\nLinear Regression Results with Cross Validation')

    scaled_x = scalar.fit_transform(x)

    linear_reg = LinearRegression()

    y_pred = cross_val_predict(linear_reg, scaled_x, y, cv=5)

    r2 = r2_score(y, y_pred)

    print(f'MAE in Sales (Millions): {mean_absolute_error(y_pred, y)}')

    print(f'MSE in Sales (Millions): {mean_squared_error(y_pred, y)}')

    print(f'R2 Coeff: {r2}')


def linear_regression_ridge_cv(x, y, scalar):
    print('\nRidge Regression Results with Cross Validation')
    x = scalar.fit_transform(x)
    x = scalar.transform(x)

    ridge = Ridge()

    grid = GridSearchCV(ridge, param_grid={'alpha':range(0,10)}, refit=True)

    y_pred = cross_val_predict(grid, x,y, cv=5)

    r2 = r2_score(y, y_pred)

    print(f'MAE in Sales (Millions): {mean_absolute_error(y_pred, y)}')

    print(f'MSE in Sales (Millions): {mean_squared_error(y_pred, y)}')

    print(f'R2 Coeff: {r2}')


def linear_regression_lasso_cv(x, y, scalar):
    print('\nLasso Regression Results with Cross Validation')
    x = scalar.fit_transform(x)
    x = scalar.transform(x)

    lasso = Lasso()

    grid = GridSearchCV(lasso, param_grid={'alpha': range(1, 10)}, refit=True)

    y_pred = cross_val_predict(grid, x, y, cv=5)

    r2 = r2_score(y, y_pred)

    print(f'MAE in Sales (Millions): {mean_absolute_error(y_pred, y)}')

    print(f'MSE in Sales (Millions): {mean_squared_error(y_pred, y)}')

    print(f'R2 Coeff: {r2}')


def linear_regression_lasso_model(x, y, scalar):
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test)

    lasso = Lasso(alpha=1)

    lasso.fit(x_train, y_train)

    y_pred = lasso.predict(x_test)

    return {'MAE': mean_absolute_error(y_test, y_pred),
            'MSE': mean_squared_error(y_test, y_pred)}



