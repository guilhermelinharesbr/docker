# Docker EXEC

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker exec** executa um novo comando em um container em execução.

O comando especificado com `docker exec` só é executado enquanto o processo primário do container (PID 1) estiver em execução e não é reiniciado se o container for reiniciado.

O comando é executado no diretório de trabalho padrão do container.

O comando deve ser um executável. Comandos encadeados ou entre aspas não funcionam.

Este exemplo funciona: `docker exec -it my_container sh -c "echo a && echo b"`

Este exemplo não funciona: `docker exec -it my_container "echo a && echo b"`


---

### Sintaxe

docker **container exec** [OPTIONS] CONTAINER COMMAND [ARG...]

---

### Apelido

docker **exec** 

---

### Opções

As opções podem ser vistas por meio do comando `docker exec --help` sendo elas:

- **-d**, **--detach** -> Modo desatachado: executa o comando em segundo plano.
- **-i**, **--interactive** -> Mantém a entrada STDIN aberta mesmo que não esteja conectada.
- **-t**, **--tty** -> Aloca um pseudo terminal.

---

### Exemplos

Ex. Executa o container de nome meu-ubuntu e exibi em tela a mensagem do comando echo:
```bash
docker exec meu-ubuntu echo "Eu gosto de usar Docker"
ou
docker exec 87hk echo "Eu gosto de usar Docker" #87hk é o começo do ID do container
```
--


---
