# Criando um container MongoDB

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar um container **MongoDB** pegando uma imagem oficial do Docker Hub.

[Link do MongoDB no Docker Hub](https://hub.docker.com/_/mongo).

---

### Prática

Para usar o MongoDB em containers Docker

```bash
docker image ls

docker image pull mongo:4.4

docker image ls

docker run -dit --name mongo-4.4 -p 27017:27017 mongo:4.4

docker container ls -a

docker exec -it mongo-4.4 bash

env

# Para abrir o prompt do MondoDB:
mongo

# Para exibir as bases disponíveis:
show dbs

# Mundando para contexto do banco de dados específico:
use predio
# Obs: No MongoDB, não usa-se o comando tradicional CREATE DATABASE como no SQL. Em vez disso,
# o MongoDB cria o banco de dados automaticamente no momento em que você insere o primeiro dado nele.
# Para "criar" e começar a usar o banco de dados "predio", deve-se alternar para ele usando o comando 
# "use" e, em seguida, inserir algum documento ou criar uma coleção. 

# Cria a coleção automaticamente: Se a coleção sensores ainda não existia dentro
# do banco de dados predio, o MongoDB a cria no exato momento em que você executa o comando:
db.sensores.insertOne({ equipamento: "sensor-01", status: "ativo" })
# Obs: Insere o documento: Logo em seguida, ele grava o 
# objeto JSON { equipamento: "sensor-01", status: "ativo" } dentro dessa coleção recém-criada.

dbs

# Lista as coleções existentes:
show collections

exit
```

---
