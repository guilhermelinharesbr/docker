# Docker commands


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [help / -h / --help](#help---h----help)
- [info](#info)
- [stats](#stats)
- [version](#version)
- [volume](#volume)
- [-v](#-v)
- [Comandos LEGADOS](#comandos-legados)
- [build (legado)](#build-legado)
- [cp (legado)](#cp-legado)

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
