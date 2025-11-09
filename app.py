import streamlit as st
from PIL import Image
import numpy as np
import cv2

from ui.components import header, upload_box
from utils.processing import process_image

# Page setup
st.set_page_config(
    page_title="Medical Image Segmentation",
    page_icon="🧠",
    layout="centered"
)

# Load custom CSS
with open("ui/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI Header
header()

# Upload area
uploaded_file = upload_box()

if uploaded_file:
    image = np.array(Image.open(uploaded_file).convert("L"))

    resized_input, segmented = process_image(image)

    col1, col2 = st.columns(2)

    with col1:
        st.image(resized_input, caption="Original Image", use_container_width=True)

    with col2:
        st.image(segmented, caption="Segmented Output", use_container_width=True)

else:
    st.markdown(
        "<p class='note'>👉 Upload a image to start segmentation.</p>",
        unsafe_allow_html=True
    )
