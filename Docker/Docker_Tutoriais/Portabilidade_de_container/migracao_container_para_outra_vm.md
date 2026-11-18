# Migrando um container de uma VM para outra

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como migrar um container de um PostgreSQL de uma VM para outra, mantendo os dados intactos.

---

### Prática

Parte do servidor de origem:

```bash
docker container ls -a

# Para descobrir o volume do container:
docker inspect postgres-14
# Obs: Foi descoberto que o volume é do tipo Docker Volume Nomeado e 
# seu nome era "55726a785e53ddbd58a1904a2a9b311ec1bddcd9af44bbaf7498fabb00cc9a65"

# Para evitar corromper dados é preciso parar o container:
docker container stop postgres-14

docker container ls -a

# Como os volumes do Docker ficam ocultos em /var/lib/docker/volumes/, a maneira 
# mais limpa de exportar é rodar um container temporário que compacta o volume em um arquivo .tar
docker run --rm -v 55726a785e53ddbd58a1904a2a9b311ec1bddcd9af44bbaf7498fabb00cc9a65:/volume -v /tmp:/backup alpine tar czf /backup/postgres_backup.tar.gz -C /volume .
# Obs: Sobe um container Alpine leve, monta o seu volume do MariaDB
# e compacta tudo em um arquivo chamado mariadb_backup.tar.gz e salva no /tmp.

ls -lh /tmp

# Enviando o arquivo para o segundo servidor:
scp /tmp/postgres_backup.tar.gz usuario@ip_vm:/tmp
```

Parte do servidor de destino:

```bash
cd /tmp

# Conferindo se o arquivo está disponível:
ls -lh

docker volume ls

# Criando um volume vazio:
docker volume create postgres_data

docker volume ls

# Extraindo os dados do backup para dentro desse novo volume:
docker run --rm -v postgres_data:/volume -v /tmp:/backup alpine tar xzf /backup/postgres_backup.tar.gz -C /volume


# Conferindo se os dados foram migrados:
ls -lh /var/lib/docker/volumes/postgres_data/_data/

# Subindo o container do PostgreSQL no novo servidor apontando para o volume restaurado:
docker run -dit \
  --name postgres-14 \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=senha_forte \
  -v postgres_data:/var/lib/postgresql/data \
  --restart=always \
  postgres:14-alpine

docker container ls -a

docker exec -it postgres-14 bash

env

psql -U postgres

# Conferindo que o dados foram migrados:
\l+
```

Pronto, com isso o PostgreSQL subirá no novo ambiente com exatamente todas as bases, tabelas e dados que estavam no servidor original.

---
