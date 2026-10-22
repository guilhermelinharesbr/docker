# Criando imagem com Docker Commit

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como criar uma imagem Docker com docker commit.

É importante conhecer a existência e seu funcionamento, mas ela não é a mais otimizada. A forma mais otimizada será mostrada no artigo [Criando imagem com DOCKER AAAAAAAAAJEITAR Dockerfile]().

Desvantagens de se criar uma imagem usando o docker container commit:
- Muito custoso;
- Não tão prático de se trabalhar;
- Para ficar organizado precisaria ficar fazendo _docker commit_ a cada pequena mudança para facilitar o entendimentos das camadas da imagem via _docker image history_.

---

### Prática

Será mostrado como criar uma imagem chamada **ubuntu-personalizado**, onde será usado como base uma imagem oficial do Ubuntu e nela serão acrescidos os pacotes **vim** e **curl** e **iputils-ping** para usar o utilitário **ping**.

```bash
# Criando o conatiner base:
docker run -dit --name ubuntu-modificado ubuntu

# Verificando que o tamanho atual dele é de 114MB:
docker container ls -as

# Entrando no container
docker exec -it ubuntu-modificado bash

# Atualizando os repositórios, instalando pacotes:
apt update
apt install curl vim iputils-ping -y
exit

# Verificando que o tamanho atual dele é de 148MB:
docker container ls -as
# Obs. Esse 34MB a mais foram adicionados ao container na camada Read/Write, já a camada Read Only se manteve intacta com seus 114MB.

# Listando as imagens atuais:
docker image ls

# Cria uma nova imagem chamada ubuntu-personalizado com base no container ubuntu-modificado já com os pacotes vim, curl e iputils-ping:
docker commit ubuntu-modificado ubuntu-personalizado
# Obs: Tornando esses pacotes que estavam na camada Read/Write em uma camada Read Only.

# Mostrando que a imagem ubuntu-personalizado foi criada:
docker image ls

# Criando um container com base na nova imagem:
docker run -dit --name container-ubuntu-personalizado ubuntu-personalizado

docker container ls -as

# Confirmando que os pacotes agora já vem por padrão no container:
docker exec -it container-ubuntu-personalizado bash
ping 8.8.8.8
vim test.txt
exit

# Verificando as camadas da imagem:
docker image history ubuntu-personalizado
# Obs: Foi observado que a última camada acabou de ser criada via o docker commit, as outras já haviam sido criadas pela equipe do Docker. 
```

---
