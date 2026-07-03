# HDB Resale Flat Dashboard (2010–2019)

An interactive Streamlit dashboard for exploring Singapore HDB (public housing) resale flat transactions from 2010 to 2019 — filter by town, street, and flat type, and compare unit availability and resale prices across the dataset.

## Data

~213,000 resale transactions with fields including `town`, `street_name`, `flat_type`, `flat_model`, `storey_range`, `floor_area_sqm`, `lease_commence_date`, `remaining_lease`, and `resale_price`.

## Features

- Sidebar filters for town, street, and flat type
- Remaining lease units by flat type and by town (bar charts)
- Remaining lease units by street (pie chart)
- Max resale price by flat type (line chart)
- Resale price vs. flat type (scatter plot)

## Tools

Python, pandas, Streamlit, Plotly Express

## Run it locally

```bash
pip install -r requirements.txt
streamlit run hddClean.py
```
