import streamlit as st

def header():
    st.markdown("<h1 class='main-title'>Medical Image Segmentation</h1>", unsafe_allow_html=True)
    

def upload_box():
    st.markdown("<div class='upload-card'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "📤 Upload a medical image (JPG, PNG)",
        type=["jpg", "jpeg", "png"]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    return uploaded_file
