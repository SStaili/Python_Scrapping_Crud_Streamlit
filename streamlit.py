import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd
import pdfplumber
import PyPDF2
import nltk
from rake_nltk import Rake
import string
import io
import re

nltk.download('stopwords')
nltk.download('punkt')
import lxml



def load_data():
    data = pd.read_csv('razer_computer.csv')

    return data

df = load_data()
df.drop(['Unnamed: 0'],axis=1)

st.dataframe(df)

