# Criando um Compose file

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Neste artigo será mostrado como criar um compose file a partir de um docker run, usando como base um projeto que usa um container de MySQL e outro de Wordpress.

---

### Prática

Serão criados três Dockerfiles:
```bash
# Criando a rede de nome meu-blog, por meio dela os containers vão se comunicar: 
docker network create --driver bridge meu-blog

docker network ls

# Docker run do container do MySQL
docker run -dit --name mysql \
-e MYSQL_DATABASE=wp-example \
-e MYSQL_USER=guilherme \
-e MYSQL_PASSWORD=123456 \
-e MYSQL_ROOT_PASSWORD=123456 \
--mount source=db,target=/var/lib/mysql \
--network meu-blog \
-p 8080:8080 \
mysql:5.7

# Docker run do container do Wordpress 
docker run -dit --name wordpress \
-e WORDPRESS_DB_HOST=mysql \
-e WORDPRESS_DB_USER=guilherme \
-e WORDPRESS_DB_PASSWORD=123456 \
-e WORDPRESS_DB_NAME=wp-example \
--mount source=wordpress,target=/var/www/html \
--network meu-blog \
-p 80:80 \
wordpress:6.2.2​​

docker container ls -a

# A partir deste momento pode-se instalar o Wordpress via navegador por meio do endereço http:ip_da_vm:80.
# Após instalado basta digitar no navegador http:ip_da_vm que poderá ver o conteúdo do blog.

# Matando os containers recém criados com docker run, para mostrar como será subir eles via docker compose:
docker container rm -f $(docker container ls -aq)
docker container ls -a

docker image prune -a
docker image ls

docker volume prune -a
docker volume ls

# Criando o diretório base do projeto:
mkdir /wordpress

# Criando o compose.yaml
# Vale ressaltar que o parâmetro "version" é deprecated só era usado até o Docker Compose V1, a partir do V2 ele não é mais necessário

# Parei em 13 min aula 33

```




---