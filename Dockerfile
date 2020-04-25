FROM python:3.7
EXPOSE 5000
COPY . /myapp
RUN pip install -r myapp/requirements.txt
WORKDIR /myapp


