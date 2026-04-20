import streamlit as st
from api_calling import debug
from PIL import Image
st.title("AI Code Debugger")
st.markdown("Upload upto 3 images to debug your code")
st.divider()
with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload your code",
        type=['jpg','png','jpeg'],
        accept_multiple_files=True
    )
    if images:
        pil_img = []
        for i in images:
            pil_img.append(Image.open(i))
        if len(images) > 3:
            st.warning("You can upload at max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded images")
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    selected = st.selectbox(
        "Option bar",
        ["Hints","Solution with code"],
        index=None
    )
    btn = st.button("Debug Code",type="primary")
if btn:
    if not images:
        st.error("You must upload atleast 1 image")
    if not selected:
        st.error("You must select an option from option bar")
    with st.container(border=True):
        st.subheader("Your code")
        with st.spinner("AI is writing for you"):
            debug_code = debug(pil_img,selected)
            st.markdown(debug_code)