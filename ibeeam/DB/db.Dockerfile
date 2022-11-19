FROM postgres:12.11

COPY init.sql /docker-entrypoint-initdb.d/
