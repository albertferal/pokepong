# Utilizar la imagen base de Python
FROM python:3

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el contenido de tu proyecto al contenedor
COPY . .

# Instalar Pygame y cualquier otra dependencia que puedas necesitar
RUN pip install pygame

# Comando para ejecutar tu juego
CMD ["python", "main.py"]
