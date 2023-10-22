FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /social_network

WORKDIR /social_network

COPY requirements.txt /social_network/

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

RUN apk --no-cache add \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev \
    ttf-dejavu \
    vim

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apk del .tmp-build-deps

ADD . /social_network/ 
