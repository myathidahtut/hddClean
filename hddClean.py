"""Streamlit dashboard for exploring Singapore HDB resale flat transactions, 2010-2019."""
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("HDDclean.csv")

st.set_page_config(page_title="HDB Resale Flat Dashboard", page_icon=":bar_chart:", layout="wide")
st.sidebar.header("Filter Here")

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

st.title(":bar_chart: HDB Resale Flat Prices, 2010-2019")
st.markdown("##")  # line spacing
total_units = df["remaining_lease"].sum()
st.subheader("Total Available")
st.subheader(f"{total_units} units")

df_select = df.query("town==@town_name and flat_type==@flat_model_name and street_name==@street_name")
col1, col2, col3 = st.columns(3)

units_by_flat_type = df_select.groupby("flat_type")["remaining_lease"].sum()
unit_by_flat = px.bar(
    units_by_flat_type,
    x=units_by_flat_type.values,
    y=units_by_flat_type.index,
    title="Remaining Units by Flat Type"
)
col1.plotly_chart(unit_by_flat, use_container_width=True)

unit_by_street = px.pie(
    df_select,
    values="remaining_lease",
    names="street_name",
    title="Remaining Units by Street"
)
col2.plotly_chart(unit_by_street, use_container_width=True)

units_by_town = df_select.groupby("town")["remaining_lease"].sum()
unit_by_town = px.bar(
    units_by_town,
    y=units_by_town.values,
    x=units_by_town.index,
    title="Remaining Units by Town"
)
col3.plotly_chart(unit_by_town, use_container_width=True)

col4, col5 = st.columns(2)
max_price_by_flat_type = df_select.groupby("flat_type")["resale_price"].max()
line_fig_flat = px.line(
    max_price_by_flat_type,
    x=max_price_by_flat_type.values,
    y=max_price_by_flat_type.index,
    title="Max Resale Price by Flat Type"
)
col4.plotly_chart(line_fig_flat, use_container_width=True)

scatter_fig_town = px.scatter(
    df_select,
    x="resale_price",
    y="flat_type",
    title="Resale Price by Flat Type"
)
col5.plotly_chart(scatter_fig_town, use_container_width=True)