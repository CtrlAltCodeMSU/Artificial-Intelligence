import altair as alt
import pandas as pd

data = pd.read_csv('python.csv')
plot = alt.Chart(data).mark_bar().encode(
  x = 'Name:N',
  y = 'Age:Q'
)

plot.show()