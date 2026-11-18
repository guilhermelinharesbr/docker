# Criando um container MariaDB

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar um container **MariaDB** pegando uma imagem oficial do Docker Hub.

[Link do MariaDB no Docker Hub](https://hub.docker.com/_/mariadb).

---

### Prática

Para usar o MariaDB em containers Docker

```bash
docker image ls

docker image pull mariadb:11.8.9-ubi9

docker image ls

docker run -dit --name mariadb-11 -p 3306:3306 -e MARIADB_ROOT_PASSWORD=senha_forte mariadb:11.8.9-ubi9

docker container ls -a

docker exec -it mariadb-11 bash

env

mariadb -u root -p$MARIADB_ROOT_PASSWORD

show databases;

create database nome_base_de_dados;

show databases;

exit
```

---
