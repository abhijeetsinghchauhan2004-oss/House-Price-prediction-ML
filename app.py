import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing

st.title('🏠 House Price prediction using ML')
st.image('https://i.pinimg.com/originals/9e/72/41/9e72419aa97348563f8f917f6b2ffe7b.gif')

