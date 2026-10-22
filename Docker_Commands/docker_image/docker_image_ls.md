# Docker IMAGE LS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker image LS** lista imagens.

Por padrão exibem todas as imagens de nível superior, seus repositórios, tags e tamanhos.

As imagens Docker possuem camadas intermediárias que aumentam a reutilização, diminuem o uso de disco e aceleram a construção do Docker, permitindo que cada etapa seja armazenada em cache. Essas camadas intermediárias não são exibidas por padrão.

Imagens sem tag (imagens órfãs) também são ocultadas por padrão. Use a flag `-a` (`--all`) para exibir as camadas intermediárias e as imagens órfãs.

Uma imagem será listada mais de uma vez se tiver vários nomes de repositório ou tags. Essa única imagem (identificável pelo seu ID de IMAGEM correspondente) usa o TAMANHO listado apenas uma vez.

---

### Sintaxe

docker **image ls** [OPTIONS] [REPOSITORY[:TAG]]

---

### Apelidos

- docker **image list** 
- docker **images** 

---

### Opções

As opções podem ser vistas por meio do comando `docker images --help` sendo elas:

- **-a**, **--all** -> Mostra todas as imagens (por padrão, oculta imagens intermediárias e flutuantes).

---

### Exemplos

Ex. lista as imagens:
```bash
docker image ls
docker image ls -a
```

---
