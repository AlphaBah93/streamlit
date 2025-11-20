import streamlit as st
import pandas as pd
import numpy as np

#st.title("My new Streamlit app")
#st.write("Let's start building! For help and inspiration")
#st.text("Alpha Amadou BAH - Data Analyst")

#Styler ------------------
# st.title("Styler Example")
# dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))

# Line chart with Styler ------------------
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# st.write(chart_data.style.highlight_max(axis=0))
# st.line_chart(chart_data)

# Map with Styler ------------------
# st.title("Map Example")
# map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
# st.map(map_data)

x = st.slider('x', 0, 200, 25, step=2)  # 👈 this is a widget
st.write(x, 'squared is', x * x)