FROM python:3.10-alpine

LABEL Author="ibeeam"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/ibeeam
COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY init.sh /
RUN chmod +x /init.sh
CMD ["/init.sh"]
