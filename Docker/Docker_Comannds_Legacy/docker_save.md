# Docker SAVE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker save** gera um repositório compactado (tar) para o fluxo de saída padrão. Contém todas as camadas pai e todas as tags + versões, ou o repositório:tag especificado, para cada argumento fornecido.

Obs: Um uso comum é quando se quer pegar uma imagem de um servidor e mandar para outro sem mandar primeiro para algum registry, um exemplo completo pode ser visto em [Exportando_e_importando_imagem_sem_Registry.md](/Docker/Docker_Tutoriais/Imagens_docker/Exportando_e_importando_imagem_sem_Registry.md)

---

### Sintaxe

docker **image save** [OPTIONS] IMAGE [IMAGE...]

---

### Apelido

- docker **save** 

---

### Opções

As opções podem ser vistas por meio do comando `docker save --help` sendo elas:

- **-o**, **--output** -> Escreve em um arquivo, em vez de usar a saída padrão (STDOUT).

---

### Exemplos

Ex:
```bash
docker save -o nome_arquivo_que_sera_gerado.tar nome_imagem:versao
```

Ex2. Salva no arquivo minha-api-python.tar a imagem de nome minha-api-python:1.0.0:
```bash
docker save -o minha-api-python.tar minha-api-python:1.0.0
```

---
