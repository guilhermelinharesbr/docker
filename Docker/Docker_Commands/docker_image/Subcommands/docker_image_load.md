# Docker IMAGE LOAD

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker image load** carrega uma imagem ou repositório de um arquivo tar (mesmo que compactado com gzip, bzip2, xz ou zstd) a partir de um arquivo ou da entrada padrão (STDIN). Restaura tanto as imagens quanto as tags.

Obs: Um uso comum é quando se quer pegar uma imagem de um servidor e mandar para outro sem mandar primeiro para algum registry, um exemplo completo pode ser visto em [Exportando_e_importando_imagem_sem_Registry.md](/Docker/Docker_Tutoriais/Imagens_docker/Exportando_e_importando_imagem_sem_Registry.md)

---

### Sintaxe

docker **image load** [OPTIONS]

---

### Apelido

- docker **load**

---

### Opções

As opções podem ser vistas por meio do comando `docker image load --help` sendo elas:

- **-i**, **--import** -> Ler de um arquivo tar, em vez da entrada padrão (STDIN).

---

### Exemplos

Ex:
```bash
docker image load -i nome_arquivo
```

Ex2. Carrega o arquivo minha-api-python.tar para gerar uma imagem que poderá ser usada para criar um container:
```bash
docker image load -i minha-api-python.tar
```

---
