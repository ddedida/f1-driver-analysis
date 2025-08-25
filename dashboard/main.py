import streamlit as st
import pandas as pd
from utils.charts import plot_driver_gap_to_fastest
from utils.colors import constructor_colors

st.title("F1 Driver Performance Tracker")
st.write("Hello F1 Fans!")

st.write("## Driver Performance Data")

df = pd.read_csv("../data/visualization/2025-08-21.csv")

years = df["YEAR"].unique()
selected_year = st.selectbox("Select Year", sorted(years, reverse=True))

race_df = df[df["YEAR"] == selected_year]

races = race_df["RACE"].unique()
selected_race = st.selectbox("Select Race", sorted(races))

race_df = race_df[race_df["RACE"] == selected_race]

st.plotly_chart(plot_driver_gap_to_fastest(race_df, constructor_colors))
