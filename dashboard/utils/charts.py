import plotly.express as px

def plot_driver_gap_to_fastest(df, colors):

    # pastikan CONSTRUCTOR_ID jadi string biar cocok dengan dict key
    df["CONSTRUCTOR_ID"] = df["CONSTRUCTOR_ID"].astype(str)

    # sort dataframe berdasarkan gap
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
