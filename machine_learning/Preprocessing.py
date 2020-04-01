from sklearn.preprocessing import LabelEncoder
import pandas as pd


def preprocessing(df):

    categorical_labels = ['Platform', 'Genre', 'Publisher']
    numerical_labels = ['Global_Sales']
    enc = LabelEncoder()
    encoded_df = pd.DataFrame(columns=['Platform', 'Genre', 'Publisher', 'Global_Sales'])
    
    for label in categorical_labels:
        temp_column = df[label]
        
        encoded_temp_col = enc.fit_transform(temp_column)
        
        encoded_df[label] = encoded_temp_col

    for label in numerical_labels:
        encoded_df[label] = df[label].values

    return encoded_df

