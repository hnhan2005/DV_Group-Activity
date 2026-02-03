import streamlit as st

tab_dashboard = st.Page("dashboard.py", title="Dashboard", icon="📊")
tab_comment = st.Page("comment.py", title="Comments", icon="✍️")

pg = st.navigation([tab_dashboard, tab_comment])

st.set_page_config(page_title="Group Activity", page_icon="🎓")

pg.run()