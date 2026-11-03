# Usando um container sem rede - driver None

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

A **rede none** é usada quando se quer suibir um container sem uma interface de rede.

O container que estiver com rede _none_ não terá acesso a internet. Essa configuração é muito usada para isolar um container, sendo considerada uma camada a mais de segurança.

---

### Prática

Por padrão o docker disponibiliza três redes, a bridge, a host e a _none_. 
Os containers se comunicam via rede em modo bridge.

Subindo um container sem interface de rede:
```bash
docker container run -dit --network none --name cont-sem-rede alpine

docker container ls -a

docker inspect cont-sem-rede
# Obs: Visto que o conatiner subiu sem interface de rede e está na rede None.
```

---
