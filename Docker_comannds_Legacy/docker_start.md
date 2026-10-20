# Docker START

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker start** inicia um ou mais containers que estavam parados.


---

### Sintaxe

docker **container start** [OPTIONS] CONTAINER [CONTAINER...]

---

### Apelido

docker **start** 

---

### Opções

As opções podem ser vistas por meio do comando `docker start --help` sendo elas:

- **-a**,**--attach** -> Anexa sinais STDOUT/STDERR e encaminha-os.
- **-i**, **--interactive** -> Anexa a entrada padrão (STDIN) do container.

---

### Exemplos

Ex:
```bash
docker start 8b54c76e81b7
ou 
docker start ocsinventory
```

--

Ex2. Inicia o container de nome meu-ubuntu e entra nele no modo interativo e deixa ele atachado:
```bash
docker start -ia meu-ubuntu
```

---
