# Utilizar la imagen base de Python
FROM python:3

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el contenido de tu proyecto al contenedor
COPY . .

# Instalar Pygame
RUN pip install pygame

# Instalar herramientas para testing, linting y code coverage
RUN pip install pytest pylint coverage

# Comando para ejecutar tu juego
CMD ["python", "main.py"]
