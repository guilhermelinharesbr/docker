# Manipulando volumes no Docker

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como manipular volumes no docker.

É bem mais profissional usar docker volume do que bind mount. 

---

### Prática

Será mostrado como criar, lista, excluir um volume do docker.

```bash
# Criando um volume chamado vol-ubuntu:
docker volume create vol-ubuntu

# Listando os volumes:
docker volume ls

# Criando um container que usa o volume docker de nome vol-ubuntu e mapeando ele para o diretório dentro do container de nome volume-ubuntu, e tem como base uma imagem ubuntu:
docker run -dit --mount source=vol-ubuntu,target=/volume-ubuntu --name cont-com-volume-docker ubuntu
# Obs: Não é obrigatório no source colocar um volume já existente, pois caso ele não exista ele será criado neste momento.


docker exec -it cont-com-volume-docker bash

# Mostrando que o diretório de nome volume-ubuntu apontado via target foi criado:
ls -lh 

touch /volume-ubuntu/arquivo1.txt

exit

# Mostrando o conteúdo do diretório padrão dos volumes do docker:
ls -lh /var/lib/docker/volumes/

# Mostrando que dentro do volume recém criado tem um diretório chamado _data, e dentro dele ficarão os arquivos persistidos, foi possível ver o arquivo1.txt criado dentro do container:
ls -lh /var/lib/docker/volumes/vol-ubuntu/_data/

docker container rm -f cont-com-volume-docker

# Mostrando que mesmo com o container excluído o volume permaneceu:
docker volume ls

# Removendo o volume de nome vol-ubuntu:
docker volume rm vol-ubuntu

# Provando que o volume foi removido:
docker volume ls

# Criando um container e ovolume docker de nome vol-ubuntu2 e mapeando ele para o diretório dentro do container de nome volume-ubuntu2, e tem como base uma imagem ubuntu:
docker run -dit --mount source=vol-ubuntu2,target=/volume-ubuntu2 --name cont-com-volume-docker2 ubuntu
# Obs: Como o volume de nome vol-ubuntu2 ainda não existia, ele será criado agora.


docker container rm -f cont-com-volume-docker2

docker volume rm vol-ubuntu2

# Criando um container e um volume, no caso do volume é usando a opção -v do comando docker run, o mais usado no mercado é a opção --mount:
docker run -dit -v vol-ubuntu3:/volume-ubuntu3 --name cont-com-volume-docker3 ubuntu
```

---
