# Docker NETWORK

### Sumário
- [Descrição](#descrição)
- [Subcomandos](#subcomandos)
    - [network create](./docker_network/docker_network_create.md)
    - [network inspect](./docker_network/docker_network_inspect.md)
    - [network ls](./docker_network/docker_network_ls.md)
    - [network rm](./docker_network/docker_network_rm.md)

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

O comando docker network possui diversos subcomandos, que podem ser vistos na subpasta [docker_network](./docker_network/) deste repositório.

---
