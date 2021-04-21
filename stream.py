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
 
df1 = pd.read_csv("set1.csv")
df2 = pd.read_csv("set2.csv")
df3 = pd.read_csv("set3.csv")
df4 = pd.read_csv("set4.csv")
df5 = pd.read_csv("set5.csv")
df6 = pd.read_csv("set6.csv")
df7_1 = pd.read_csv("set7_1.csv")
df7_2 = pd.read_csv("set7_2.csv")
df7_3 = pd.read_csv("set7_3.csv")
df7_4 = pd.read_csv("set7_4.csv")
df7_5 = pd.read_csv("set7_5.csv")
df8_1 = pd.read_csv("set8_1.csv")
df8_2 = pd.read_csv("set8_2.csv")
df8_3 = pd.read_csv("set8_3.csv")
df8_4 = pd.read_csv("set8_4.csv")
df8_5 = pd.read_csv("set8_5.csv")
df9_1 = pd.read_csv("set9_1.csv")
df9_2 = pd.read_csv("set9_2.csv")
df9_3 = pd.read_csv("set9_3.csv")
df9_4 = pd.read_csv("set9_4.csv")
df9_5 = pd.read_csv("set9_5.csv")
df10 = pd.read_csv("set10.csv")
df11 = pd.read_csv("set11.csv")
df12 = pd.read_csv("set12.csv")
df13 = pd.read_csv("set13.csv")

fig = px.line(df1, x="Year,month", y="Avg_leads", color="platform",color_discrete_sequence=px.colors.qualitative.Dark24,  height=600,width=900, 
              line_group="platform", hover_name="platform",title='Average Leads by monthly basis for platforms')
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)

fig = px.line(df2, x="Year,month", y="Leads_per_ad", color="platform",color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Leads per ad by monthly basis for platforms',
              line_group="platform", hover_name="platform")
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)

fig = px.bar(df3, x="Year,month", y="Avg_leads", color="channel_grouping",
             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Average Leads by monthly basis for channel groupings',)
st.plotly_chart(fig)

# fig = px.bar(df4, x="Year,month", y="Leads_per_ad", color="channel_grouping",
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Leads per ad by monthly basis for channel grouping')
# st.plotly_chart(fig)

# fig = px.line(df5, x="Year,month", y="Avg_leads", color="vertical",
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Average leads by monthly basis for Vertical',
#             line_group="vertical", hover_name="vertical")
# st.plotly_chart(fig)

# fig = px.line(df6, x="Year,month", y="Leads_per_ad", color="vertical",
#               color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900, title='Leads per ad by monthly basis for Vertical',
#               line_group="vertical", hover_name="vertical")
# st.plotly_chart(fig)

# fig = px.line(df7_1, x="Year,month", y="Avg_leads", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical - Auto', 
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df7_2, x="Year,month", y="Avg_leads", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical - Generalist', 
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)  

# fig = px.line(df7_3, x="Year,month", y="Avg_leads", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical - Jobs', 
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df7_4, x="Year,month", y="Avg_leads", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical - Services', 
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df7_5, x="Year,month", y="Avg_leads", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical - Property', 
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df8_1, x="Year,month", y="Leads_per_ad", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical [Ad Ratio] - Auto',
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df8_2, x="Year,month", y="Leads_per_ad", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical [Ad Ratio] - Generalist',
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df8_3, x="Year,month", y="Leads_per_ad", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical [Ad Ratio] - Jobs',
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df8_4, x="Year,month", y="Leads_per_ad", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical [Ad Ratio] - Services',
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.line(df8_5, x="Year,month", y="Leads_per_ad", color="seller_type",height=600,width=900,title = 'Seller type based on Vertical [Ad Ratio] - Property',
#               line_group="seller_type", hover_name="seller_type")
# st.plotly_chart(fig)

# fig = px.bar(df9_1, x="Year,month", y="Avg_leads", color="reply_type",title = 'Reply type based on vertical - Auto',
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900)
# st.plotly_chart(fig)

# fig = px.bar(df9_2, x="Year,month", y="Avg_leads", color="reply_type",title = 'Reply type based on vertical - Generalist',
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900)
# st.plotly_chart(fig)

# fig = px.bar(df9_3, x="Year,month", y="Avg_leads", color="reply_type",title = 'Reply type based on vertical - Jobs',
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900)
# st.plotly_chart(fig)

# fig = px.bar(df9_4, x="Year,month", y="Avg_leads", color="reply_type",title = 'Reply type based on vertical - Services',
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900)
# st.plotly_chart(fig)

# fig = px.bar(df9_5, x="Year,month", y="Avg_leads", color="reply_type",title = 'Reply type based on vertical - Property',
#             color_discrete_sequence=px.colors.qualitative.Dark24,height=600,width=900)
# st.plotly_chart(fig)

# st.subheader("Subcategory Breakdown Average Leads")
# subcategory = df10['subcategory']
# labels=subcategory[:43]
# for category in subcategory[:43]:
#     df_b=df10[df10['subcategory']==category]    
#     fig=px.line(df_b, x="Year,month", y="Avg_leads",labels="subcategory",height=600,width=900 ) 
#     st.write(category) 
#     st.plotly_chart(fig)

# st.subheader("Subcategory Breakdown Leads Per Ad")
# subcategory = df11['subcategory']
# labels=subcategory[:43]
# for category in subcategory[:43]:
#     df_b1=df11[df11['subcategory']==category]    
#     fig=px.line(df_b1, x="Year,month", y="Leads_per_ad",labels="subcategory",color_discrete_sequence=['red'],height=600,width=900) 
#     st.write(category) 
#     st.plotly_chart(fig)

# st.subheader("Region Breakdown Average Leads")
# region = df12['region']
# labels=region[:16]
# for regions in region[:16]:
#     df_b2=df12[df12['region']==regions]    
#     fig=px.line(df_b2, x="Year,month", y="Avg_leads",labels="region",color_discrete_sequence=['green'],height=600,width=900 ) 
#     st.write(regions)    
#     st.plotly_chart(fig)

# st.subheader("Region Breakdown Leads Per Ad")
# region = df13['region']
# labels=region[:16]
# for regions in region[:16]:
#     df_b3=df13[df13['region']==regions]    
#     fig=px.line(df_b3, x="Year,month", y="Leads_per_ad",labels="region",color_discrete_sequence=['purple'],height=600,width=900 ) 
#     st.write(regions)    
#     st.plotly_chart(fig)