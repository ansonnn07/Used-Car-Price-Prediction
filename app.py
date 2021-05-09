import json
from collections import deque

import cufflinks as cf
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import streamlit as st
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
# plt.rcParams['figure.figsize'] = 15, 10

pd.options.plotting.backend = "plotly"

st.set_page_config(
    page_title="Used Car Price",
    # page_icon="FB",
    # layout="wide",
    initial_sidebar_state="expanded",
)

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


def get_label(feature):
    label = str(feature)
    if label.find('_') != -1:
        label = ' '.join(label.split('_')).capitalize()
    else:
        label = label.capitalize()
    return label


model = joblib.load('model_pipe.joblib')

col_ranges = json.load(open('data//col_range.json', 'r'))
cats = ['manufacturer', 'condition', 'cylinders', 'fuel',
        'title_status', 'transmission', 'drive', 'type', 'paint_color']
nums = ['price', 'year', 'odometer', 'lat', 'long']
form_value_dict = {}

st.sidebar.header('Selections')
with st.sidebar.form("selection_form"):
    for feature, feat_range in col_ranges.items():
        if feature == 'price':
            continue

        label = get_label(feature)
        if feature in nums:
            min_value = int(feat_range[0])
            max_value = int(feat_range[-1])
            default_value = None
            step = 1000 if feature == 'odometer' else 1
            if feature in ('lat', 'long'):
                help_text = f'{label + "ititude"} of the listing.'
            else:
                help_text = None
            selected = st.slider(f'{label}', min_value, max_value,
                                 default_value, step, '%i', help=help_text)
            form_value_dict[feature] = [selected]
        else:
            current_range = sorted(feat_range)
            if 'other' in current_range:
                # Rearrange the 'other' to put at the last
                current_range.remove('other')
                current_range.append('other')
            if 'unknown' in current_range:
                # current_range = deque(current_range)
                # Rearrange the 'Unknown' to put at the last
                current_range.remove('unknown')
                current_range.append('unknown')
            current_range = [text.capitalize() for text in current_range]
            default_idx = 0
            selected = st.selectbox(f'{label}', options=current_range,
                                    index=default_idx)
            form_value_dict[feature] = [selected]

    submitted = st.form_submit_button("Predict!")

st.header("Explanations of the attributes of the used car")
st.markdown("""
- **Year**: Year of the vehicle
- **Odometer**: Miles traveled by the vehicle
- **Lat**: Latitude of the listing
- **Long**: Longitude of the listing
- **Manufacturer**: Manufacturer of the vehicle
- **Condition**: Condition of the vehicle
- **Cylinders**: Number of cylinders
- **Fuel**: Fuel type
- **Title status**: Title status of the vehicle
- **Transmission**: Transmission type of the vehicle
- **Drive**: Type of wheel drive
- **Type**: Generic type of the vehicle
- **Paint color**: Color of the vehicle
""")

st.markdown("---")


if submitted:
    selected_values = pd.DataFrame.from_dict(form_value_dict)
    pred = model.predict(selected_values).flatten()[0]
    st.success(f"""The predicted price is ${pred:,.2f} !""")
else:
    st.info("""Press the 'Predict!' button after you have selected the values at the sidebar 
    to predict the used car price!""")
