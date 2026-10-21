# Docker CONTAINER

### Sumário
- [Descrição](#descrição)
- [Subcomandos](#)
    - [container create](#container-create)
    - [container ls](#container-ls)
    - [container prune](#container-prune)
    - [container rm](./docker_container/docker_container_rm.md)
    - [container run](#container-run)
    - [container start](#container-start)
    - [container top](./docker_container/docker_container_top.md)

---

### Descrição

O **docker container** serve para gerenciar containers.

---

### Subcomandos

O comando docker container possuei diversos subcomandos, que serão mostrados mais abaixo neste artigo.

---

#### container create

O **docker container create** cria um novo container a partir da imagem especificada, sem iniciá-lo.

Ao criar um container, o daemon do Docker cria uma _camada de container_ **writeable** sobre a imagem especificada e a prepara para executar o comando especificado. O ID do container é então impresso na saída padrão (STDOUT). Isso é semelhante ao comando `docker run -d`, exceto pelo fato de que o container nunca é iniciado. Pode-se usar o comando `docker container start` para iniciar o container a qualquer momento.

Isso é útil quando deseja-se configurar um container antecipadamente para que ele esteja pronto para iniciar quando necessário. O status inicial do novo container é "**created**".

O comando `docker container create` compartilha a maioria de suas opções com o comando `docker container run` (que executa um `docker container create` antes de iniciá-lo).

--

Ex. Cria um container com base na imagem de nome ubuntu e deixa ele no estado created:
```bash
docker container create -it ubuntu
```

---

#### container ls 

O **docker container ls** lista os containers.

--

Ex. lista os containers em execução:
```bash
docker container ls
```

--

Ex2. lista os containers estando em execução ou não:
```bash
docker container ls -a
```

Obs: Os comandos dos Ex. e Ex2. fazem o mesmo que o `docker ps` e `docker ps -a`.

---

#### container run

O **docker container run** executa um comando em um novo container, baixando a imagem se necessário e iniciando o container.

Pode-se reiniciar um container parado, mantendo todas as alterações anteriores, usando `docker container start`.

--

Opções:

- **-d**, **--detach** -> Executa o container em segundo plano e imprime o ID do container.
- **-i**, **--interactive** -> Mantém a entrada STDIN aberta mesmo que não esteja conectada.
- **--name** string -> Atribui um nome ao container.
- **-t**, **--tty** -> Aloca um pseudo terminal.

--

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

Obs: Para entrar nele basta rodar `docker exec -it [conatinerID/containerName] bash`. 

---

#### container start

O **docker container start** inicia um ou mais containers que estavam parados.

--

Ex:
```bash
docker container start 8b54c76e81b7
ou 
docker container start ocsinventory
```

---

#### container start

O **docker container start** inicia um ou mais containers que estavam parados.

--

Ex:
```bash
docker container start 8b54c76e81b7
ou 
docker container start ocsinventory
```

---
