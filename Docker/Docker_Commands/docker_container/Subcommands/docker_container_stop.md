# Docker CONTAINER STOP

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container stop** faz com que o processo principal dentro do container receberá um sinal SIGTERM e, após um período de tolerância, um sinal SIGKILL. O primeiro sinal pode ser alterado com a instrução STOPSIGNAL no Dockerfile do container ou com a opção --stop-signal nos comandos docker run e docker create.

O tempo limite padrão pode ser especificado usando a opção `--stop-timeout` do comando `docker container create`. Se nenhum valor padrão for configurado para o container, o Daemon determinará o padrão, que é de _10 segundos para containers Linux_ e _30 segundos para containers Windows_.

---

### Sintaxe

docker **container stop** [OPTIONS] CONTAINER [CONTAINER...]

---

### Apelido

docker **stop** 

---

### Opções

As opções podem ser vistas por meio do comando `docker container stop --help` sendo elas:

- **-t**,**--timeout** int -> Para que aguardar tantos segundo antes de parar o container.


---

### Exemplos

Ex. :
```bash
docker container stop meu-ubuntu
ou
docker container stop 87hk #87hk é o começo do ID do container
```

--

Ex2 :
```bash
docker container stop -t 0 meu-ubuntu
ou
docker container stop -t0 meu-ubuntu
# Faz com que o container pare imediatamente, ou seja em 0 segundos 
```

Obs: Geralmente o docker demora uns 10 segundos para parar o container de maneira segura.

---
