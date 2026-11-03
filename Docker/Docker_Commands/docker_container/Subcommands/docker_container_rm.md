# Docker CONTAINER RM

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container rm** serve para remover um ou mais containers.

---

### Sintaxe

docker **container rm** [OPTIONS] CONTAINER [CONTAINER...]

---

### Apelidos

- docker **container remove** 
- docker **rm**

---

### Opções

As opções podem ser vistas por meio do comando `docker container rm --help` sendo elas:

- **-f**, **--force** -> Força a remoção de um container em execução (usa SIGKILL).

---

### Exemplos

Ex. remove um container se ele estiver parado:
```bash
docker container rm ocsinventory 
```

--

Ex2. com a opção **-f** força a remoção do container, mesmo que ele esteja em execução:
```bash
docker container rm -f ocsinventory
```

--

Ex3. remove um container se ele estiver parado, usando o id ou parte do id:
```bash
docker container rm 87hklerkl338924
ou
docker container rm 87hk
```

--

Ex4. remove todos os containers:
```bash
docker container rm -f $(docker container ls -aq)
```

---
