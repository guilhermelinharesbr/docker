# Docker BUILD

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker build** serve para criar (construir) uma imagem Docker a partir de um Dockerfile e de um conjunto de arquivos (conhecido como contexto de build).

Em termos práticos, ele funciona como a ferramenta que lê a sua "receita de bolo" (o Dockerfile) linha por linha, instalando dependências, copiando códigos e configurando o ambiente, e empacota tudo isso em uma imagem imutável. Essa imagem gerada pode posteriormente ser executada como um container em qualquer máquina.

Pré-BuildKit???

---

### Sintaxe

docker **image build** [OPTIONS] PATH | URL | -

---

### Apelidos

- docker **build**
- docker **builder build** 

---

### Opções

As opções podem ser vistas por meio do comando `docker build --help` sendo elas:

- **-f**, **--file** -> Nome do Dockerfile (padrão: PATH/Dockerfile).
- **-t**, **--tag** -> Nome e, opcionalmente, uma tag no formato nome:tag.

---

### Exemplos

Ex:
```bash
docker build -t meu-app-python:v1

```

--

---
