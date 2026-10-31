# Docker IMAGE HISTORY

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Exemplos](#exemplos)

---

### Descrição

O **docker image history** mostra o histórico da imagem.

---

### Sintaxe

docker **image history** [OPTIONS] IMAGE

---

### Apelido

docker **history** 

---

### Exemplos

Ex:
```bash
docker image history nome_imagem
ou
docker image history id_imagem
```

--

Ex2. Mostra o histórico da imagem de nome static-site:
```bash
docker image history dockersamples/static-site:latest
```

--

Ex3. Mostra o histórico da imagem de nome static-site, filtrando pela variável AUTHOR:
```bash
docker image history dockersamples/static-site:latest | grep AUTHOR
```

---
