# Docker CONTAINER KILL

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container kill** mata/encerra um ou mais containers.

O processo principal dentro do container recebe o sinal SIGKILL (padrão) ou o sinal especificado com a opção `--signal`. Pode-se referenciar um container pelo seu ID, prefixo de ID ou nome.

---

### Sintaxe

docker **container kill** [OPTIONS] CONTAINER [CONTAINER...]

---

### Apelido

docker **kill** 

---

### Opções

As opções podem ser vistas por meio do comando `docker container kill --help` sendo elas:

- **-s**,**--signal** -> Define o sinal de chamada de sistema enviado ao container. Esse sinal pode ser um nome de sinal no formato SIG\<NOME>, por exemplo, SIGINT, ou um número sem sinal que corresponda a uma posição na tabela de chamadas de sistema do kernel, por exemplo, 2.

Embora o sinal padrão (SIGKILL) encerre o container, o sinal definido por meio de `--signal` pode não ser terminal, dependendo do processo principal do container. Por exemplo, o sinal SIGHUP, na maioria dos casos, não será terminal e o container continuará em execução após recebê-lo.

Obs: Os comandos `ENTRYPOINT` e `CMD` no formato shell são executados como processos filhos de `/bin/sh -c`, que não repassa sinais. Isso significa que o executável não é o PID 1 do container e não recebe sinais Unix.

---

### Exemplos

Ex. Para o container de maneira abrupta:
```bash
docker container kill nome_container
```

Obs: Se fosse usado o comando ``docker container stop nome_container` possilvelmente teria que aguardar 10 segundos para ele ser parado.

---
