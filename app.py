import streamlit as st
from group_by import group_by_keyword

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

df_lotter = group_by_keyword("Lotte", 'Nice To Have')
st.write("Lotte")
st.bar_chart(df_lotter.set_index('Time'))

df_winmart = group_by_keyword("Winmart", 'Nice To Have')
st.write("Winmart")
st.bar_chart(df_winmart.set_index('Time'))