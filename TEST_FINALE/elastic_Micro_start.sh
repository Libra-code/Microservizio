#!/bin/sh 
cd Loggin
docker-compose up --build -d 
cd ..
docker-compose up --build
