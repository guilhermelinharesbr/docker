# Docker NETWORK INSPECT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network inspect** retorna informações sobre uma ou mais redes. Por padrão, este comando renderiza todos os resultados em um objeto JSON.

Por padrão, o docker disponibiliza três redes:
- bridge
- host
- none

---

### Sintaxe

docker **network inspect** [OPTIONS] NETWORK [NETWORK...]

---

### Opções

As opções podem ser vistas por meio do comando `docker network inspect --help` sendo elas:

- **-v**, **--verbose** -> Para uma saída no modo mais verboso.

---

### Exemplos

Ex. Exibe os containers que estão na rede _bridge_, além de outras informações:
```bash
docker network inspect bridge
ou
# Para uma saída um pouco mais verbosa:
docker network inspect bridge -v
```

Ex2. Exibe os containers que estão na rede _host_, além de outras informações:
```bash
docker network inspect host
```

Ex3. Exibe os containers que estão na rede _none_, além de outras informações:
```bash
docker network inspect none
```

---
