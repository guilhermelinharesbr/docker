# Docker CONTAINER UNPAUSE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container unpause** retoma todos os processos nos containers especificados. No Linux, isso é feito usando o cgroup `freezer`.

---

### Sintaxe

docker **container unpause** CONTAINER [CONTAINER...]

---

### Apelido

docker **unpause** 

---

### Exemplos

Ex:
```bash
docker container unpause nome_container
```

Obs: Para colocar novamente o container no estado de **paused** usar o comando [docker container pause](./docker_container_pause.md).

---
