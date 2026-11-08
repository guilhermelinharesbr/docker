# Docker STATS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker stats**  exibe um fluxo ao vivo das estatísticas de uso de recursos do(s) container(s). Por exemplo, container, uso de CPU, uso de memória, etc.

---

### Sintaxe

**docker conatiner stats**[OPTIONS] [CONTAINER...]

---

### Opções

As opções podem ser vistas por meio do comando `docker stats --help` sendo elas:

- **-a**,**--all** -> Mostra todos os containers(por padrão, mostra apenas os que estão em execução).

---

### Exemplos

Ex:
```bash
docker stats
```

Ex2:
```bash
docker stats -a
```

---
