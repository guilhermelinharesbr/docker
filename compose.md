# Docker Compose


### Sumário

- [Definição](#definição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)
- [COMANDOS](#comandos)
- []()


---

#### Definição


---

#### Fonte de Pesquisa


---

### COMANDOS



---

#### compose down

Usado para matar os containers que estejam dentro do arquivo docker-compose. O docker-compose não é isntalado por padrão com o docker é preciso usar `sudo apt install docker-compose -y`.

Também exclui a rede criada no docker-compose. Podendo confirmar a exlcusão da rede via [docker network ls AJUSTAR](#?????????????????????).
 
```bash
docker-compose down
ou
docker-compose -f file_name down
ou
docker-compose -f docker-compose.yaml down 
ou
docker-compose -f docker-compose.yml down 
```

---
