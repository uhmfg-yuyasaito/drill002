FROM python:3.11.0
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*
RUN mkdir /etc/uwsgi
RUN mkdir /code
WORKDIR /code
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Tokyo
CMD ["uwsgi","--ini","/etc/uwsgi/uwsgi.ini"]