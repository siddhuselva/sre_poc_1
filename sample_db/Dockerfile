FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=srepoc123
ENV MYSQL_DATABASE=srepoc
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=srepoc123
EXPOSE 3306

# Add SQL script to create database
# COPY init.sql /docker-entrypoint-initdb.d/
COPY create_user_table.sql /docker-entrypoint-initdb.d/