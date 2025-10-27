import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
import joblib

# Load model
clf = joblib.load("mnist_model.pkl")

st.title("Digit-2 Detector using Logistic Regression and MNIST Dataset")

# Canvas configuration
canvas_result = st_canvas(
    stroke_width=15,
    stroke_color="#000000",     # black stroke
    background_color="#FFFFFF", # white background
    update_streamlit=True,
    height=280,
    width=280,
    key="canvas",
)

if st.button("Predict"):
    if canvas_result.image_data is None:
        st.write("Draw something first.")
    else:
        # Convert numpy RGBA image to grayscale PIL
        img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA').convert('L')
        # Resize to 28x28
        img = img.resize((28, 28), Image.Resampling.LANCZOS)

        # Convert to numpy array
        arr = np.array(img)

        # Invert colors because typical canvas: black stroke on white background,
        # MNIST has white-ish foreground on dark background; many models trained
        # on raw pixels still work with simple inversion.
        arr = 255 - arr

        # Flatten & reshape for sklearn
        X = arr.reshape(1, -1)

        pred = clf.predict(X)[0]
        st.image(img, caption="28x28 (resized)", use_container_width=True)
        st.success(f"Predicted digit: {pred}")
