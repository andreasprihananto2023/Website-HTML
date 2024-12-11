import streamlit as st
import cv2
import numpy as np
import base64

# Fungsi untuk mengompres gambar
@st.cache_data
def compress_image(image, max_size=(800, 800)):
    h, w = image.shape[:2]
    ratio = min(max_size[0]/w, max_size[1]/h)
    new_size = (int(w*ratio), int(h*ratio))
    return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

# Fungsi untuk mengkonversi gambar ke base64
def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

def main():
    # Tambahkan CSS eksternal
    st.markdown("""
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Judul Aplikasi
    st.title("Aplikasi Transformasi Gambar")

    # Sidebar untuk pengaturan
    with st.sidebar:
        st.header("Pilih Transformasi")
        transform_type = st.radio(
            "Jenis Transformasi",
            ['Translasi', 'Rotasi', 'Skala', 'Distorsi']
        )

    # Unggah file
    unggah_file = st.file_uploader(
        "Unggah gambar dalam format JPEG atau PNG", 
        type=["jpg", "jpeg", "png"]
    )

    if unggah_file is not None:
        # Baca dan kompres gambar
        file_bytes = np.asarray(bytearray(unggah_file.read()), dtype=np.uint8)
        gambar_asli = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        gambar_asli = compress_image(gambar_asli)

        # Konversi gambar ke base64
        base64_asli = image_to_base64(cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB))

        # Transformasi sesuai pilihan
        if transform_type == 'Translasi':
            dx = st.slider("Translasi Horizontal (dx)", -200, 200, 50)
            dy = st.slider("Translasi Vertikal (dy)", -200, 200, 30)
            
            matriks_translasi = np.float32([[1, 0, dx], [0, 1, dy]])
            gambar_transformasi = cv2.warpAffine(gambar_asli, matriks_translasi, (gambar_asli.shape[1], gambar_asli.shape[0]))
            base64_transformasi = image_to_base64(cv2.cvtColor(gambar_transformasi, cv2.COLOR_BGR2RGB))
            
            # Tampilkan gambar
            col1, col2 = st.columns(2)
            with col1:
                st.image(cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2RGB), caption="Gambar Asli")
            with col2:
                st.image(cv2.cvtColor(gambar_transformasi, cv2.COLOR_BGR2RGB), caption="Gambar Translasi")

        # Tambahkan logika serupa untuk transformasi lainnya
        # (Rotasi, Skala, Distorsi)

if __name__ == "__main__":
    main()