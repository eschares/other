# Plot 100m and 200m data
# Eric Schares
# April 8, 2024

import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown('# 4A 100m and 200m times')

# 100m times
st.markdown("""---""")
st.header('100m times')

'https://www.gobound.com/ia/ihsaa/boystrack/2023-24/leaderlist?competitor=athlete&range=comp&idGroup=h2024032603035787461b7744e87c643&idMetricGroup=h2020020309584653664580f3c421b46&page=1&block=total'

df = pd.read_csv('4A_100mtimes_040824.csv')

fig = px.scatter(df, x='Rank', y='Time',
                 hover_name='Athlete Name',
                 hover_data=['School'],
                 color='Year',
                 category_orders={'Year': ['SR', 'JR', 'SO', 'FR']},
                 # color_discrete_sequence=['blue', 'red', 'green', 'orange']
                 )

fig.update_layout(
    title_text='Boys 4A 100m times - as of April 8, 2024; Jeffrey T27th at 11.23')

fig.add_annotation(x=27, y=11.23,
                   text="Jeffrey Roberts",
                   # showarrow=False,
                   ay=-20,
                   arrowhead=0)
st.plotly_chart(fig, use_container_width=True)


fig = px.scatter(df, x='Athlete Name', y='Time',
                 hover_name='Athlete Name',
                 hover_data=['School'],
                 color='Year',
                 category_orders={'Year': ['SR', 'JR', 'SO', 'FR']},
                 # color_discrete_sequence=['blue', 'red', 'green', 'orange']
                 )

fig.update_layout(title_text='Boys 4A 100m times - as of April 8, 2024')
fig.add_annotation(x='Jeffrey Roberts', y=11.23,
                   text="Jeffrey Roberts",
                   # showarrow=False,
                   ay=-10,
                   arrowhead=0)

st.plotly_chart(fig)



# 200m times
st.markdown("""---""")
st.header('200m')

'https://www.gobound.com/ia/ihsaa/boystrack/2023-24/leaderlist?competitor=athlete&range=comp&idGroup=h2024032603035787461b7744e87c643&idMetricGroup=h20200203095847599efc1b1e3dfdb4d&page=1&block=total'
df = pd.read_csv('4A_200mtimes_040824.csv')

fig = px.scatter(df, x='Rank', y='Time',
                 hover_name='Athlete Name',
                 hover_data=['School'],
                 color='Year',
                 category_orders={'Year': ['SR', 'JR', 'SO', 'FR']},
                 # color_discrete_sequence=['blue', 'red', 'green', 'orange']
                 )

fig.update_layout(
    title_text='Boys 4A 200m times - as of April 8, 2024; Jeffrey 14th at 22.64')

fig.add_annotation(x=14, y=22.64,
                   text="Jeffrey Roberts",
                   # showarrow=False,
                   ay=-30,
                   arrowhead=0)
st.plotly_chart(fig)

fig = px.scatter(df, x='Athlete Name', y='Time',
                 hover_name='Athlete Name',
                 hover_data=['School'],
                 color='Year',
                 category_orders={'Year': ['SR', 'JR', 'SO', 'FR']},
                 # color_discrete_sequence=['blue', 'red', 'green', 'orange']
                 )

fig.update_layout(title_text='Boys 4A 200m times - as of April 8, 2024')
fig.add_annotation(x='Jeffrey Roberts', y=22.64,
                   text="Jeffrey Roberts",
                   # showarrow=False,
                   ay=-20,
                   arrowhead=0)

st.plotly_chart(fig)
