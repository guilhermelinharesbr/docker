# Docker commands


### Sumário

- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [help / -h / --help](#help---h----help)
- [-v](#-v)

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

#### -v

O **docker -v** mostra a versão docker de maneira bem resumida, litando-se a apenas uma linha.
A maneira de ver as informações mais completas da versão do docker é o [docker version](#version).

Ex:
```bash
docker -v
```

---
