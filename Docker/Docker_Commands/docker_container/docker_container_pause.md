# Docker CONTAINER PAUSE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container pause** suspende todos os processos nos containers especificados. No Linux, isso utiliza o cgroup `freezer`. Tradicionalmente, ao suspender um processo, o sinal `SIGSTOP` é utilizado, o qual é observável pelo processo que está sendo suspenso. Com o cgroup `freezer`, o processo não tem conhecimento, e não consegue capturar, que está sendo suspenso e posteriormente retomado. No Windows, apenas containers Hyper-V podem ser pausados.

Ao voltar do estado de _paused_ o container mantém todos os processos que já estavam em execução, diferente de quando volta do estado _stopped_, pois os processos são todos encerrados.

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
docker container pause nome_container
```

Obs: Para tirar o container do estado de **paused** usar o comando [docker container unpause](./docker_container_unpause.md), com isso o container ficará com o estado _running_.

---
