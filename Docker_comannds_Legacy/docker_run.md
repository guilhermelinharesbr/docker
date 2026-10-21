# Docker RUN

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker run** executa um comando em um novo container, baixando a imagem se necessário e iniciando o container.

Pode-se reiniciar um container parado, mantendo todas as alterações anteriores, usando `docker start`.

---

### Sintaxe

docker **container run** [OPTIONS] IMAGE [COMMAND] [ARG...]

---

### Apelido

docker **run**

---

### Opções

As opções podem ser vistas por meio do comando `docker run --help` sendo elas:

- **-d**, **--detach** -> Executa o container em segundo plano e imprime o ID do container.
- **-i**, **--interactive** -> Mantém a entrada STDIN aberta mesmo que não esteja conectada.
- **--name** string -> Atribui um nome ao container.
- **-t**, **--tty** -> Aloca um pseudo terminal.


---

### Exemplos

Ex. Executa/baixa o container de nome hello-world e sai em seguida:
```bash
docker run hello-world
```
--

Ex2. Executa/baixa uma imagem do mariadb da versão mais recente, colocando o nome some-mariadb, passa a variável de ambiente MYSQL_ROOT_PASSWORD já definindo uma senha para ela e executa o container em segundo plano: 
```bash
docker run --name some-mariadb -e MYSQL_ROOT_PASSWORD=123456 -d mariadb:latest
```

--

Ex3. Executa/baixa o container que tem a imagem do ubuntu, roda o comando echo para exibir a mensagem em tela e para o container:
```bash
docker run ubuntu echo "Eu gosto de usar Docker"
```

--

Ex4. Executa/baixa o container que tem a imagem do ubuntu, roda o comando ls para listar os arquivos do diretório / deste container:
```bash
docker run ubuntu ls
```

--

Ex5. Executa/baixa o container que tem a imagem do ubuntu, já entrando no modo interativo e em um pseudo terminal, ao sair do container ele é finalizado:
```bash
docker run -it ubuntu
ou
docker run -i -t ubuntu
```

--

Ex6. Executa/baixa o container que tem a imagem do ubuntu, colocando o nome no container de meu-ubuntu, já entrando no modo interativo e em um pseudo terminal, ao sair do container ele é finalizado:
```bash
docker run --name meu-ubuntu -it ubuntu
```

--

Ex7. Executa/baixa o container que tem a imagem do ubuntu, deixando ele desatachado e com interatividade ativada:
```bash
docker run -di ubuntu
```

Obs: Para entrar nele basta rodar `docker exec -it [containerID/containerName] bash`. 

--

Ex8. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta aleatória:
```bash
docker run -P -d dockersamples/static-site
```

--

Ex9. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta de número 5000 e dentro do container ela é a 80:
```bash
docker run -p 5000:80 -d dockersamples/static-site
```

--

Ex10. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta de número 7000 e dentro do container ela é a 80, e passando a variável de ambiente AUTHOR:
```bash
docker run -p 7000:80 -d -e AUTHOR="Guilherme" dockersamples/static-site
```

---
