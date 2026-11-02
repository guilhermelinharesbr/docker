# Docker NETWORK CONNECT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network connect** conecta um container a uma rede. Pode-se conectar um container pelo nome ou pelo ID. Uma vez conectado, o container pode se comunicar com outros containeres na mesma rede.

---

### Sintaxe

docker **network connect** [OPTIONS] NETWORK CONTAINER

---

### Opções

As opções podem ser vistas por meio do comando `docker network connect --help` sendo elas:

---

### Exemplos

Ex. Conectando uma rede em um container:
```bash
docker network connect nome_rede nome_container
```

Ex2. Conectando a rede de nome minha-rede no container de nome cont-1:
```bash
docker network connect minha-rede cont-1
```

---
