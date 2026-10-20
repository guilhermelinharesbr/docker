# Docker RM

### Sumário
- [Descrição](#descrição)
- [Sintaxes](#sintaxes)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker rm** serve para remover objetos Docker, podendo ser imagens, containers, redes, etc.

---

### Sintaxes

- docker **image rm** [OPTIONS] IMAGE [IMAGE...]
- docker **container rm** [OPTIONS] CONTAINER [CONTAINER...]
- docker **network rm** NETWORK [NETWORK...]
- ETC

---

### Apelidos

- docker **image rm** 
- docker **container rm**
- docker **network rm**
- ETC


---

### Opções

As opções podem ser vistas por meio do comando `docker rm --help` sendo elas:

- **-f**, **--force** -> Força a remoção de um container em execução (usa SIGKILL).

---

### Exemplos

Ex. remove um container se ele estiver parado:
```bash
docker rm ocsinventory 
```

Ex2. com a opção **-f** força a remoção do container, mesmo que ele esteja em execução:
```bash
docker rm -f ocsinventory
```

Ex3. remove um container se ele estiver parado, usando o id ou parte do id:
```bash
docker rm 87hklerkl338924
ou
docker rm 87hk
```

---
