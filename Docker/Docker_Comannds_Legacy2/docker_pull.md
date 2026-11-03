# Docker PULL

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker pull** baixa uma imagem de um registro.

Pode ser usado para baixar uma imagem específica ou um conjunto de imagens (ou seja, um repositório).

A maioria das imagens será criada com base em uma imagem do registro do Docker Hub.

O Docker Hub contém muitas imagens pré-construídas que pode-se baixar e experimentar sem precisar definir e configurar as suas próprias.

---

### Sintaxe

docker **image pull** [OPTIONS] NAME[:TAG|@DIGEST]

---

### Apelido

docker **pull** 

---

### Opções

As opções podem ser vistas por meio do comando `docker pull --help` sendo elas:

- **-a**, **--all-tags** -> Baixa todas as imagens etiquetadas no repositório.

---

### Exemplos

Ex. Baixa a imagem de nome nginx do Docker Hub, como não foi passada nenhuma tag, é baixada a última versão:
```bash
docker pull nginx
```

--

Ex2:
```bash
docker pull hello-world 
```

--

Ex3:
```bash
docker pull cglinhares/my-go-app:1.0
```

--

Ex4:
```bash
docker pull grafana/grafana
```

---
