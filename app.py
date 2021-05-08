import streamlit as st
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import plotly.graph_objs as go
import cufflinks as cf
import pickle


register_matplotlib_converters()
# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
# plt.rcParams['figure.figsize'] = 15, 10

pd.options.plotting.backend = "plotly"

st.set_page_config(
    page_title="Used Car Price",
    # page_icon="FB",
    layout="wide",
    initial_sidebar_state="expanded",
)


np.random.seed(42)

# Add title, descriptions and image
st.title('Used Car Price Prediction')
st.markdown('''
- !!!!!! TO WRITE


- App built by [Anson](https://www.linkedin.com/in/ansonnn07/)
- Built with `Python`, using `streamlit`, `pandas`, `numpy`, `plotly`

**Links**: [GitHub](https://github.com/ansonnn07/Used-Car-Price-Prediction), 
[LinkedIn](https://www.linkedin.com/in/ansonnn07/),
[Kaggle](https://www.kaggle.com/ansonnn/code)
''')

st.markdown("""
""")

st.markdown('---')
