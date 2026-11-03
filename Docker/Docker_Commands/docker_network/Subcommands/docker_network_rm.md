# Docker NETWORK RM

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network rm** remove uma ou mais redes por nome ou ID. Para remover uma rede, primeiro deve-se desconectar todos os containeres conectados a ela.

---

### Sintaxe

docker **network rm** NETWORK [NETWORK...]

---

### Opções

As opções podem ser vistas por meio do comando `docker network rm --help` sendo elas:

- **-f**, **--force** -> para Não apresentar erro se a rede não existir.

---

### Exemplos

Ex:
```bash
docker network rm nome_rede
```

---
