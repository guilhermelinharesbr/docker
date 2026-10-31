# Docker PUSH

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker push** é usado para compartilhar imagens no registry do Docker Hub ou em um registry auto-hospedado.

Obs: Para Interromper o processo `docker push`, por exemplo, pressionando `CTRL + C` enquanto ele estiver em execução em um terminal, encerra a operação de envio.

Obs2: As credenciais do registry são gerenciadas pelo comando `docker login`.

---

### Sintaxe

docker **image push** [OPTIONS] NAME[:TAG]

---

### Apelido

docker **push** 

---

### Opções

As opções podem ser vistas por meio do comando `docker push --help` sendo elas:

- **-a**, **--all-tags** -> Envia todas as tags de uma imagem para o repositório.

---

### Exemplos

Ex:
```bash
docker push cglinhares/my-go-app:1.0
```

---
