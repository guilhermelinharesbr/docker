# Criando um Docker Volume

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como criar um docker volume.


---

### Prática

Será mostrado como subir um container com volume e baseado em uma imagem ubuntu.


```bash
# Criando o container base ubuntu:
docker run -dit -v /app --name container-com-volume ubuntu
# Obs: O /app é o diretório do container onde serão persistidos os dados no docker host.

docker exec -it container-com-volume bash

# É possível ver que foi criado o diretório /app dentro do container:
ls -lh

# Inspecionando o container, olhando a área de "Mounts", e observando o "Source", que informa onde os dados estão sendo persistidos.
# No caso foi "/var/lib/docker/volumes/bd6c281f7b08fc1839e41da50a8e2b9018498dbc3c8193d3992d5e7b6dd8bc3a/_data" e o "Destination" é o "/app": 
docker inspect container-com-volume

# Vendo que dentro deste diretório ainda não tem nenhum arquivo:
ls -lh /var/lib/docker/volumes/bd6c281f7b08fc1839e41da50a8e2b9018498dbc3c8193d3992d5e7b6dd8bc3a/_data

cd /var/lib/docker/volumes/bd6c281f7b08fc1839e41da50a8e2b9018498dbc3c8193d3992d5e7b6dd8bc3a/_data

# Criando cinco arquivos:
touch arquivo{1..5}.txt

#Provando que os cinco arquivos foram criados:
ls -lh

docker exec -it container-com-volume bash

# Provando que os cinco arquivos criados existem dentro do container:
ls -lh /app

cd /app

# Criando três arquivos:
touch arquivo{6..8}.txt

# Mostrando que agora tem 8 arquivos dentro do container:
ls -lh /app

exit

cd /var/lib/docker/volumes/bd6c281f7b08fc1839e41da50a8e2b9018498dbc3c8193d3992d5e7b6dd8bc3a/_data

# Mostrando que agora tem 8 arquivos também fora do container:
ls -lh 
```

---
