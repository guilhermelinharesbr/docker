# Docker INSPECT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker inspect** fornece informações detalhadas sobre as estruturas controladas pelo Docker.

Por padrão, exibe os resultados em um array JSON.

---

### Sintaxe

**docker inspect** [OPTIONS] NAME|ID [NAME|ID...]

---

### Opções

As opções podem ser vistas por meio do comando `docker inspect --help` sendo elas:

- 

---

### Exemplos

Ex. Inspeciona a imagem de nome nginx:
```bash
docker inspect nginx:latest
ou
docker inspect nginx
```

--

Ex2. Para ver o diretório padrão do container:
```bash
docker inspect apache-joomla | grep Destination
```

---
