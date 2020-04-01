import DataCleaning as d_c
import EDA as eda
import pandas as pd
from machine_learning import Preprocessing as preprocess, LinearRegression as l_r
def main():
    df = pd.read_csv('Data/vgsales.csv')

    df = d_c.clean_data(df)

    #eda.eda(df)

    # Stuck on whether or not the name column is important. Brand names are really important,
    # but I don't know if I have the information or model sophisticated enough to consider that.
    # I'll drop it for now
    df.drop(['Name'], axis=1, inplace=True)
    df.drop(['Rank'], axis=1, inplace=True)
    df.drop(['Year'], axis=1, inplace=True)

    df = preprocess.preprocessing(df)

    l_r.linear_regression(df)

if __name__ == '__main__':
    main()