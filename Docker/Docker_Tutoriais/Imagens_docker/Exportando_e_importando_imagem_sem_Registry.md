# Exportando e Importando imagem Docker sem passar por um Registry

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como exportar e depois importar uma imagem Docker sem para por um Registry, como por exemplo o Docker Hub.

---

### Prática

```bash
# Listando as imagens atuais na VM de IP 192.168.1.200:
docker image ls

# Salvando no arquivo minha-api-python.tar a imagem de nome minha-api-python:1.0.0:
docker save -o minha-api-python.tar minha-api-python:1.0.0

# Confirmando que o arquivo foi criado:
ls -lh

# Enviando o arquivo para outro servidor:
scp minha-api-python.tar root@192.168.1.118:/tmp

# Agora acessando via SSH a VM 192.168.1.118 é possível ver o arquivo:
cd /tmp
ls -lh

# Carregando a imagem minha-api-python:1.0.0 a partir do arquivo minha-api-python.tar:
docker load -i minha-api-python.tar

# Listando as imagens atuais na VM de IP 192.168.1.118:
docker image ls

# Subdindo um container com base na imagem recém importada:
docker run -dit --name app -p 8000:8000 minha-api-python:1.0.0

# Entrando no container
docker exec -it app bash
```

Agora para testar a aplicação na prática basta digitar no navegador:  
http:192.168.1.118:8000

Com isso, foi mostrado como exportar uma imagem sem mandar ela para algum Registry, depois mandar o arquivo para outra VM, para então importar ele, subir um container com base na imagem recém importada e por último testar a aplicação diretamente no navegador.

---
