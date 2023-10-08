# Utiliza una imagen base de Python
FROM python:3.10.13-slim-bookworm

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Crea un entorno virtual y actívalo
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Instala las dependencias desde requirements.txt
RUN pip install -r requirements.txt

#  Expone el puerto en el que se ejecuta Streamlit
EXPOSE 8501

# Comando para iniciar tu aplicación Streamlit
CMD ["streamlit", "run", "app.py"]
