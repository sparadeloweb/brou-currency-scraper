# Usa una imagen base de Python
FROM python:3.9-slim

# Instala Firefox y dependencias
RUN apt-get update && apt-get install -y firefox-esr

# Copia el contenido de tu proyecto al contenedor
WORKDIR /app
COPY . /app

# Asigna permisos ejecutables al geckodriver de Linux
RUN chmod +x /app/geckodriver

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "server.py"]
