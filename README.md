# HDB Resale Flat Dashboard (2010–2019)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
</p>

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
