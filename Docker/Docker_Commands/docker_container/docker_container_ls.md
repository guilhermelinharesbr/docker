# Docker CONTAINER LS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container ls** lista os containers.

---

### Sintaxe

docker **container ls** [OPTIONS]

---

### Apelidos

- docker **container list**
- docker **container ps**
- docker **ps**

---

### Opções

As opções podem ser vistas por meio do comando `docker container ls --help` sendo elas:

- **-a**,**--all** -> Mostra todos os containers(por padrão, mostra apenas os que estão em execução).
- **-q**, **--quiet** -> Mostra apenas os container IDs.
- **-s**, **--size** -> Mostra o tamanho total dos arquivos.

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
