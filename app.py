import streamlit as st
from group_by import group_by_keyword, group_by_column_type

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

df_lotter = group_by_keyword("Lotte", 'Nice To Have')
st.write("Lotte")
st.bar_chart(df_lotter.set_index('Time'))

df_winmart = group_by_keyword("Winmart", 'Nice To Have')
st.write("Winmart")
st.bar_chart(df_winmart.set_index('Time'))