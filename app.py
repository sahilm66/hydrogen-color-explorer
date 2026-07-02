import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Hydrogen Colour Explorer")
st.write("Comparing hydrogen production pathways across cost, emissions and maturity.")

df = pd.read_excel(r"C:\Hydrogen Research\03_Data\Raw_Originals\H2_Colour_Explorer_Data.xlsx", sheet_name="H2 Colour Data", header=3)

df = df.dropna(how='all', axis=1)
df = df.dropna(how='all', axis=0)
df.columns = df.columns.str.replace('\n', ' ', regex=False).str.strip()

colour_col = "Colour Name (e.g. Green, Grey, Blue)"
lcoh_col = "LCOH Central $/kgH₂"
gwp_col = "GWP100 kgCO₂eq/kgH₂"

st.sidebar.title("Filters")
colour = st.sidebar.selectbox("Filter by Colour", options=["All"] + list(df[colour_col].dropna().unique()))

if colour != "All":
    df = df[df[colour_col] == colour]

st.dataframe(df)

chart_df = df[[colour_col, lcoh_col]].dropna()
fig = px.bar(chart_df, x=colour_col, y=lcoh_col, title="LCOH by Hydrogen Colour ($/kgH₂)", labels={colour_col: "Colour", lcoh_col: "LCOH ($/kg)"})
st.plotly_chart(fig)

gwp_df = df[[colour_col, gwp_col]].dropna()
fig2 = px.bar(gwp_df, x=colour_col, y=gwp_col, title="GWP100 by Hydrogen Colour (kgCO₂eq/kgH₂)", labels={colour_col: "Colour", gwp_col: "GWP100 (kgCO₂eq/kg)"})
st.plotly_chart(fig2)   