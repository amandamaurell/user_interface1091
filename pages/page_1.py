import streamlit as st
import requests

gif = st.text_input("Tell me what gif you would like to see...", value='dog')

url = "https://api.giphy.com/v1/gifs/search"

params={
    'api_key':st.secrets["api_key"],
    'q':gif
}

response = requests.get(url, params=params).json()

giphy = response['data'][0]['embed_url']

st.write(f"<iframe src={giphy} >", unsafe_allow_html=True)
