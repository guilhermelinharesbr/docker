# Docker LOGIN

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker login** serve para pedir o seu login do docker.
É usado em conjunto com o `docker build` e `docker push`, para enviar imagens um Registry, seja ele público ou privado, o registry mais famoso é o Docker Hub.

Ele adiciona a credencial no arquivo _/root/.docker/config.json_, não sendo necessário colocar a senha em uma segunda execução do `docker login`.

As credenciais de autenticação são armazenadas no repositório de credenciais configurado. Se estiver usando o Docker Desktop, as credenciais são salvas automaticamente no chaveiro nativo do seu sistema operacional. Se não estiver usando o Docker Desktop, pode configurar o repositório de credenciais no arquivo de configuração do Docker, localizado em `$HOME/.docker/config.json` no Linux ou `%USERPROFILE%/.docker/config.json` no Windows. Se não configurar um repositório de credenciais, o Docker armazena as credenciais no arquivo `config.json` em formato codificado em base64. Esse método é menos seguro do que configurar e usar um repositório de credenciais.

---

### Sintaxe

**docker login** [OPTIONS] [SERVER]

---

### Opções

As opções podem ser vistas por meio do comando `docker login --help` sendo elas:

- **-u**, **--username** -> Para informar o nome do usuário.

---

### Exemplos

Ex. Para logar via terminal no usuário cglinhares:
```bash
docker login -u cglinhares
# Obs: Foi digitado um Access token, mas poderia ser a senha do usuário também.
# Obs2: Os Acesses Token são criados no registry, neste caso foi no Docker Hub.
```

---
