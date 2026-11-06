# Docker COMPOSE DOWN

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker compose down** é usado para interromper e remover os serviços em execução.

Quando usa-se este comando ele:
- Remove os containers e as networks
- Não remove os volumes e as imagens
    - para remover volumes usar a opção -v

---

### Sintaxe

docker **compose down**

---

### Opções

As opções podem ser vistas por meio do comando `docker compose down --help` sendo elas:

- **-v**, **--volume** -> Remova os volumes nomeados declarados na seção "volumes" do arquivo Compose e os volumes anônimos anexados aos containeres.

---

### Exemplos

Ex:
```bash
docker compose down
```

Ex2:
```bash
docker compose down -v
```

---
