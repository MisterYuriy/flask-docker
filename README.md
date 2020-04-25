# flask-docker
Good day! Let's me introduce my flask application, which consists of:
1. ETL script.
2. Actually the flask application itself
3. Docker files for deployment
Let us dwell on each of them.
# ETL script.
It contains mainly tools for working with data, it is here that the profiles are downloaded from the external API, processed and saved to the Postgresql database; initialization of connection to the storage, data model; creation of functions for our api to work in the flask application.
# Flask application
It is a complex of modules and packages for performing the main task - creating RESTful API. The application itself is initialized in the __init__ module of the awtest package, after which the application starts when the module run.py is launched specifically for this purpose.
All routing, processing requests, receiving data and generating a response is in the file view.py
# Docker files.
Required for deployment and containerization. Dockerfile creates an environment for our services and installs the necessary components into it, copies our application and related files into it, creates a working directory, defines a port for connection. Dockercompose deploys our services: in a separate container, the database, and in another our application, allows them to communicate with each other. After initializing our web service, the ETL script starts.
