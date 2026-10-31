# Docker CONTAINER RUN

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker conatiner run** executa um comando em um novo container, baixando a imagem se necessário e iniciando o container.

Pode-se reiniciar um container parado, mantendo todas as alterações anteriores, usando `docker container start`.

Cria e inicia um novo container a partir de uma imagem especificada. Ele combina as operações `docker create` e `docker start`, oferecendo uma variedade de opções para personalizar o ambiente de execução do container.

---

### Sintaxe

docker **container run** [OPTIONS] IMAGE [COMMAND] [ARG...]

---

### Apelido

docker **run**

---

### Opções

As opções podem ser vistas por meio do comando `docker container run --help` sendo elas:

- **-d**, **--detach** -> Executa o container em segundo plano e imprime o ID do container.
- **-e**, **--env** -> Define variáveis ​​de ambiente.
- **-i**, **--interactive** -> Mantém a entrada STDIN aberta mesmo que não esteja conectada.
- **--mount** -> Anexa um filesystem mount ao container.
    - subparâmetro **type** -> Ex: docker run -dit **--mount type**=tmpfs,destination=/meu-app --name cont-tmpfs-mount ubuntu
- **--name** string -> Atribui um nome ao container.
- **-p**, **--publish** -> Publica porta de um container para o host. O Administrador define a porta.
- **-P**, **--publish-all** -> Publica todas as portas expostas em portas aleatórias. O Docker define a porta.
- **-t**, **--tty** -> Aloca um pseudo terminal.
- **-v**, **--volume** -> Monta um volume.


---

### Exemplos

Ex. Executa/baixa o container de nome hello-world e sai em seguida:
```bash
docker container run hello-world
```
--

Ex2. Executa/baixa uma imagem do mariadb da versão mais recente, colocando o nome some-mariadb, passa a variável de ambiente MYSQL_ROOT_PASSWORD já definindo uma senha para ela e executa o container em segundo plano: 
```bash
docker container run --name some-mariadb -e MYSQL_ROOT_PASSWORD=123456 -d mariadb:latest
```

--

Ex3. Executa/baixa o container que tem a imagem do ubuntu, roda o comando echo para exibir a mensagem em tela e para o container:
```bash
docker container run ubuntu echo "Eu gosto de usar Docker"
```

--

Ex4. Executa/baixa o container que tem a imagem do ubuntu, roda o comando ls para listar os arquivos do diretório / deste container:
```bash
docker container run ubuntu ls
```

--

Ex5. Executa/baixa o container que tem a imagem do ubuntu, já entrando no modo interativo e em um pseudo terminal, ao sair do container ele é finalizado:
```bash
docker container run -it ubuntu
ou
docker container run -i -t ubuntu
```

--

Ex6. Executa/baixa o container que tem a imagem do ubuntu, colocando o nome no container de meu-ubuntu, já entrando no modo interativo e em um pseudo terminal, ao sair do container ele é finalizado:
```bash
docker container run --name meu-ubuntu -it ubuntu
```

--

Ex7. Executa/baixa o container que tem a imagem do ubuntu, deixando ele desatachado e com interatividade ativada:
```bash
docker container run -di ubuntu
```

Obs: Para entrar nele basta rodar `docker exec -it [containerID/containerName] bash`. 

--

Ex8. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta aleatória:
```bash
docker container run -P -d dockersamples/static-site
```

--

Ex9. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta de número 5000 e dentro do container ela é a 80:
```bash
docker container run -p 5000:80 -d dockersamples/static-site
```

--

Ex10. Baixando a imagem de nome static-site do usuário dockersmaples, já deixando o container desatachado e com uma porta exposta de número 7000 e dentro do container ela é a 80, e passando a variável de ambiente AUTHOR:
```bash
docker container run -p 7000:80 -d -e AUTHOR="Guilherme" dockersamples/static-site
```

--

Ex11. Baixando a imagem de nome card-business do usuário cglinhares com a tag 1.0, já deixando o container uma porta exposta de número 8080 e dentro do container ela é a 8080:
```bash
docker container run -dit -p 8080:8080 cglinhares/card-business:1.0
```

--

Ex12. Baixando a imagem de nome card-business do usuário cglinhares com a tag 1.0, já deixando o container uma porta exposta de número 8080 e dentro do container ela é a 8080, acresentando variáveis de ambiente e um nome para o container:
```bash
docker container run -dit -p 8080:8080 -e NOME="Guilherme" -e IDADE="20" -e EMAIL="guilherme@dominio.com.br" --name container-cardbusiness cglinhares/card-business:1.0
```

---
