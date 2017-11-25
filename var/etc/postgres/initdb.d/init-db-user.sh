#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER $PGSQL_USER WITH PASSWORD '$PGSQL_PASS';
    CREATE DATABASE $PGSQL_DATABASE;
    GRANT ALL PRIVILEGES ON DATABASE $PGSQL_DATABASE TO $PGSQL_USER;
EOSQL