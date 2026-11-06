# Baixando imagens do Docker Hub

### Sumário
- [Descrição](#descrição)
- [Exemplos](#exemplos)


---

### Descrição

É possível baixar imagens do Docker Hub de algumas maneiras, onde algumas delas serão mostradas mais abaixo neste artigo.

---

### Exemplos

Ex. Baixando a imagem oficial do ubuntu na versão latest:
```bash
docker container run ubuntu
```

--

Ex2. Baixando a imagem de nome static-site do usuário dockersmaples:
```bash
docker container run -P -d dockersamples/static-site
```

Obs: Geralmente quando a imagem não tem selo de oficial no Docker Hub é preciso baixá-la informando: nome_usuario_da_imagem/nome_imagem.

Obs2: Para acessar o site estático basta digitar no navegador: 
- http://[ip-da-vm]:[porta-exposta-aleatória]/ -> http://192.168.1.200:32768/.


--

Ex3. Baixando a imagem de nome static-site do usuário dockersmaples já deixando o container desatachado e com uma porta exposta de número 5000 e dentro do container ela é a 80:
```bash
docker container run -p 5000:80 -d dockersamples/static-site
```

Obs: Para acessar o site estático basta digitar no navegador: 
- http://[ip-da-vm]:[porta-exposta-definida]/ -> http://192.168.1.200:5000/.

---
