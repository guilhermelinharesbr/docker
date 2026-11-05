# Criando imagem Docker no padrão OCI

### Sumário
- [Descrição](#descrição)
- [Endereços na Web](#endereços-na-web)

---

### Descrição

Será mostrado como criar uma imagem Docker usando o padrão da OCI (Open Container Initiative).

---

### Prática

Criando o diretório do projeto:
```bash
mkdir -p /oci
cd /oci
```

Criando o Dockerfile:
```bash
vim Dockerfile
```
```dockerfile
# Conteúdo
FROM alpine:3.18
RUN apk add --no-cache curl
# Mantém o container rodando indefinidamente em segundo plano
CMD ["sleep", "infinity"]
```

Logando no Docker Hub:
```bash
docker login -u cglinhares
# Confirmando o login:
cat  /root/.docker/config.json
```

Construindo a imagem no padrão OCI e já mandando para o docker Hub:
```bash
docker buildx build \
--platform linux/amd64 \
-t docker.io/cglinhares/minha-imagem-oci:1.0.0 \
--push .
# Obs: Ao fazer isso já é possível ver a imagem no Docker Hub e foi criado a imagem localmente.
# Obs2: O BuildKit constrói a imagem respeitando estritamente o padrão OCI e faz o upload das camadas direto para a nuvem do Docker Hub.
```

Removendo a imagem local:
```bash
docker image ls
docker image rm cglinhares/minha-imagem-oci:1.0.0
docker image ls
```

Baixando a imagem do Docker Hub:
```bash
docker image pull cglinhares/minha-imagem-oci:1.0.0
docker image ls
```

Subindo o container:
```bash
docker container run -dit --name cont-padrao-oci --rm cglinhares/minha-imagem-oci:1.0.0
docker container ls -a
docker exec -it cont-padrao-oci sh
# Para ver os processos em execução:
top
```

Deslogando do Docker Hub:
```bash
docker logout
# Confirmando que logout foi realizado:
cat  /root/.docker/config.json
```

Com isso foi mostrado como criar um container no padrão OCI, mandá-lo para o Docker Hub, baixar essa imagem e depois criar um container com base nela. 

Existem outras forma de criar uma imagem de um container no padrão OCI, sendo elas:
- **Docker Buildx** (Com o BuildKit) -> Já foi mostrado neste artigo como é essa criação, mas outra forma seria:
    - `docker buildx build -t minha-imagem:1.0.0 --output type=oci,dest=minha-imagem.tar .`
- **Buildah** é uma ferramenta projetada especificamente para criar imagens de containers compatíveis com a OCI, sem sequer precisar do Docker Daemon rodando em segundo plano. É muito utilizada no ecossistema Red Hat / Fedora / Ubuntu.
![buildah.png](images/buildah.png)
    - [Buildah site](https://buildah.io/)
    - Exemplo: 
```bash
# Cria um container temporário a partir de uma base
container=$(buildah from alpine:3.18)
# Instala pacotes ou altera arquivos dentro dele
buildah run $container -- apk add --no-cache curl
# Salva o resultado diretamente no padrão de layout OCI em uma pasta
buildah commit --format oci $container oci-image-dir:1.0.0
```


- **Podman** é um motor de gerenciamento de containers compatível com a CLI do Docker, mas construído nativamente sobre a arquitetura OCI e libpod.
    - `podman build -t minha-imagem-podman:latest .`
    ![podman.png](images/podman.png)
    - [Podman site](https://podman.io/)
    - Exemplo: 
```bash
podman build -t minha-imagem-podman:1.0.0 .
```

---
