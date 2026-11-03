# Docker NETWORK LS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network ls** lista todas as redes que o daemon do Engine conhece. Isso inclui as redes que abrangem vários hosts em um cluster.

---

### Sintaxe

docker **network ls** [OPTIONS]

---

### Apelidos

- docker **network list**

---

### Opções

As opções podem ser vistas por meio do comando `docker network ls --help` sendo elas:

- **-q**, **--quiet** -> Exibe somente os IDs de rede.

---

### Exemplos

Ex:
```bash
docker network ls
```

Ex2:
```bash
docker network list
```

Ex3:
```bash
docker network ls -q
```

---
