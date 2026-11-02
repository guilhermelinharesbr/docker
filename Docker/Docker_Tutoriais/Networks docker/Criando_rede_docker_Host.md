# Criando uma Rede docker HOST

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

A **rede host** é usada quando se quer inserir o container na rede do host dele, por exemplo a mesma rede da VM.

---

### Prática

Por padrão o docker disponibiliza três redes, a bridge, a _host_ e a none. 
Os containers se comunicam via rede em modo bridge.

Subindo um container já na rede host:
```bash
docker container run -dit --network host --name static-site  dockersamples/static-site
# Obs: Como o container foi inserido na rede host, não é necessário fazer nenhum mapeamento de portas.

# Visto que o conatiner está na rede host, ou seja na mesma faixa de rede do host do Docker, no caso uma VM Ubuntu:
docker inspect static-site
# Obs: Para acessar aplicação basta digitar no navegador http://localhost ou http://ip_da_vm.
```

---
