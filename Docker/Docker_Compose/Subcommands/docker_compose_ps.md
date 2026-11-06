# Docker COMPOSE PS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker compose ps** lista os containeres de um projeto Compose, com o status atual e as portas expostas.

---

### Sintaxe

docker **compose ps** [OPTIONS] [SERVICE...]

---

### Opções

As opções podem ser vistas por meio do comando `docker compose ps --help` sendo elas:

- **-q**, **--quiet** -> Exibe somente os IDs.

---

### Exemplos

Ex:
```bash
docker compose ps 
```

Ex2:
```bash
docker compose ps -q
```

---
