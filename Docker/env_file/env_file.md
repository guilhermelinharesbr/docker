# .env

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Prática](#prática)

---

### Descrição

O arquivo **.env** é um arquivo de texto simples usado para armazenar variáveis de ambiente de forma centralizada e isolada. No ecossistema do **Docker** e do **Docker Compose**, ele desempenha um papel fundamental: separar as configurações e credenciais sensíveis (como senhas de banco de dados, chaves de API e portas) do código da aplicação ou da estrutura do arquivo de configuração.

Quando utiliza-se o _Docker Compose_, ele procura automaticamente por um arquivo chamado _.env_ na mesma pasta onde o _compose.yaml_ está salvo.

O **funcionamento** baseia-se em duas etapas:
- **Armazenamento**: definição variáveis no formato CHAVE=VALOR dentro do .env.
- **Injeção**: O Docker Compose lê essas variáveis e permite a utilização dentro do compose.yaml usando a sintaxe de interpolação ${NOME_DA_VARIAVEL}. O Docker Engine se encarrega de repassá-las para dentro dos containers.

Algumas **Vantagens** de usar o .env:
- **Segurança** (Evita vazamentos): O arquivo .env com senhas reais e confidenciais fica armazenado apenas na sua máquina local ou no servidor seguro. Ele nunca deve ser enviado para o controle de versão (como o Git). Para isso, deve-se sempre adicionar o .env dentro do seu .gitignore.
- **Reutilização de ambientes**: Pode-se ter arquivos .env diferentes para cada cenário (ex: .env.development, .env.production), permitindo subir a mesma estrutura de containers alterando apenas as variáveis de ambiente sem precisar mexer no compose.yaml.
- **Manutenção facilitada**: Se a senha do banco de dados mudar, basta alterar em apenas um lugar (.env) em vez de ter que caçar e substituir em vários arquivos de configuração.

Obs: Lembrando que arquivos começados com . como o .env, no linux são tratados como ocultos, para listá-los usar `ls -lha`.

Obs2: Quando usa-se um .env em um projeto com **compose.yaml** pode-se usar os parâmetros **environment** ou **env_file**, com ambos funciona.

---

### Sintaxe

Regras e Sintaxe básica:

- **Comentários** -> Usar **#** no ínicio da linha.
- Curingas (**Wildcards**): Us __*__ para múltiplos caracteres ou __?__ para um único caractere (ex: *.log ignora todos os logs).
- **Negação**: O ponto de exclamação **!** serve como exceção, reabrindo a inclusão de um arquivo previamente ignorado (ex: !important.log).
- **Localização**: Ele deve estar posicionado na **raiz do projeto**, no mesmo diretório onde fica o Dockerfile.

---

### Prática

Criando o arquivo .dockerignore na raiz do projeto:
```bash
vim .env
```


```bash
# Configurações de Rede e Portas
DB_PORT=3306
WP_PORT=80

# Credenciais do Banco de Dados
MYSQL_ROOT_NAME=root
MYSQL_ROOT_PASSWORD=senha_super_secreta_root
MYSQL_DATABASE=meu_banco_producao
MYSQL_USER=guilherme
MYSQL_PASSWORD=senha_usuario_123

# Configurações do WordPress
WP_DB_HOST=mysql_db
```

Mostrando como é o uso do .env em um compose file:
```bash
vim compose.yaml
```

```yaml
services:
  wordpress:
    image: wordpress:6.2.2
    container_name: meu_blog_app
    restart: always
    ports:
      - "${WP_PORT}:80"
    environment:
      WORDPRESS_DB_HOST: "${WP_DB_HOST}:${DB_PORT}"
      WORDPRESS_DB_USER: "${MYSQL_USER}"
      WORDPRESS_DB_PASSWORD: "${MYSQL_PASSWORD}"
      WORDPRESS_DB_NAME: "${MYSQL_DATABASE}"
    volumes:
      - wordpress_data:/var/www/html
    networks:
      - rede_interna

  db:
    image: mysql:5.7
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "${MYSQL_ROOT_PASSWORD}"
      MYSQL_DATABASE: "${MYSQL_DATABASE}"
      MYSQL_USER: "${MYSQL_USER}"
      MYSQL_PASSWORD: "${MYSQL_PASSWORD}"
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - rede_interna

networks:
  rede_interna:
    driver: bridge

volumes:
  wordpress_data:
  mysql_data:
```

Subindos os containers:
```bash
docker compose up -d
```

Confirmando que as imagens foram baixadas, containers, volumes e redes foram criados:
```bash
docker image ls
docker container ls -a
docker volume ls
docker network ls
docker compose ps
```

---
