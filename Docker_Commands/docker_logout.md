# Docker LOGOUT

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker logout** serve encerrar sessão no registry. Se nenhum servidor for especificado, o padrão será definido pelo daemon.

Ele exlcui as credenciais do arquivo _/root/.docker/config.json_, então na próxima vez que for preciso usar o **docker login**, será preciso passar usuário e senha. 

---

### Sintaxe

**docker logout** [SERVER]

---

### Opções

As opções podem ser vistas por meio do comando `docker logout --help` sendo elas:

---

### Exemplos

Exs:
```bash
docker logout
```

---
