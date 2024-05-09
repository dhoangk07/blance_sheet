import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    url = 'https://docs.google.com/spreadsheets/d/1YAEnVA0NlZJXOVPpAZC8EjlUUpm95uJ1wNRi29lhu2I/export?format=csv&gid=0'
    df = pd.read_csv(url, usecols=[0,1,2,3,4], header=3)
    df['Time'] = pd.to_datetime(df['Time'], format='%B %d %Y')
    return df

data_load_state = st.text('Loading data ...')

data = load_data()

data_load_state = st.text('Loading data ... done with catching')

def group_by_keyword(keyword, column_type):
    df_keyword = data[data['Items'].str.contains(keyword)]
    df_keyword[column_type] = df_keyword[column_type].astype(int)
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

st.header('Blance Sheet Visualization')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data.tail(21))

df_must_have = group_by_column_type('Must Have')
st.write("Must Have")
st.bar_chart(df_must_have.set_index('Time'))

df_nice_to_have = group_by_column_type('Nice To Have')
st.write("Nice To Have")
st.bar_chart(df_nice_to_have.set_index('Time'))

df_wasted = group_by_column_type('Wasted')
st.write("Wasted")
st.bar_chart(df_wasted.set_index('Time'))

df_xang_jupiter = group_by_keyword("Xăng jupiter", 'Must Have')
st.write("Xăng jupiter")
st.bar_chart(df_xang_jupiter.set_index('Time'))

df_xang_lead = group_by_keyword("Xăng lead", 'Must Have')
st.write("Xăng lead")
st.bar_chart(df_xang_lead.set_index('Time'))

df_vi_tam = group_by_keyword("Vì tâm", 'Nice To Have')
st.write("Vì tâm")
st.bar_chart(df_vi_tam.set_index('Time'))

df_dua = group_by_keyword("Dừa", 'Nice To Have')
st.write("Dừa")
st.bar_chart(df_dua.set_index('Time'))

df_ve_so = group_by_keyword("Vé số", 'Nice To Have')
st.write("Vé số")
st.bar_chart(df_ve_so.set_index('Time'))

df_bivina = group_by_keyword("Bivina", 'Nice To Have')
st.write("Bivina")
st.bar_chart(df_bivina.set_index('Time'))

df_banhcan = group_by_keyword("Bánh căn", 'Must Have')
st.write("Bánh căn")
st.bar_chart(df_banhcan.set_index('Time'))

df_cfe = group_by_keyword("Cfe", 'Nice To Have')
st.write("Cfe")
st.bar_chart(df_cfe.set_index('Time'))

df_trung = group_by_keyword("Trứng", 'Nice To Have')
st.write("Trứng")
st.bar_chart(df_trung.set_index('Time'))

df_lotter = group_by_keyword("Lotte", 'Nice To Have')
st.write("Lotte")
st.bar_chart(df_lotter.set_index('Time'))

df_winmart = group_by_keyword("Winmart", 'Nice To Have')
st.write("Winmart")
st.bar_chart(df_winmart.set_index('Time'))