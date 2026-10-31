# Docker CREATE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker create** cria um novo container a partir da imagem especificada, sem iniciá-lo.

Ao criar um container, o daemon do Docker cria uma _camada de container_ **writeable** sobre a imagem especificada e a prepara para executar o comando especificado. O ID do container é então impresso na saída padrão (STDOUT). Isso é semelhante ao comando `docker run -d`, exceto pelo fato de que o container nunca é iniciado. Pode-se usar o comando `docker start` para iniciar o container a qualquer momento.

Isso é útil quando deseja-se configurar um container antecipadamente para que ele esteja pronto para iniciar quando necessário. O status inicial do novo container é "**created**".

O comando `docker create` compartilha a maioria de suas opções com o comando `docker run` (que executa um `docker create` antes de iniciá-lo).

---

### Sintaxe

docker **container create** [OPTIONS] IMAGE [COMMAND] [ARG...]

---

### Apelido

docker **create** 

---

### Opções

As opções podem ser vistas por meio do comando `docker create --help` sendo elas:

- **-t**, **--tty** -> Aloca um pseudo terminal.

---

### Exemplos

Ex. Cria um container com base na imagem de nome ubuntu e deixa ele no estado created:
```bash
docker create -it ubuntu
```

--

Ex2. Cria um container com base na imagem de nome ubuntu, coloca nome no container de teste1 e deixa ele no estado created:
```bash
docker create -it --name teste1 ubuntu
```

---
