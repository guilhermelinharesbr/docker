# Docker commands


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [build](#build)
- [cp](#cp)
- [help / -h / --help](#help---h----help)
- [info](#info)
- [login](#login)
- [ps](#ps)
- [pull](#pull)
- [push](#push)
- [version](#version)
- [-v](#-v)


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

#### build

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

#### cp

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

#### info

O **docker info** mostra informações de todo sistema(host), entre as informações, a versão do Docker, quantos containers, quantos containers rodando, quantos containers parados, quantas imagens, versão do S.O., etc.

Ex:
```bash
docker info
```

---

#### login

O **docker login** serve para pedir o seu login do docker. É usado em conjunto com o [docker build](#build) e [docker push](#push). 
Ele adiciona a credencial no arquivo /root/.docker/config.json, não sendo necessário colocar a senha em uma segunda execução do docker login.

---

#### ps

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

#### version

O **docker version** mostra a versão do docker, docker engine, cliente e servidor. 
É uma maneira mais completa de informações da versão do docker, a maneira resumida é o [docker -v](#-v).

Ex:
```bash
docker version
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
