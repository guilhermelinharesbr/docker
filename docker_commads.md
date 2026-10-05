# Docker commands


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [CTRL + d](#ctrl--d)
- [build](#build)
- [pull](#pull)


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
