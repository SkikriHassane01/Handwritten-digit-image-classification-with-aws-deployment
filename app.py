import streamlit as st 
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
# load the model 
model = load_model('best_model.keras')

# preprocess_image

def preprocess_image(image):
    image = ImageOps.grayscale(image)
    image = image.resize((28,28))
    image = ImageOps.invert(image)
    image = np.array(image)
    image = image / 255.0
    image = image.reshape(1,28,28,1)
    return image

st.title("Handwritten Digit Classifier✍️")
uploaded_file = st.file_uploader("Upload an image of a digit", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    image = preprocess_image(image)

    prediction = model.predict(image)
    predicted_digit = np.argmax(prediction)

    st.write(f"Predicted Digit:**{predicted_digit}**")