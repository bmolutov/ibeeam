FROM python:3.9.15-alpine

LABEL Author="ibeeam"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/auxiliary
COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]
