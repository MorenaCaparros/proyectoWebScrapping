FROM python:3.9
WORKDIR /app
ADD . /app
# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
