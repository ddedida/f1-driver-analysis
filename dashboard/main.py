import streamlit as st
import pandas as pd
from utils.charts import plot_driver_gap_to_fastest
from utils.colors import constructor_colors
from utils.charts import chart_driver_teammate_comparison

def gap_to_fastest():
    df = pd.read_csv("../data/visualization/driver_avg_pace_with_gap.csv")

    selected_year = st.selectbox("Select Year", sorted(df["YEAR"].unique(), reverse=True))

    race_df = df[df["YEAR"] == selected_year]
    selected_race = st.selectbox("Select Race", sorted(race_df["RACE"].unique()))
    race_df = race_df[race_df["RACE"] == selected_race]

    st.plotly_chart(plot_driver_gap_to_fastest(race_df, constructor_colors))

def driver_teammate_comparison():
    df = pd.read_csv("../data/visualization/driver_teammate_comparison.csv")

    selected_driver = st.selectbox("Select Driver for Comparison", df["DRIVER"].unique())
    
    driver_df = df[df["DRIVER"] == selected_driver].copy()
    driver_df["TOTAL_POINTS"] = driver_df["DRIVER_POINTS"] + driver_df["TEAMMATE_POINTS"]

    st.altair_chart(chart_driver_teammate_comparison(driver_df, selected_driver), use_container_width=True)

if __name__ == "__main__":
    st.title("F1 Driver Performance Tracker")

    # Gap to Fastest
    gap_to_fastest()

    # Driver Teammate Comparison
    driver_teammate_comparison()