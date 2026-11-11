# Docker DIFF

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker diff** lista os arquivos e diretórios alterados no sistema de arquivos de um container desde a sua criação. 
Três tipos diferentes de alterações são rastreadas:

Símbolo -> Descrição
- **A** -> Um arquivo ou diretório foi adicionado(added)
- **D** -> Um arquivo ou diretório foi excluído(deleted)
- **C** -> Um arquivo ou diretório foi alterado(changed)

---

### Sintaxe

docker **container diff** CONTAINER

---

### Apelido

docker **diff** 

---

### Opções

Apesar de não possuir opções, alguns detalhes podem ser vistas por meio do comando `docker diff --help`.


---

### Exemplos

Ex:
```bash
docker diff nome_container
```

---
