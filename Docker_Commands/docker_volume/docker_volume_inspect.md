# Docker VOLUME INSPECT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker volume inspect** exibe informações detalhadas sobre um ou mais volumes.

---

### Sintaxe

docker **volume inspect** [OPTIONS] VOLUME [VOLUME...]

---

### Opções

As opções podem ser vistas por meio do comando `docker volume inspect --help` sendo elas:

- **-f**, **--format** -> Formata a saída usando um modelo personalizado.

---

### Exemplos

Ex.:
```bash
docker volume inspect nome_volume
```

Ex2. Inspeciona o volume de nome vol-ubuntu:
```bash
docker volume inspect vol-ubuntu
```

---
