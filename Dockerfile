FROM python:3.9.6-alpine

RUN apk update \
    && apk add --no-cache curl postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev build-base \
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev imagemagick

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Europe/Moscow

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt


COPY ./bot/pngegg.png /app
COPY ./bot /app

CMD ["python", "main.py"]
