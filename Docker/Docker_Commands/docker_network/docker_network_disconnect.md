# Docker NETWORK DISCONNECT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network disconnect** desconecta um container de uma rede. O container precisa estar em execução para ser desconectado da rede.

---

### Sintaxe

docker **network disconnect** [OPTIONS] NETWORK CONTAINER

---

### Opções

As opções podem ser vistas por meio do comando `docker network disconnect --help` sendo elas:

- **-f**, **--force** -> Força o container a desconectar-se de uma rede.

---

### Exemplos

Ex:
```bash
# Desconectando da rede bridge um container:
docker network disconnect bridge nome_container
```

---
