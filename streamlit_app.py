import streamlit as st
import pandas as pd
import numpy as np

#st.title("My new Streamlit app")
#st.write("Let's start building! For help and inspiration")
#st.text("Alpha Amadou BAH - Data Analyst")

#Styler
# st.title("Styler Example")
# dataframe = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write(chart_data)

st.line_chart(chart_data)