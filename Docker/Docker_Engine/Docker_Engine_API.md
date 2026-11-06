# Docker ENGINE API

### Sumário
- [Descrição](#descrição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)

---

### Descrição

A **Docker Engine API** é uma API RESTful exposta pelo Daemon do Docker (dockerd). Como ela segue o padrão HTTP, qualquer linguagem de programação ou ferramenta externa (como o curl) pode conversar diretamente com o motor do Docker para criar containers, gerenciar imagens e monitorar recursos sem precisar passar pela CLI tradicional.

O Docker fornece uma API para interagir com o daemon do Docker (Docker Engine API), bem como SDKs para Go e _Python_. Os SDKs permitem criar e dimensionar aplicativos e soluções Docker de forma eficiente. Se Go ou Python não forem adequados para você, é possível usar a API do Docker Engine diretamente.

---

### Fonte de Pesquisa

- [Docker Engine API](https://docs.docker.com/reference/api/engine/)

---

### Prática

Testando a Docker Engine API com **HTTP** com o comando _curl_:

```bash
# Baixando uma imagem do Docker Hub, para depois o equivalente via API
docker pull cglinhares/minha-imagem-oci:1.0.0
docker image ls
docker image rm cglinhares/minha-imagem-oci:1.0.0
docker image ls

# Para listar as imagens:
curl --unix-socket /var/run/docker.sock http://localhost/v1.52/images/json
# Obs: Se listar apenas "[]" é que não tem nenhuma imagem baixada.

# Baixando a imagem, equivalente ao comando:
# "docker pull cglinhares/minha-imagem-oci:1.0.0"
curl --unix-socket /var/run/docker.sock -X POST "http://localhost/v1.52/images/create?fromImage=cglinhares/minha-imagem-oci&tag=1.0.0"

# Mostrando que a imagem foi baixada:
docker image ls

# Criando o container:
curl --unix-socket /var/run/docker.sock -H "Content-Type: application/json" \
  -d '{"Image": "cglinhares/minha-imagem-oci:1.0.0"}' \
  -X POST http://localhost/v1.52/containers/create

# Mostrando que o container foi criado, mas não iniciado.
docker container ls -a

# Iniciando o container:
curl --unix-socket /var/run/docker.sock -X POST http://localhost/v1.52/containers/486ba23e8b38/start
#Obs: O número 486ba23e8b38 é o ID do container que foi criado, é preciso substituir pelo ID que for gerado, todas as vezes.

# Mostrando que o container foi iniciado.
docker container ls -a
```

Como foi visto acima o Docker Engine API funciona perfeitamente com o HTTP, da mesma forma seria com a linguagens Go, Python, etc.

---
