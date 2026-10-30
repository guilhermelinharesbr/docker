# Docker VOLUME RM

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker volume rm** remova um ou mais volumes. Não é possível remover um volume que esteja sendo usado por um container.

---

### Sintaxe

docker **volume rm** [OPTIONS] VOLUME [VOLUME...]

---

### Opções

As opções podem ser vistas por meio do comando `docker volume ls --help` sendo elas:

- **-f**, **--force** -> Força a remoção de um ou mais volumes.

---

### Exemplos

Ex. Remove o volume de nome vol-ubuntu:
```bash
docker volume rm vol-ubuntu
```

---
