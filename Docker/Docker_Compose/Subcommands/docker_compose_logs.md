# Docker COMPOSE LOGS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker compose logs** exibe a saída de log dos serviços.

---

### Sintaxe

docker **compose logs** [OPTIONS] [SERVICE...]

---

### Opções

As opções podem ser vistas por meio do comando `docker compose logs --help` sendo elas:

- **-f**, **--follow** -> Para acompanhar a saída de logs em tempo real.

---

### Exemplos

Ex:
```bash
docker compose logs
# Obs: Precisa estar dentro da raiz do projeto.
```

Ex2:
```bash
docker compose logs -f
# Obs: Precisa estar dentro da raiz do projeto.
```

Ex3:
```bash
docker compose -f /path_da_raiz_do_projeto/compose.yaml logs -f
# Obs: Não precisa estar dentro da raiz do projeto, pois está sendo passado o caminho completo do compose.yaml.
```


---
