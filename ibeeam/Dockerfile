FROM python:3.10.6

LABEL Author="ibeeam"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY init.sh /
RUN chmod +x /init.sh
CMD ["/init.sh"]
