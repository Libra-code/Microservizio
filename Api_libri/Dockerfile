# init a base image 
FROM python:3.8-alpine
# define the present working directory
WORKDIR /app
# copy the contents into the working dir
COPY . .
# run pip to install the dependencies of the flask app
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
# define flask variable
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
# define the command to start the container
CMD ["flask", "run"]