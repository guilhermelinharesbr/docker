# Docker VERSION

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker version** exibe o número da versão atual de todos os componentes do Docker que possuem versões independentes. Pode-se usar a opção `--format` para personalizar a saída.

Mostra a versão do docker, docker engine, cliente e servidor.
É uma maneira mais completa de informações da versão do docker, a maneira resumida é o `docker -v` ou `docker --version`.

O comando `docker version` exibe os números de versão dos componentes do Docker, enquanto a opção `-v` ou `--version` (`docker --version`) exibe o número da versão da CLI do Docker que você está usando.

---

### Sintaxe

**docker version** [OPTIONS]

---

### Opções

As opções podem ser vistas por meio do comando `docker version --help` sendo elas:

- **-f**, **--format** -> formatar a saída usando um modelo personalizado:
    - 'json': Imprime em formato JSON

---

### Exemplos

Ex:
```bash
docker version
```

Ex2:
```bash
docker version -f json
ou
docker version --format json
```

---
