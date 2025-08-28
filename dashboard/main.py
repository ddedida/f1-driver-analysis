import streamlit as st
import pandas as pd
from utils.charts import plot_driver_gap_to_fastest
from utils.colors import constructor_colors
from utils.charts import chart_driver_teammate_comparison
from utils.charts import chart_driver_lap_time

def gap_to_fastest():
    df = pd.read_csv("../data/visualization/driver_avg_pace_with_gap.csv")

    selected_year = st.selectbox("Select Year", sorted(df["YEAR"].unique(), reverse=True), key="gap_year")
    race_df = df[df["YEAR"] == selected_year]
    selected_race = st.selectbox("Select Race", sorted(race_df["RACE"].unique()), key="gap_race")
    race_df = race_df[race_df["RACE"] == selected_race]

    st.plotly_chart(plot_driver_gap_to_fastest(race_df, constructor_colors))

def driver_teammate_comparison():
    df = pd.read_csv("../data/visualization/driver_teammate_comparison.csv")

    selected_driver = st.selectbox("Select Driver for Comparison", df["DRIVER"].unique(), key="teammate_driver")
    
    driver_df = df[df["DRIVER"] == selected_driver].copy()
    driver_df["TOTAL_POINTS"] = driver_df["DRIVER_POINTS"] + driver_df["TEAMMATE_POINTS"]

    st.altair_chart(chart_driver_teammate_comparison(driver_df, selected_driver), use_container_width=True)

def driver_lap_time():
    df = pd.read_csv("../data/visualization/driver_lap_time.csv")

    selected_year = st.selectbox("Select Year", sorted(df["YEAR"].unique(), reverse=True), key="lap_year")
    race_df = df[df["YEAR"] == selected_year]
    selected_race = st.selectbox("Select Race", sorted(race_df["RACE"].unique()), key="lap_race")
    race_df = race_df[race_df["RACE"] == selected_race]

    st.plotly_chart(chart_driver_lap_time(race_df))

if __name__ == "__main__":
    st.title("F1 Driver Performance Tracker")

    st.subheader("Driver Average Pace Gap to Fastest")
    gap_to_fastest()

    st.subheader("Driver Position Evolution Each Lap")
    driver_lap_time()

    st.subheader("Driver Teammate Comparison")
    driver_teammate_comparison()
