# se inicia con una imagen de python
FROM python:3

# se crea la carpeta que contendrá el código
RUN mkdir /reporter

# se copia el código del microservicio dentro de la carpeta creada
ADD . /reporter

# se mueve a la carpeta creada
WORKDIR /reporter

# se instalan las dependencias del microservicio
RUN pip install -r requirements.txt

# se expone el puerto que utilizará el microservicio
RUN pip uninstall mailmerge -y

# se expone el puerto que utilizará el microservicio
EXPOSE 8002

# se ejecuta el microservicio
CMD ["python", "main.py"] 

