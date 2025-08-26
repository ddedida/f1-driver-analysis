import plotly.express as px
import altair as alt
import pandas as pd

def plot_driver_gap_to_fastest(df, colors):
    df["CONSTRUCTOR_ID"] = df["CONSTRUCTOR_ID"].astype(str)

    df = df.sort_values("GAP_TO_FASTEST", ascending=True)

    fig = px.bar(
        df,
        x="DRIVER_CODE",
        y="GAP_TO_FASTEST",
        color="CONSTRUCTOR_ID",
        color_discrete_map=colors,
        text="GAP_TO_FASTEST",
        category_orders={"DRIVER_CODE": df["DRIVER_CODE"].tolist()}  # 👈 kunci urutan
    )

    fig.update_traces(
        texttemplate='%{text:.3f}',
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title="Driver",
        yaxis_title="Gap in Race Pace",
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        showlegend=False,
        bargap=0.2,
        height=500
    )

    return fig

def chart_driver_teammate_comparison(df, selected_driver):
    df_long = pd.melt(
        df,
        id_vars=["TEAMMATE"],
        value_vars=["DRIVER_POINTS", "TEAMMATE_POINTS"],
        var_name="ROLE",
        value_name="POINTS"
    )

    df_long["PERCENT"] = df_long.apply(
        lambda row: row["POINTS"] / df_long.loc[df_long["TEAMMATE"] == row["TEAMMATE"], "POINTS"].sum() * 100,
        axis=1
    )

    df_long["ROLE"] = df_long["ROLE"].replace({"DRIVER_POINTS": "Driver", "TEAMMATE_POINTS": "Teammate"})

    chart = alt.Chart(df_long).mark_bar().encode(
        y=alt.Y('TEAMMATE:N', sort='-x', title='Teammate'),
        x=alt.X('PERCENT:Q', stack='normalize', title='Percentage of Points'),
        color=alt.Color('ROLE:N', scale=alt.Scale(scheme="category10")),
        tooltip=['TEAMMATE', 'ROLE', 'POINTS', 'PERCENT']
    ).properties(
        title=f"{selected_driver} vs Teammate Points Comparison"
    )

    return chart