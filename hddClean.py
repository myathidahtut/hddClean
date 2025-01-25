import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("HDDclean.csv")

st.set_page_config(page_title="My HDD Clean Dashboard 2025", page_icon = ":bar_chart:", layout="wide")
st.sidebar.header('Please Filter Here')

town_name = st.sidebar.multiselect(
    "Select Town", 
    options = df['town'].unique(), 
    default = df['town'].unique()[:3]
)
street_name = st.sidebar.multiselect(
    "Select Street", 
    options = df['street_name'].unique(), 
    default = df['street_name'].unique()[:100]
)
flat_model_name = st.sidebar.multiselect(
    "Select Flat Type", 
    options = df['flat_type'].unique(), 
    default = df['flat_type'].unique()
)

st.title(":bar_chart: HDD Clean from 2010 to 2019")
st.markdown('##') # line spacing
total = df['remaining_lease'].sum()
st.subheader('Total Available')
st.subheader(f"{total} units")

df_select = df.query("town==@town_name and flat_type==@flat_model_name and street_name==@street_name")
a, b, c = st.columns(3)

aa = df_select.groupby('flat_type')['remaining_lease'].sum()
unit_by_flat = px.bar(
    aa,
    x = aa.values,
    y = aa.index,
    title = "Remaining Units by Flat Type"
)
a.plotly_chart(unit_by_flat, use_container_width=True)

unit_by_street = px.pie(
    df_select,
    values = 'remaining_lease',
    names = 'street_name',
    title = "Remaining Units by Street"
)
b.plotly_chart(unit_by_street, use_container_width=True)

cc = df_select.groupby('town')['remaining_lease'].sum()
unit_by_town = px.bar(
    cc,
    y = cc.values,
    x = cc.index,
    title = "Remaining Units by Town"
)
c.plotly_chart(unit_by_town, use_container_width=True)

d, e = st.columns(2)
dd = df_select.groupby('flat_type')['resale_price'].max()
line_fig_flat = px.line(
    dd,
    x = dd.values,
    y = dd.index,
    title = "Max Resale Price by Flat Type"
)
d.plotly_chart(line_fig_flat, use_container_width=True)

scatter_fig_town = px.scatter(
    df_select,
    x = 'resale_price',
    y = 'flat_type',
    title = "Resale Price by Flat Type"
)
e.plotly_chart(scatter_fig_town, use_container_width=True)