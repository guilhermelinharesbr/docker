# Docker PS

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker ps** lista os containers.
O _ps_ vem de _process status_.

---

### Sintaxe

docker **container ls** [OPTIONS]

---

### Apelidos
	
docker **container list**
docker **container ps**
docker **ps**

---

### Opções

As opções podem ser vistas por meio do comando `docker ps --help` sendo elas:

- **-a**,**--all** -> Mostra todos os containers(por padrão, mostra apenas os que estão em execução).
- **-q**, **--quiet** -> Mostra apenas os container IDs.
- **-s**, **--size** -> Mostra o tamanho total dos arquivos.

---

### Exemplos

Ex:
```bash
docker ps --help
```

--

Ex2. listando os containers em execução:
```bash
docker ps
```

--

Ex3. listando todos os containers estando em execução ou não:
```bash
docker ps -a
ou
docker ps --all
```

--

Ex4. mostra apenas os IDs dos containers:
```bash
docker ps -q
ou
docker ps --quiet
```

--

Ex5. também é possível combinar opções. Mostrando apenas os IDs de todos os containers, estando em execução ou não:
```bash
docker ps -qa
```

--

Ex6. mostrando o tamanho dos containers, estando em execução ou não:
```bash
docker ps -as
ou
docker ps --all --size
```

---
