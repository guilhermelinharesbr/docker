# Criando um container PostgreSQL

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar um container **PostgreSQL** pegando uma imagem oficial do Docker Hub.

[Link do PostgreSQL no Docker Hub](https://hub.docker.com/_/postgres).

---

### Prática

Para usar o PostgreSQL em containers Docker

```bash
docker image ls

docker image pull postgres:14-alpine

docker image ls

docker run -dit --name postgres-14 -e POSTGRES_PASSWORD=senha_forte postgres:14-alpine

docker container ls -a

docker exec -it postgres-14 bash

env

psql -U postgres

create database nome_base_de_dados

\l+

\q

exit
```

---
