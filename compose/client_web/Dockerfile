FROM node:8

WORKDIR /app

COPY ./client_web/package.json /app
COPY ./client_web/package-lock.json /app

RUN npm install

ADD ./client_web/ /app
