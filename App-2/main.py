import streamlit as st
import pandas


st.set_page_config(layout="wide")
st.header("The Best Company")
content1 = ("Lila is introspective and warm, often described as the “human embodiment of lavender.” She journals every "
            "night, rides a bright yellow vintage bike named “Marigold,” and loves early mornings at farmer’s "
            "markets. She doesn’t own a TV, but she’s obsessed with old radio dramas and records her own podcast "
            "called “The Buzzline”, where she interviews urban farmers, scientists, and sustainability advocates. "
            "Last year, Lila spent a month in New Zealand studying Apis mellifera populations and indigenous Māori "
            "beekeeping practices. She brought back seeds from local plants (where legal) and started a "
            "“sister-garden” in her hometown. She also survived a surprise thunderstorm while checking on a "
            "mountaintop hive in Oregon—an experience that she says made her feel “infinitely small and deeply "
            "grateful.")

st.write(content1)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("App-2/data-2.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("App-2/images-2/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("App-2/images-2/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("App-2/images-2/" + row["image"])
