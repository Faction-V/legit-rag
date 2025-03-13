
_default:
    @just --list

ssh:
    docker exec -it rag-api /bin/bash

up:
    docker compose up -d

down:
    docker compose down -t 1