ctf-ingest
===========

Tools for ingesting data from the Children's Tumor Foundation into various external databases.

# Currently works for
... exactly ...
## Currently Sorta Works For:
* Salesforce (with third party ingest)

# Planned
## Planned Ingests
* Salesforce Classic
* Classy
 * Via Salesforce
 * Via Classy API
* iContact

## Planned Databases
* PostgreSQL
* ElasticSearch
* CartoDB (standalone image)


# Instructions:
## Prerequisites:
* Git
* [Docker](https://www.docker.com/get-docker)

## Get Started
* Clone this repository: 'git clone https://github.com/childrenstumorfoundation/ctf-ingest.git'
* get to this folder
* Copy a Storage folder from local source
 * Should have `pg` & `pg_superset` folders
 * OR you be you, and import your own data.
* Start the program: `docker-compose up -d`

### Additional Commands
* To shutdown running instance: `docker-compose stop`
* To restart running instance: `docker-compose start`
* To pull new docker images: `docker-compose pull`
* To initialize fresh Superset: `docker-compose exec superset superset-init`
* To upgrade if a new Superset image is pulled: `docker-compose exec superset superset db upgrade`

# Public Services:
* [Jupyter Notebook - http:8888](http://127.0.0.1:8080)
* [Apache Superset - http:8088](http://127.0.0.1:8088)
* Postgresql datawarehouse - psql:5432


# Configuration Notes:
* Currently doesn't use volumes appropriately `¯\_(ツ)_/¯`. Writes to disk instead
* Superset consists of:
 * Superset Application (User)
 * Superset Worker (async queries)
 * Superset Postgres (Storing its own data)
 * Superset Redis (Cache)
