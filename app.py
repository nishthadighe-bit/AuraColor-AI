import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans

# Set page configuration
st.set_page_config(page_title="AuraColor AI", page_icon="🎨", layout="centered")

def extract_skin_tone(image_bytes):
    # Convert uploaded file to OpenCV format
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Select Region of Interest (Center of the image)
    h, w, _ = img.shape
    roi = img[h//4:h//2, w//3:2*w//3] 
    
    # Flatten pixels for K-Means
    pixels = roi.reshape(-1, 3)
    
    # Machine Learning: K-Means Clustering to find dominant skin color
    kmeans = KMeans(n_clusters=3, n_init=10)
    kmeans.fit(pixels)
    
    # Identify the cluster most likely to be skin
    dominant_color = kmeans.cluster_centers_[np.argmax(kmeans.cluster_centers_[:, 0])]
    return dominant_color.astype(int)

def get_season_details(rgb):
    r, g, b = rgb
    # Hue Analysis
    is_warm = r > b
    # Luminance Analysis
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
    is_light = brightness > 140

    if is_warm and is_light:
        return "Spring 🌸", ["#FEB2A8", "#FFD700", "#98FF98", "#FF7F50"], "Warm & Clear"
    elif is_warm and not is_light:
        return "Autumn 🍂", ["#8B4513", "#D2691E", "#556B2F", "#DAA520"], "Warm & Muted"
    elif not is_warm and is_light:
        return "Summer 🏖️", ["#E6E6FA", "#ADD8E6", "#FFB6C1", "#F0F8FF"], "Cool & Light"
    else:
        return "Winter ❄️", ["#000080", "#123524", "#4B0082", "#C0C0C0"], "Cool & Deep"

# UI Layout
st.title("🎨 AuraColor AI")
st.markdown("### Discover your Seasonal Palette using Computer Vision")
st.write("Upload a selfie to analyze your skin undertones using K-Means Clustering.")

uploaded_file = st.file_uploader("Choose a photo...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    with col2:
        with st.spinner('Analyzing color distributions...'):
            rgb = extract_skin_tone(uploaded_file.getvalue())
            season, palette, desc = get_season_details(rgb)
            
            st.success(f"Analysis Complete!")
            st.subheader(f"You are a {season}")
            st.info(f"**Profile:** {desc}")
            
            st.write("**Detected Skin Centroid:**")
            st.markdown(f'<div style="background-color: rgb({rgb[0]},{rgb[1]},{rgb[2]}); height: 40px; border-radius: 5px; border: 1px solid #ddd;"></div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("✨ Recommended Color Palette")
    p_cols = st.columns(4)
    for i, color in enumerate(palette):
        p_cols[i].markdown(f'<div style="background-color: {color}; height: 70px; border-radius: 10px;"></div>', unsafe_allow_html=True)
        p_cols[i].caption(color)

st.sidebar.markdown("---")
st.sidebar.write("Developed by a Data Science Student 🚀")
