# Docker SYSTEM DF

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker system df** exibe informações sobre a quantidade de espaço em disco utilizada pelo daemon do Docker.

---

### Sintaxe

docker **system df** [OPTIONS]

---

### Opções

As opções podem ser vistas por meio do comando `docker system df --help` sendo elas:

- **-v**, **--verbose** -> Exibe informações detalhadas sobre o uso do disco.

---

### Exemplos

Ex:
```bash
docker system df
```

Ex2. Exibe informações, como volumes, etc:
```bash
docker system df -v
```

---
