FROM python:3.6.15

LABEL Author="ibeeam"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY init.sh /
RUN chmod +x /init.sh
CMD ["/init.sh"]
