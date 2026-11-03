# Docker NETWORK

### Sumário
- [Descrição](#descrição)
- [Subcomandos](#subcomandos)
    - [network connect](Subcommands/docker_network_connect.md)
    - [network create](Subcommands/docker_network_create.md)
    - [network disconnect](Subcommands/docker_network_disconnect.md)
    - [network inspect](Subcommands/docker_network_inspect.md)
    - [network ls](Subcommands/docker_network_ls.md)
    - [network rm](Subcommands/docker_network_rm.md)

---

### Descrição

O **docker network** gerencia redes. Pode-se usar subcomandos para criar, inspecionar, listar, remover, limpar, conectar e desconectar redes.

Por padrão, o docker disponibiliza três redes:
- bridge
- host
- none

O Docker por padrão gerencia os IPs, provendo a comunicação entre os containers, sendo eles já criados na rede bridge, essa informações podem ser pegue via comando [docker inspect](./docker_inspect.md) na sessão de Networks.

O primeiro container docker criado tende a receber o IP 172.17.0.2, com a exclusão deste primeiro container, outros poderão receber este mesmo IP.

---

### Subcomandos

O comando docker network possui diversos subcomandos, que podem ser vistos na subpasta [docker_network](Subcommands/) deste repositório.

---
