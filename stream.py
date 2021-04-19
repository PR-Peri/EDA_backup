
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.io as pio
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
 
dfa = pd.read_csv("set1.csv")
dfb = pd.read_csv("set2.csv")


fig = px.line(dfa, x="Year,month", y="Avg_leads", color="platform",color_discrete_sequence=px.colors.qualitative.Dark24,  height=600,width=900, 
              line_group="platform", hover_name="platform",title='Average Leads by monthly basis for platforms')
#fig.show()
st.plotly_chart(fig)

fig = px.line(dfb, x="Year,month", y="Leads_per_ad", color="platform",color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Leads per ad by monthly basis for platforms',
              line_group="platform", hover_name="platform")
#fig.show()
st.plotly_chart(fig)
