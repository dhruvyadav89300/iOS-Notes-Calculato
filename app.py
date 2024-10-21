from PIL import Image
import streamlit as st
from gemini_calculator import calculate
from canvas import Canvas

st.set_page_config(layout="wide")

st.title("iOS Notes Calculator Demo")
data = Canvas()
run = st.button("Run")


if data.image_data is not None and run:
    img = Image.fromarray(data.image_data.astype('uint8'), 'RGBA')
    ans = calculate(image=img)
    st.write_stream(ans)
