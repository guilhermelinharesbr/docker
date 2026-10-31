# Docker VOLUME PRUNE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker volume prune** remove todos os volumes locais não utilizados. Volumes locais não utilizados são aqueles que não são referenciados por nenhum container. Por padrão, apenas volumes anônimos são removidos.

---

### Sintaxe

docker **volume prune** [OPTIONS]

---

### Opções

As opções podem ser vistas por meio do comando `docker volume prune --help` sendo elas:

- **-a**, **--all** -> Remove todos os volumes não utilizados, não apenas os anônimos.

---

### Exemplos

Ex.:
```bash
docker volume prune
```

Ex. 2:
```bash
docker volume prune -a
```

---
