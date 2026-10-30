# Docker CONTAINER START

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker container create** cria um novo container a partir da imagem especificada, sem iniciá-lo.

Ao criar um container, o daemon do Docker cria uma _camada de container_ **writeable** sobre a imagem especificada e a prepara para executar o comando especificado. O ID do container é então impresso na saída padrão (STDOUT). Isso é semelhante ao comando `docker run -d`, exceto pelo fato de que o container nunca é iniciado. Pode-se usar o comando `docker container start` para iniciar o container a qualquer momento.

Isso é útil quando deseja-se configurar um container antecipadamente para que ele esteja pronto para iniciar quando necessário. O status inicial do novo container é "created".

O comando `docker container create` compartilha a maioria de suas opções com o comando `docker container run` (que executa um `docker container create` antes de iniciá-lo).

---

### Sintaxe

docker **container create** [OPTIONS] IMAGE [COMMAND] [ARG...]

---

### Apelido

docker **create** 

---

### Opções

As opções podem ser vistas por meio do comando `docker container create --help` sendo elas:

- **--name** string -> Atribui um nome ao container.

---

### Exemplos

Ex. Cria um container com base na imagem de nome ubuntu e deixa ele no estado created:
```bash
docker container create -it ubuntu
```

---
