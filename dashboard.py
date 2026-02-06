import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Hoạt động nhóm", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
    }
    h1 {
        margin: 2.0rem 0 !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv('superstore.csv', encoding='latin1')

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')


st.markdown("<h1 style='text-align: center;'>Hoạt động nhóm - Superstore</h1>", unsafe_allow_html=True)

col1, _, col2 = st.columns([1, 0.1, 1])

with col1:
    # Filter date
    date_col1, date_col2 = st.columns(2)
    with date_col1:
        start_date = st.date_input("**Ngày bắt đầu**", value=df['Order Date'].min(), min_value=df['Order Date'].min(), max_value=df['Order Date'].max())
    
    with date_col2:
        end_date = st.date_input("**Ngày kết thúc**", value=df['Order Date'].max(), min_value=df['Order Date'].min(), max_value=df['Order Date'].max())
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    if start_date <= end_date:
        profit_by_date = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
        
        profit_by_region = profit_by_date.groupby('Region')['Profit'].sum().reset_index()
        profit_by_region = profit_by_region.sort_values('Profit', ascending=False)
        
        st.write("**Khu vực:**")
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
                    textposition='outside'
                )
            )
            
            fig.update_layout(
                title=dict(
                    text="Lợi nhuận theo khu vực",
                    x=0.5,
                    xanchor='center',
                ),
                yaxis=dict(range=[0, 120000]),
                xaxis_title="Khu vực",
                yaxis_title="Lợi nhuận ($)",
                hovermode='x unified',
                height=400,
                margin=dict(l=50, r=50, t=80, b=50)
            )
            
            st.plotly_chart(fig, width="stretch")
        else:
            st.warning("Chưa chọn khu vực nào!")
    else:
        st.warning("Ngày bắt đầu phải trước ngày kết thúc!")

# Cuong
with col2:
    sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
    sales_by_category = sales_by_category.sort_values('Sales', ascending=False)
    
    st.write("**Danh mục sản phẩm:**")
    category_cols = st.columns(len(sales_by_category))
    selected_categories = []
    
    for idx, category in enumerate(sales_by_category['Category'].unique()):
        with category_cols[idx]:
            if st.checkbox(category, value=True, key=f"cat_{category}"):
                selected_categories.append(category)
    
    # filter 
    filtered_sales = sales_by_category[sales_by_category['Category'].isin(selected_categories)]
    
    # sale distribution 
    if len(filtered_sales) > 0:
        colors_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        
        fig = go.Figure(
            data=go.Pie(
                labels=filtered_sales['Category'],
                values=filtered_sales['Sales'],
                hole=0.4,
                marker=dict(colors=colors_palette[:len(filtered_sales)]),
                textinfo='label+percent',
                textposition='auto',
                hovertemplate='<b>%{label}</b><br>Doanh thu: $%{value:,.2f}<br>Phần trăm: %{percent}<extra></extra>'
            )
        )
        
        fig.update_layout(
            title=dict(
                text="Phân bố Doanh thu theo danh mục",
                x=0.5,
                xanchor='center'
            ),
            height=400,
            margin=dict(l=40, r=40, t=60, b=40),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )
        
        st.plotly_chart(fig, width="stretch")
    else:
        st.warning("Chưa chọn danh mục nào!")
