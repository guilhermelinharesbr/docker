# Criando uma Rede docker BRIDGE

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar uma rede docker por meio do comando [docker network](/Docker/Docker_Commands/docker_network.md).

---

### Prática

Por padrão o docker disponibiliza três redes, a _bridge_, a host e a none. 
Os containers se comunicam via rede em modo bridge.

Mostrando a comunicação básica de dois containers:
```bash
docker image pull alpine

docker container run -dit --name cont-1 alpine
docker container run -dit --name cont-2 alpine

# Descobrindo os IPs dos containers:
docker inspect cont-1
docker inspect cont-2
# Obs: No caso foram 172.17.0.2 e 172.17.0.3 e ambos estão na rede Bridge.

docker exec -it cont-1 sh
# Mostrando que é possível pingar de um container para o outro:
ping 172.17.0.3
# Mostrando que via rede Bridge padrão do docker não é possível pingar via nome de container:
ping cont-2

# Logando neste container, mas em outro terminal:
docker exec -it cont-2 sh
# Mostrando que é possível pingar de um container para o outro:
ping 172.17.0.2
# Mostrando que via rede Bridge padrão do docker não é possível pingar via nome de container:
ping cont-1
```

Mostrando como fazer um ping no nome de container, via uma rede docker criada manualmente:
```bash
# Criando uma rede com driver bridge de nome minha-rede:
docker network create --driver bridge minha-rede

docker network ls 

# Desconectando da rede bridge o container de nome cont-1:
docker network disconnect bridge cont-1
# Mostrando que agora o cont-1 está sem rede, essa informação é pegue na sessão Networks:
docker inspect cont-1

docker network disconnect bridge cont-2
docker inspect cont-2

# Conectando a rede de nome minha-rede no cont-1:
docker network connect minha-rede cont-1
# Mostrando que agora o container está conectado na minha-rede e seu novo ip 172.18.0.2:
docker inspect cont-1

docker network connect minha-rede cont-2
# Mostrando que agora o container está conectado na minha-rede e seu novo ip 172.18.0.3:
docker inspect cont-2

docker exec -it cont-1 sh
# Mostrando que é ainda possível pingar de um container para o outro via IP:
ping 172.18.0.3
# Mostrando que via rede de nome minha-rede com driver Bridge é possível pingar via nome de container:
ping cont-2

docker exec -it cont-2 sh
# Mostrando que é ainda possível pingar de um container para o outro via IP:
ping 172.18.0.2
# Mostrando que via rede de nome minha-rede com driver Bridge é possível pingar via nome de container:
ping cont-1
```

Mostrando como criar um container já com uma rede específica, ao invés de alterar a rede, como foi mostrado mais acima:
```bash
docker container ls -a
docker container rm -f cont-1 cont-2
docker container ls -a

# Criando o container já com a rede de nome minha-rede:
docker container run -dit --network minha-rede --name cont-1 alpine
# Mostrando que o container já foi criado com a minha-rede e ip 172.18.0.2:
docker inspect cont-1

docker container run -dit --network minha-rede --name cont-2 alpine
# Mostrando que o container já foi criado com a minha-rede e ip 172.18.0.3:
docker inspect cont-2

docker exec -it cont-1 sh
# Mostrando que é possível pingar de um container para o outro via IP:
ping 172.18.0.3
# Mostrando que via rede de nome minha-rede com driver Bridge é possível pingar via nome de container:
ping cont-2

docker exec -it cont-2 sh
# Mostrando que é possível pingar de um container para o outro via IP:
ping 172.18.0.2
# Mostrando que via rede de nome minha-rede com driver Bridge é possível pingar via nome de container:
ping cont-1
```

---
