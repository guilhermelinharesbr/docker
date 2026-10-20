# Docker CONTAINER

### Sumário
- [Descrição](#descrição)
- [Subcomandos](#)
    - [container ls](#container-ls)
    - [container prune](#)
    - [conatiner top](#container-top)

---

### Descrição

O **docker container** serve para gerenciar containers.

---

### Subcomandos

O comando docker container possuei diversos subcomandos, que serão mostrados mais abaixo neste artigo.

---

#### container ls 

Lista os containers.

Ex. lista os containers em execução:
```bash
docker container ls
```

Ex2. lista os containers estando em execução ou não:
```bash
docker container ls -a
```

Obs: Os comandos dos Ex. e Ex2. fazem o mesmo que o [docker ps](#ps) e [docker ps -a](#ps).

---

#### container prune

Exclui todos os containers parados. 

Obs: O _container prune_ já é menos perigoso que o _docker volume prune_, pois é só subir outro container que o problema estará resolvido.


Ex:
```bash
docker container prune
```

---

#### container top

Mostra os processos em execução no container.

Ex:
```bash
docker container top ocsinventory #ocsinventory é o containername
ou
docker container top 87hk #87hk é o containerid
```

---
