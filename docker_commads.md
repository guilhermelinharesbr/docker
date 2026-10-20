# Docker commands


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [container](#container)
- [help / -h / --help](#help---h----help)
- [image](#image)
- [info](#info)
- [login](#login)
- [logout](#logout)
- [pull](#pull)
- [push](#push)
- [stats](#stats)
- [version](#version)
- [volume](#volume)
- [-v](#-v)
- [Comandos LEGADOS](#comandos-legados)
- [build (legado)](#build-legado)
- [cp (legado)](#cp-legado)
- [images (legado)](#images-legado)
- [ps (legado)](#ps-legado)
- [rm (legado)](#rm-legado)
- [rmi (legado)](#rmi-legado)

---

#### Definição

O **Docker** é uma plataforma open-source desenvolvida para facilitar a criação, o envio e a execução de aplicações através do uso de containers.

---

#### Fonte de Pesquisa

- [Site oficial do Docker](https://www.docker.com/ "Site oficial do Docker")
- [Docker Hub](https://hub.docker.com/ "Docker Hub")

---

#### CTRL + d

Serve para **desatachar** do container sem matá-lo. Por trás desse atalho é enviado o comando exit.

---

#### container

Comando usado para gerenciar containers.

Ex. lista os containers em execução:
```bash
docker container ls
```

Ex2. lista os containers em execução:
```bash
docker container ls -a
```

Obs: Os comandos dos Ex. e Ex2. fazem o mesmo que o [docker ps](#ps) e [docker ps -a](#ps).

Ex3. Mostra os processos em execução no container:
```bash
docker container top ocsinventory #ocsinventory é o containername
ou
docker container top 87hk #87hk é o containerid
```

---

#### help / -h / --help

O **docker help** mostra as opções do comando docker.
Ele também pode ser usado dessas outras quatro maneiras abaixo:

Ex:
```bash
docker help
ou
docker -h
ou
docker --help
ou
docker
```

Obs: Se digitar apenas _docker_, é o mesmo que digitar _docker help_.

Ex2. mostrando opções do subcomando de nome _ps_:
```bash
docker help ps
ou
docker ps -h
ou
docker ps --help
```

---

#### image

A imagem determina o comportamento de um container.

Foi introduzido para organizar a CLI em subcomandos estruturados de acordo com os objetos do Docker (ex: docker container, docker volume, docker network, docker image).

Por si só, docker image é o comando pai do grupo de gerenciamento de imagens.

Se rodar apenas `docker image ls`, o resultado será exatamente igual a `docker images`.

Ex. lista as imagens:
```bash
docker image ls
ou
docker image list
```

Ex2. é exibido o menu de ajuda do comando docker image: 
```bash
docker image
ou 
docker image --help
```

Obs: O comando estruturado `docker image`(junto com a reorganização da CLI baseada em objetos como docker container, docker network e docker volume) foi introduzido oficialmente no Docker 1.13.0, lançado em janeiro de 2017.

---

#### info

O **docker info** mostra informações de todo sistema(host), entre as informações, a versão do Docker, quantos containers, quantos containers rodando, quantos containers parados, quantas imagens, versão do S.O., etc.

Ex:
```bash
docker info
```

---

#### login

O **docker login** serve para pedir o seu login do docker. É usado em conjunto com o [docker build](#build) e [docker push](#push). 
Ele adiciona a credencial no arquivo _/root/.docker/config.json_, não sendo necessário colocar a senha em uma segunda execução do docker login.

---

#### logout

O **docker logout** serve para encerrar a seção do Docker Hub.  
Ele exlcui as credenciais do arquivo _/root/.docker/config.json_, então na próxima vez que for preciso usar o [docker login](#login), será preciso passar usuário e senha. 

---

#### pull

O **docker pull** extrai/baixa uma imagem ou um repositório de um registro.

Ex:
```bash
docker pull hello-world 
```

Ex2:
```bash
docker pull cglinhares/my-go-app:1.0
```

---

#### push

O **docker push** serve para subir uma imagem para o Docker Hub.

Ex:
```bash
docker push cglinhares/my-go-app:1.0
```

---

#### stats

O **docker stats** exibe um fluxo ao vivo das estatísticas de uso de recursos do(s) container(s). Por exemplo, container, uso de CPU, uso de memória, etc.

Ex:
```bash
docker stats 8b54c76e81b7
ou 
docker stats ocsinventory
```

---

#### version

O **docker version** mostra a versão do docker, docker engine, cliente e servidor. 
É uma maneira mais completa de informações da versão do docker, a maneira resumida é o [docker -v](#-v).

Ex:
```bash
docker version
```

---

#### volume

O **docker volume** é usado para os armazenamentos de dados persistentes para containers, criados e gerenciados pelo Docker.

Ex. lista os volumes docker:
```bash
docker volume list
ou
docker volume ls
```

Ex. exclui os volumes docker não utilizados:
```bash
docker volume prune
```

---

#### -v

O **docker -v** mostra a versão docker de maneira bem resumida, litando-se a apenas uma linha.
A maneira de ver as informações mais completas da versão do docker é o [docker version](#version).

Ex:
```bash
docker -v
```

---

### Comandos LEGADOS

Com a introdução da CLI estruturada em subcomandos baseados em objetos (como docker container, docker image, docker network) a partir da versão 1.13, diversos comandos de primeiro nível passaram a ser considerados legados.

Apesar de serem chamados de legados, eles continuam funcionando perfeitamente (a Docker os mantém por razões de compatibilidade com scripts e hábitos antigos).

---

#### build (legado)

O **docker build** é usado para “buildar” e gerar uma imagem a partir do Dockerfile.

Ex:
```bash
docker build . -t python-ubuntu
```

Obs: No exemplo acima o **.** significa que o Dockerfile está nessa pasta. A opção **-t** é para colocar uma tag/nomear a imagem, -t vem de tag list. 
Além disso, se não houvesse a imagem do ubuntu já baixado no host ele baixaria agora.

Ex2:
```bash
docker build -t joomla3php8 .
```

---

#### cp (legado)

O **docker cp** é usado para copiar um arquivo que estava fora do contêiner para dentro do container, ou de dentro do container para fora.

Ex. de cópia de um arquivo de _fora_ para dentro:
```bash
docker cp bkp_mysql docker_mysql-master_1:/usr/local/bin/
```

Ex. de cópia de um arquivo de _dentro_ para fora:
```bash
docker cp Ubuntu-A:/destino/MeuZip.zip  Zipcopia.zip
```

---

#### images (legado)

É o comando original/clássico das primeiras versões do Docker. Serve para listar as imagens armazenadas localmente no seu host.

Ex. lista as imagens:
```bash
docker images
```

---

#### ps (legado)

O **docker ps** lista os containers.


Este subcomando possui diversas opções, que podem ser vistas consultado com o comando:

Ex:
```bash
docker ps --help
```

Ex2. listando os containers em execução:
```bash
docker ps
```

Ex3. listando todos os containers estando em execução ou não:
```bash
docker ps -a
ou
docker ps --all
```

Ex4. mostra apenas os IDs dos containers:
```bash
docker ps -q
ou
docker ps --quiet
```
Ex5. também é possível combinar opções. Mostrando apenas os IDs de todos os containers, estando em execução ou não:
```bash
docker ps -qa
```

Ex6. mostrando o tamanho dos containers, estando em execução ou não:
```bash
docker ps -as
ou
docker ps --all --size
```

---

#### rm (legado)

O **docker rm** remove um ou mais containers.

Ex. remove um container se ele estiver parado:
```bash
docker rm ocsinventory 
```

Ex2. com a opção **-f** força a remoção do container, mesmo que ele esteja em execução:
```bash
docker rm -f ocsinventory
```

Ex3. remove um container se ele estiver parado, usando o id ou parte do id:
```bash
docker rm 87hklerkl338924
ou
docker rm 87hk
```

---

#### rmi (legado)

O **docker rmi** remove uma ou mais imagens.

Ex:
```bash
docker rmi node
```

Ex2. o primeiro comando feito é o de dentro do parênteses ele lista as imagens docker e depois o resultado é jogado para o comando de fora do parenteses, que ele remove as imagens não utilizadas: 
```bash
docker rmi $(docker image list -q)  
```

---
