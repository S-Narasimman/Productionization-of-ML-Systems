#Use official Python Image as Parent Image
FROM python:3.9-slim-buster

#Set working directory inside the container
WORKDIR /app

#Copy the contents in current directory into the container at /app
COPY . /app

#Copy the requirements.text separately and install dependencies first
COPY requirements.txt ./requirements.txt

#Copy machine learning models into the container
COPY ./cat_encoder.joblib /app/cat_encoder.joblib
COPY ./rf_model.joblib /app/rf_model.joblib

#Install all dependencies and packages
RUN pip install -r requirements.txt

#Expose the port 8000 for the Flask app to listen on
EXPOSE 8000

#Define environment variable for the Flask
ENV FLASK_APP=app.py 

#Run the Flask Application
CMD [ "flask","run", "--host=0.0.0.0", "--port=8000" ]