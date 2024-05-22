import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    url = 'https://docs.google.com/spreadsheets/d/1YAEnVA0NlZJXOVPpAZC8EjlUUpm95uJ1wNRi29lhu2I/export?format=csv&gid=0'
    df = pd.read_csv(url, usecols=[0,1,2,3,4], header=3)
    df['Time'] = pd.to_datetime(df['Time'], format='%B %d %Y')
    return df

st.title('Blance Sheet Visualization')
data_load_state = st.text('Loading data ...')
data = load_data()
data_load_state = st.text('Loading data ... done with catching')

def group_by_keyword(keyword, column_type):
    df_keyword = data[data['Items'].str.contains(keyword)]
    df_keyword[column_type] = df_keyword[column_type].astype(float)
    df_sort = sort_values_by_time(df_keyword, column_type)
    return df_sort

def group_by_column_type(column_type):
    df = data.drop(data[data[column_type] == ' '].index)
    df = df[df[column_type].notna()]
    df[column_type] = df[column_type].astype(float)
    df_sort = sort_values_by_time(df, column_type)
    return df_sort

def sort_values_by_time(data, column_type):
    df_groupby = (data.groupby(data['Time'].dt.strftime('%Y-%m'))
                      .agg(total = (column_type, 'sum'))
                      .reset_index())
    df_groupby['Time'] = pd.to_datetime(df_groupby['Time'], format='%Y-%m').dt.strftime('%Y-%m')
    df_groupby.sort_values(by='Time') 
    return df_groupby

def bar_chart_by_streamlit(keyword, column_type):
    df_keyword = group_by_keyword(keyword, column_type)
    st.write(keyword)
    st.bar_chart(df_keyword.set_index('Time'))

def bar_chart(column_type):
    df_column_type = group_by_column_type(column_type)
    st.write(column_type)
    st.bar_chart(df_column_type.set_index('Time'))

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data.tail(21))

if st.button("Clear All Cache"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()

bar_chart('Must Have')
bar_chart('Nice To Have')
bar_chart('Wasted')

bar_chart_by_streamlit("Tiền sinh hoạt chung cư", 'Must Have')
bar_chart_by_streamlit("Xăng jupiter", 'Must Have')
bar_chart_by_streamlit("Xăng lead", 'Must Have')
bar_chart_by_streamlit("Bánh căn", 'Must Have')

bar_chart_by_streamlit("Cắt tóc", 'Nice To Have')
bar_chart_by_streamlit("Vì tâm", 'Nice To Have')
bar_chart_by_streamlit("Dừa", 'Nice To Have')
bar_chart_by_streamlit("Vé số", 'Nice To Have')
bar_chart_by_streamlit("Bivina", 'Nice To Have')
bar_chart_by_streamlit("Cfe", 'Nice To Have')
bar_chart_by_streamlit("Trứng", 'Nice To Have')
bar_chart_by_streamlit("Lotte", 'Nice To Have')
bar_chart_by_streamlit("Winmart", 'Nice To Have')
