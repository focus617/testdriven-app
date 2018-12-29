# base image
FROM postgres:10.4-alpine

# adding a SQL file to the "docker-entrypoint-initdb.d" directory in the container,
# which will execute on init.
# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
