
_default:
    @just --list

ssh:
    docker exec -it rag-api /bin/bash

up:
    docker compose up -d

down:
    docker compose down -t 1

logs:
    docker compose logs -f
open:
    open http://localhost:8012/docs

reload: down up