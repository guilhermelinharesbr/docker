# Enviando imagens para o Docker Hub

### Sumário
- [Descrição](#descrição)
- [Exemplos](#exemplos)


---

### Descrição

É possível enviar imagens para o registry Docker Hub ou um registry local, neste artigo será mostrado como enviar para o Docker Hub.

---

### Exemplos

Comandos:

```bash
# Fazendo o build para trasnformar o projeto em uma imagem:
docker image build -t cglinhares/card-business:2.0 .

# Logando:
docker login -u cglinhares
# Obs: Foi digitado um Access token, mas poderia ser a senha do usuário também.

# Confirmando o login:
cat ~/.docker/config.json

# Enviando a imagem para o Docker Hub:
docker image push cglinhares/card-business:1.0



# Deslogando, sempre fazer isso por segurança:
docker logout
```

---
