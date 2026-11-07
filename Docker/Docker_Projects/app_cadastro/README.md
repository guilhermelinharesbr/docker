# Docker Project: App de cadastros

---

### Descrição

Projeto de uma página web para cadastro de usuários desenvolvido em NodeJS, MongoExpress com intuito educacional e nginx como loadbalance, tudo em containers docker.

Escopo:

![escopo](/Docker/images/Docker_Projects/app_cadastro/escopo.jpeg)

Na imagem acima são mostrados três containers chamados app-cadastro, onde eles no [compose.yaml](compose.yaml) são representados pelos services node1, node2 e node3.

Para executar este projeto, rodar na raiz do projeto, onde encontra-se o arquivo compose.yaml:

`docker compose up -d`

Conferindo o que foi criado:

```bash
docker image ls
docker container ls -a
docker network ls
docker volume ls
```

Para verificar se aplicação está funcionando basta acessar o navegador e digitar:

`http://ip_da_vm`

e depois:

`http://ip_da_vm:8081`


---
