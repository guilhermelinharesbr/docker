# Docker commands


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [build](#build)
- [info](#info)
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

O **docker build** é usado ara “buildar” e gerar uma imagem a partir do Dockerfile.

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

#### info

O **docker info** mostra informações de todo sistema(host), entre as informações, a versão do Docker, quantos containers, quantos containers rodando, quantos containers parados, quantas imagens, versão do S.O., etc.

Ex:
```bash
docker info
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
