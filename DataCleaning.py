import numpy as np


def clean_data(df):

    # Fill empty values.. only about 300ish, so I could've dropped them as well.

    df['Year'].fillna(df['Year'].mode()[0], inplace=True)

    df['Publisher'].replace(np.nan, df['Publisher'].mode()[0], inplace=True)

    df['Platform'].replace('2600', 'Atari', inplace=True)

    df = df[df.Year < 2017]

    return df
