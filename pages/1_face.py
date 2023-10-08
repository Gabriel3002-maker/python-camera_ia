import cv2
import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Cámara IA Face😎")
st.markdown("# Cámara Face😎")
st.sidebar.header("Cámara Face😎")
st.write("""
    Hola chicos, esta es una cámara con inteligencia artificial que permite la detección de caras humanas
""")

with st.spinner('Por favor, espere'):
    time.sleep(2)
st.success('¡Hecho!')

# Cargamos el clasificador de caras (smile en este caso)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Funcino para inicializar y obtener la camara
def get_camera():
    cap = cv2.VideoCapture(0)
    return cap


#Detectar caras en un frame
def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img

cap = get_camera()

# Configurar el widget de Streamlit para mostrar el video
video_display = st.image([], channels='BGR')

def clean():
    st.experimental_set_query_params(camera_closed=True)
    cap.release()
    cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    
    # Comprobar si la captura de video se realizó correctamente
    if not ret:
        break
    
    frame = detect_faces(frame)

    # Mostrar el video en Streamlit
    video_display.image(frame, channels='BGR')


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

clean()
