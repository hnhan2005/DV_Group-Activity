import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv('superstore.csv', encoding='latin1')

st.set_page_config(page_title="Group Activity", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center;'>Group Activity - Superstore</h1>", unsafe_allow_html=True)

# Hnhan
col1, col2 = st.columns(2)

with col1:
    profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()
    profit_by_region = profit_by_region.sort_values('Profit', ascending=False)
    
    st.write("**Regions:**")
    region_cols = st.columns(len(profit_by_region))
    selected_regions = []
    
    for idx, region in enumerate(profit_by_region['Region'].unique()):
        with region_cols[idx]:
            if st.checkbox(region, value=True):
                selected_regions.append(region)
    
    # Filter region
    filtered_profit = profit_by_region[profit_by_region['Region'].isin(selected_regions)]
    
    # The most profitable region
    if len(filtered_profit) > 0:
        max_profit_region = filtered_profit.loc[filtered_profit['Profit'].idxmax(), 'Region']
        
        colors = ['#D32F2F' if region == max_profit_region else '#D3D3D3' 
                  for region in filtered_profit['Region']]
        
        fig = go.Figure(
            data=go.Bar(
                x=filtered_profit['Region'],
                y=filtered_profit['Profit'],
                marker=dict(color=colors),
                text=filtered_profit['Profit'].round(2),
                textposition='auto'
            )
        )
        
        fig.update_layout(
            xaxis_title="Region",
            yaxis_title="Profit ($)",
            hovermode='x unified',
            height=350,
            margin=dict(l=40, r=40, t=40, b=40)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No regions selected!")

# Cuong
with col2:
    pass
