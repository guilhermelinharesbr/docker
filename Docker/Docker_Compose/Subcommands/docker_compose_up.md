# Docker COMPOSE UP

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker compose up** constrói, (re)cria, inicia e conecta-se a containeres de um serviço.

A menos que já estejam em execução, este comando também inicia quaisquer serviços vinculados.

---

### Sintaxe

docker **compose up** [OPTIONS] [SERVICE...]

---

### Opções

As opções podem ser vistas por meio do comando `docker compose up --help` sendo elas:

- **-d**, **--detach** -> Detached mode: executa containeres em segundo plano.

---

### Exemplos

Ex:
```bash
docker compose up
```

Ex2:
```bash
docker compose up -d
```

---
