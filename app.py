import streamlit as st
#import numpy as np
from PIL import Image
from io import BytesIO
import plotly.express as px

from SRGANupscaling.main import super_resolution_model
from SRGANupscaling.params import MODEL
import tensorflow_hub as hub

import streamlit as st

st.set_page_config(
    page_title="Pixel Perfect",
    page_icon="💫",
    layout="wide",
    initial_sidebar_state="auto",
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('PIXEL PERFECT')
st.write('Upscale and enhance any image by using AI')

with st.sidebar:
    st.write("It can used for anything! From preserving old media material to \
            enhancing a microscope’s view, or identifying an individual in CCTV - \
            super-resolution’s impact is widespread and extremely evident.")
    st.image('static/super_resolution.png')
    with st.expander("How does it work?"):
        st.write("""
         To upscale your image, we use a SRGAN model to super-resolutionise your image with minimal information distortion.
        """)
    with st.expander("The Team:"):
        st.write("**Melissa Siddle**")
        st.write("https://github.com/melissasiddle")
        st.write("**Obakanyinsola Adegun**")
        st.write("https://github.com/Akanjii")
        st.write("**Pablo Gracia Diego**")
        st.write("https://github.com/Pablograciad")
        st.write("**Sridhar Ganesh Kumar**")
        st.write("https://github.com/sridhar211")

# Load the model (only executed once!)
@st.cache
def load_model():
	  return hub.load(MODEL)

model = load_model()

# st.header("Pixel Perfect")
# main_image = Image.open('static/main_banner.png')
# st.image(main_image,use_column_width='auto')
# st.title("Upscale and enhance any image by using our SRGAN model.")
# st.write("It can used for anything! From preserving old media material to \
#          enhancing a microscope’s view, or identifying an individual in CCTV - \
#          super-resolution’s impact is widespread and extremely evident.")


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# st.info("✨ It can used for anything! From preserving old media material to \
#          enhancing a microscope’s view, or identifying an individual in CCTV - \
#          super-resolution’s impact is widespread and extremely evident.😉")

uploaded_file = st.file_uploader("Upload Image 🚀", type=["png","jpg","bmp","jpeg"])

if uploaded_file is not None:
    col1, col2 = st.columns([1,1])

    #src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)

    with col1:
        st.markdown("---")
        fig = px.imshow(image)
        fig.update_layout(width=500, height=600, margin=dict(l=1, r=1, b=1, t=1))
        fig.update_layout(hovermode=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        st.plotly_chart(fig, use_container_width=True)
        #st.image(image, caption='Input Image', use_column_width=True)

    #st.write(os.listdir())

    with col2:

        st.markdown("---")
        im = super_resolution_model(image, model)
        fig = px.imshow(im)
        fig.update_layout(width=500, height=600, margin=dict(l=1, r=1, b=1, t=1))
        fig.update_layout(hovermode=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        st.plotly_chart(fig, use_container_width=True)
        #st.image(im, caption='Output Image', use_column_width=True)

    # Convert Image?

    # if im.mode in ("RGBA", "P"):
    #     im = im.convert("RGB")

    rgb_im = im.convert('RGB')
    buf = BytesIO()
    rgb_im.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    if st.download_button(
      label="Download Image ",
      data=byte_im,
      file_name=str("super " + uploaded_file.name),
      mime="image/jpeg",

      ):

        st.balloons()
        st.success('✅ Download Successful !!')

# else:
#     st.warning('⚠ Please upload your Image file 😯')

# import time

# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete + 1)



st.markdown("<br><hr><center>Enjoy ❤️</center><hr>", unsafe_allow_html=True)
