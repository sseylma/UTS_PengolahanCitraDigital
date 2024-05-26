import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Fungsi-fungsi manipulasi gambar
def rgb_to_hsv(image):
    hsv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    return hsv_image

def calculate_histogram(image):
    histogram = cv2.calcHist([np.array(image)], [0], None, [256], [0, 256])
    return histogram

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    alpha = 1 + contrast / 127
    beta = brightness
    adjusted_image = cv2.convertScaleAbs(np.array(image), alpha=alpha, beta=beta)
    return adjusted_image

def find_contours(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    _, threshold = cv2.threshold(gray_image, 127, 255, 0)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# HTML dan CSS untuk latar belakang
page_bg_img = '''
<style>
body {
    background-image: url("https://images.pexels.com/photos/1234567/pexels-photo-1234567.jpeg");
    background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Halaman Data Diri Pribadi
st.title('Data Diri Pribadi')
st.subheader('Nama : Selma Ohoira')
st.subheader('NIM : 312210727')
st.subheader('Kelas : TI.22.C6')
st.subheader('Prodi : Teknik Informatika')

# Link Github langsung
st.markdown("[Github](https://github.com/sseylma/UTS_PengolahanCitraDigital.git)")

# Divider
st.write("---")

# Fitur manipulasi gambar
st.header("Image Manipulation")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Manipulasi RGB ke HSV
    st.subheader("RGB to HSV")
    hsv_image = rgb_to_hsv(image)
    st.image(hsv_image, caption="HSV Image", use_column_width=True)

    # Manipulasi Histogram
    st.subheader("Histogram")
    histogram = calculate_histogram(image)
    st.bar_chart(histogram)

    # Manipulasi Brightness and Contrast
    st.subheader("Brightness and Contrast")
    brightness = st.slider("Brightness", -100, 100, 0, key="brightness_slider")
    contrast = st.slider("Contrast", -100, 100, 0, key="contrast_slider")
    adjusted_image = adjust_brightness_contrast(image, brightness, contrast)
    st.image(adjusted_image, caption="Adjusted Image", use_column_width=True)

    # Manipulasi Contour
    st.subheader("Contour")
    contours = find_contours(image)
    image_with_contours = np.array(image)
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 3)
    st.image(image_with_contours, caption="Image with Contours", use_column_width=True)
