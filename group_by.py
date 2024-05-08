import pandas as pd
import config

def group_by_keyword(keyword, column_type):
    df = format_datetime_dataframe()
    df_keyword = df[df['Items'].str.contains(keyword)]
    df_keyword[column_type] = df_keyword[column_type].astype(int)
    df_sort = sort_values_by_time(df_keyword, column_type)
    return df_sort

def group_by_column_type(column_type):
    df = format_datetime_dataframe()
    df = df.drop(df[df[column_type] == ' '].index)
    df = df[df[column_type].notna()]
    df[column_type] = df[column_type].astype(float)
    df_sort = sort_values_by_time(df, column_type)
    return df_sort

def format_datetime_dataframe():
    df = pd.read_csv(config.SPREADSHEET_URL, usecols=[0,1,2,3,4], header=3)
    df['Time'] = pd.to_datetime(df['Time'], format='%B %d %Y')
    return df

def sort_values_by_time(df, column_type):
    df_groupby = (df.groupby(df['Time'].dt.strftime('%Y-%m'))
                    .agg(total = (column_type, 'sum'))
                    .reset_index())
    df_groupby['Time'] = pd.to_datetime(df_groupby['Time'], format='%Y-%m').dt.strftime('%Y-%m')
    df_groupby.sort_values(by='Time') 
    return df_groupby