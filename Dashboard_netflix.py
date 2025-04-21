import networkx as nx
import streamlit as st
import matplotlib as plt
import seaborn as sns

import pandas as pd
import numpy as np
import plotly.express as px


# Streamlit Dashboard
st.title('Netflix Data Dashboard')
st.plotly_chart(fig_time_series)
st.plotly_chart(fig_geo)
st.write('### Top 10 Directors')
st.bar_chart(top_directors)
st.pyplot()