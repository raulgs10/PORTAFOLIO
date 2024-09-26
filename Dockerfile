FROM python:3.12    

# Copiar los archivos de la aplicación
WORKDIR /app
COPY . .

# Instalar las dependencias
RUN pip install flask

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "--app", "appy", "run", "--host=0.0.0.0"]
