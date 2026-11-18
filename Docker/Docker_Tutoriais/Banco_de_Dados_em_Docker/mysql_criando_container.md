# Criando um container MySQL

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar um container **MySQL** pegando uma imagem oficial do Docker Hub.

[Link do MySQL no Docker Hub](https://hub.docker.com/_/mysql).

---

### Prática

Para usar o MySQL em containers Docker

```bash
docker image ls

docker image pull mysql:5.7

docker image ls

docker run -dit --name mysql-5.7 -e MYSQL_ROOT_PASSWORD=senha_forte mysql:5.7

docker container ls -a

docker exec -it mysql-5.7 bash

env

mysql -p$MYSQL_ROOT_PASSWORD

show databases;

create database nome_base_de_dados;

show databases;

exit
```

---
