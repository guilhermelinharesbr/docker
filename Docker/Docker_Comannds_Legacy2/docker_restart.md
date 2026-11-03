# Docker RESTART

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker restart** reinicia um ou mais containers.

---

### Sintaxe

docker **container restart** [OPTIONS] CONTAINER [CONTAINER...]

---

### Apelido

docker **restart** 

---

### Opções

As opções podem ser vistas por meio do comando `docker container restart --help` sendo elas:

- **-s**,**--signal** -> Define o sinal de chamada de sistema enviado ao container.
- **-t**,**--timeout** int -> Para que aguardar tantos segundo antes de parar o container.

---

### Exemplos

Ex:
```bash
docker restart id_container
ou 
docker restart nome_container
```

---
