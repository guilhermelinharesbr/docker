# Docker PAUSE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Exemplos](#exemplos)

---

### Descrição

O **docker pause** suspende todos os processos nos containers especificados. No Linux, isso utiliza o cgroup `freezer`. Tradicionalmente, ao suspender um processo, o sinal `SIGSTOP` é utilizado, o qual é observável pelo processo que está sendo suspenso. Com o cgroup `freezer`, o processo não tem conhecimento, e não consegue capturar, que está sendo suspenso e posteriormente retomado. No Windows, apenas containers Hyper-V podem ser pausados.

---

### Sintaxe

docker **container pause** CONTAINER [CONTAINER...]

---

### Apelido

docker **pause** 

---

### Exemplos

Ex:
```bash
docker pause nome_container
```

Obs: Para tirar o container do estado de **paused** usar o comando [docker unpause](./docker_unpause.md), com isso o container ficará com o estado _running_.

---
