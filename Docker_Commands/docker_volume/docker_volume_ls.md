# Docker VOLUME LS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker volume ls** lista os volumes.

---

### Sintaxe

docker **volume ls**

---

### Opções

As opções podem ser vistas por meio do comando `docker volume ls --help` sendo elas:

- **-q**, **--quiet** -> Mostra apenas os container IDs.


---

### Exemplos

Ex. lista os containers em execução:
```bash
docker container ls
```

--

Ex2. lista os containers estando em execução ou não:
```bash
docker container ls -a
```

Obs: Os comandos dos Ex. e Ex2. fazem o mesmo que o `docker ps` e `docker ps -a`.

---
