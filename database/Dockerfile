FROM postgres:latest
ENV POSTGRES_PASSWORD=sreality_db
ENV POSTGRES_USER=sokovninn
ENV POSTGRES_DB=sreality_db
COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql
