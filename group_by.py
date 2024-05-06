import pandas as pd
import config

def group_by_keyword(keyword, column_type):
    df = pd.read_csv(config.SPREADSHEET_URL, usecols=[0,1,2,3,4], header=3)
    df['Time'] = pd.to_datetime(df['Time'], format='%B %d %Y')
    df_keyword = df[df['Items'].str.contains(keyword)]
    df_keyword[column_type] = df_keyword[column_type].astype(int)
    df_groupby = (df_keyword
                  .groupby(df_keyword['Time'].dt.strftime('%Y-%m'))
                  .agg(total = (column_type, 'sum')))

    new_df = df_groupby.reset_index()
    new_df['Time'] = pd.to_datetime(new_df['Time'], format='%Y-%m').dt.strftime('%Y-%m')
    new_df.sort_values(by='Time') 
    return new_df