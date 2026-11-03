# Docker SYSTEM INFO

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker system info** mostra informações de todo sistema(host), entre as informações, a versão do Docker, quantos containers, quantos containers rodando, quantos containers parados, quantas imagens, versão do S.O., etc.

---

### Sintaxe

docker **system info** [OPTIONS]

---

### Apelido

- docker **info**

---

### Opções

As opções podem ser vistas por meio do comando `docker system info --help` sendo elas:

- **-f**, **--format** -> Formata a saída usando um modelo personalizado:
    - 'json': Imprime em formato JSON
    - 'TEMPLATE': Imprime a saída usando o modelo Go fornecido.

---

### Exemplos

Ex:
```bash
docker system info
```

---
