# Docker CP

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelido](#apelido)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker cp** copia o conteúdo de `SRC_PATH` para `DEST_PATH`. Pode-se copiar do sistema de arquivos do container para a máquina local ou vice-versa, do sistema de arquivos local para o container. Se `-` for especificado para `SRC_PATH` ou `DEST_PATH`, também pode-se transmitir um arquivo tar da entrada padrão (STDIN) ou da saída padrão (STDOUT). O container `CONTAINER` pode estar em execução ou parado. O `SRC_PATH` ou `DEST_PATH` podem ser um arquivo ou diretório.

---

### Sintaxe

docker **container cp** [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|- docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

---

### Apelido

docker **cp** 

---

### Opções

As opções podem ser vistas por meio do comando `docker cp --help` sendo elas:


---

### Exemplos

Ex. Para copiar um arquivo que estava fora do container para dentro do container:
```bash
docker cp nome_arquivo nome_container:/diretorio-de-destino
```

Ex2. Copiando o arquivo de nome bkp_mysql do host local para dentro do container chamado docker_mysql-master_1 no diretório /usr/local/bin:
```bash
docker cp bkp_mysql docker_mysql-master_1:/usr/local/bin/
```

--

Ex3. Para copiar um arquivo de dentro do Container para a máquina local:
```bash
docker cp nome_container:/diretorio-de-origem/nome-arquivo nome_arquivo_que_será_no_host_local
```

Ex4. Copiando o arquivo de nome Meuzip.zip de dentro do container chamado cont-alpine para o host local, e já nomeando o arquivo como Meuzip.zip.bkp:
```bash
docker cp cont-alpine:/home/Meuzip.zip /tmp/Meuzip.zip.bkp
# Obs: Este comando é executado fora do container. 
```

---
