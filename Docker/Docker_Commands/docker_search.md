# Docker SEARCH

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker search** pesquisa imagens no Docker Hub.

---

### Sintaxe

**docker search** [OPTIONS] TERM

---

### Opções

As opções podem ser vistas por meio do comando `docker search --help` sendo elas:

- **-f**, **--filter** -> filtra a saída com base nas condições fornecidas.

---

### Exemplos

Ex:
```bash
docker search termo
```

Ex2. Pesquisa por imagens no Docker Hub que contenham o nome ubuntu:
```bash
docker search ubuntu
```

Ex3. Pesquisa por imagens no Docker Hub que contenham o nome ubuntu e que tenham pelo menos oito "stars", ou seja pelo menos oito avaliações:
```bash
docker search -f=stars=8 ubuntu
ou
docker search --filter=stars=8 ubuntu
```

---
