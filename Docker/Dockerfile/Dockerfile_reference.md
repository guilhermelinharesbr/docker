# Dockerfile

### Sumário
- [Descrição](#descrição)
- [Instruções](#instruções)
- [Formato](#formato)
- [Nomenclatura](#nomenclatura)
- [Vantagens](#vantagens)
- [Boas Práticas](#boas-práticas)

---

### Descrição

O Docker pode criar imagens automaticamente lendo as instruções de um **Dockerfile**. Um Dockerfile é um documento de texto que contém todos os comandos que um usuário pode executar na linha de comando para montar uma imagem. 

---

### Instruções

O Dockerfile oferece suporte às seguintes instruções:

| Instrução | Descrição  |
| :--- | :--- |
| **`ADD`** | Adiciona arquivos e diretórios locais ou remotos. |
| **`ARG`** | Usa variáveis ​​de tempo de compilação(build-time) |
| **`CMD`** | Especifica comandos padrão. |
| **`COPY`** | Copia arquivos e diretórios. |
| **`ENTRYPOINT`** | Especifica o executável padrão. |
| **`ENV`** | Define variáveis ​​de ambiente. |
| **`EXPOSE`** | Descrever em quais portas a aplicação está escutando. |
| **`FROM`** | Criar um novo estágio de build a partir de uma imagem base. |
| **`HEALTHCHECK`** | Verificar a integridade/saúde de um container na inicialização. |
| **`LABEL`** | Adiciona metadados a uma imagem. |
| **`MAINTAINER`** (deprecated) | Especifica o autor de uma imagem. Usar a instrução LABEL no lugar. |
| **`ONBUILD`** | Especifica instruções para quando a imagem for usada em uma build. |
| **`RUN`** | Executa comandos de build. |
| **`SHELL`** | Define o shell padrão de uma imagem. |
| **`STOPSIGNAL`** | Especifica o sinal de chamada de sistema para sair de um container. |
| **`USER`** | Define o ID do usuário e do grupo. |
| **`VOLUME`** | Cria volume mounts. |
| **`WORKDIR`** | Altera o diretório de trabalho. |

---

### Formato

Aqui está o formato do Dockerfile:

```bash
# Comment
INSTRUCTION arguments
```
 
---

### Nomenclatura

Por padrão, o Docker espera encontrar o arquivo de configuração exatamente com o nome **Dockerfile** (com a letra _D maiúscula_ e sem nenhuma extensão, como .txt ou .yml).

No entanto, dependendo da estrutura do projeto ou da necessidade de gerenciar múltiplos ambientes, existem diferentes nomenclaturas e convenções utilizadas no mercado:
I) Nome Padrão
    **Dockerfile**: É o nome reconhecido automaticamente pelo comando **docker build** se você não especificar nenhum arquivo.

II) Nomenclaturas por Ambiente (Padrão de Mercado)
Quando um projeto possui diferentes estágios de desenvolvimento, é muito comum utilizar sufixos para diferenciar as receitas:

- **Dockerfile.dev** ou **Dockerfile.development**: Usado para o ambiente de desenvolvimento local (focado em agilidade, com volumes mapeados e ferramentas de debug).
- **Dockerfile.prod** ou **Dockerfile.production**: Usado para gerar a imagem final otimizada e segura para produção (mais limpa e enxuta).
- **Dockerfile.test** ou **Dockerfile\.ci**: Utilizado exclusivamente para rodar testes automatizados em pipelines de CI/CD.
- **Dockerfile.staging**: Usado no ambiente de homologação/pré-produção.

Se for utilizado um nome diferente do padrão (por exemplo, **Dockerfile.prod**), o Docker não o encontrará automaticamente. Para instruí-lo a usar o arquivo correto, você deve utilizar a flag **-f** (ou **--file**) durante o build:

`docker build -f Dockerfile.prod -t meu-app:latest .`

Obs: Dica importante sobre maiúsculas e minúsculas

Em sistemas operacionais baseados em Linux (como o Ubuntu), o sistema de arquivos é case-sensitive (diferencia maiúsculas de minúsculas). Portanto, o nome deve ser estritamente Dockerfile. Criar arquivos como dockerfile ou DOCKERFILE pode fazer com que o Docker falhe em reconhecê-los automaticamente.

Outra forma menos comum de nomear um Dockerfile é colocar o **nome_imagem.dockerfile**, por exemplo [bacula.dockerfile](./Exemplos/bacula.dockerfile), geralmente usado quando existe mais de uma imagem dentro do mesmo projeto.

---

### Vantagens

- Bem mais prático que usar o docker commit
- Controle de versão
- Colaboração da equipe
- Legibilidade

---

### Boas Práticas

Aqui serão listadas algumas boas práticas:

- A **instrução** não diferencia maiúsculas de minúsculas. No entanto, por convenção, ela deve ser escrita em MAIÚSCULAS para diferenciá-la mais facilmente dos **argumentos**;
- **Utilizar imagens base oficiais e leves**: Prefira versões slim ou alpines (ex: python:3.11-slim) para reduzir a superfície de ataque e o tamanho final da imagem.
- **Aproveitar o sistema de cache (Ordem das Instruções)**: O Docker executa as linhas em camadas e guarda o cache de cada uma. Coloque instruções que mudam com pouca frequência no topo (como instalação de dependências do sistema) e alteração de códigos-fonte mais abaixo. Assim, alterações no código não invalidam o cache das bibliotecas pesadas.
- **Evitar usar o usuário root**: Por padrão, os containeres rodam com privilégios de root. Utilizar a instrução USER para criar e executar a aplicação com um usuário sem privilégios, aumentando a segurança.
- **Usar o arquivo .dockerignore**: Assim como o .gitignore, ele impede que arquivos desnecessários (como pastas locais de testes, logs, git ou ambientes virtuais) sejam enviados para o contexto de build, acelerando o processo e evitando vazamento de dados.
- **Agrupar comandos RUN**: Cada instrução RUN cria uma nova camada na imagem. Agrupar comandos usando **&&** e limpando caches temporários na mesma linha reduz o número de camadas e o tamanho do arquivo final.
    - Manter imagens Docker leves, seguras e padronizadas exige atenção rigorosa ao uso dos gerenciadores de pacotes (**apt**, **dnf** ou **apk**). O principal erro que incha as imagens e expõe falhas de segurança é deixar caches de pacotes e ferramentas de compilação nas camadas finais da imagem. As quatro principais regras de ouro para gerenciar pacotes no Dockerfile são:
        - **Instalar e limpar no mesmo comando RUN**: O Docker cria uma camada para cada instrução. Ao atualizar os repositórios, instalar pacotes e limpar o cache em comandos RUN separados, o lixo continuará ocupando espaço nas camadas anteriores. Tudo deve acontecer em uma única linha usando **&&**.
        - **Desativar pacotes recomendados/opcionais** (apt): No Debian/Ubuntu, o apt instala por padrão pacotes recomendados que você quase nunca usa.
        - **Limpar o cache do gerenciador**: Remover os arquivos temporários de cache antes de fechar a camada.
        - **Fixar versões** (opcional, mas recomendado para estabilidade): Evitar surpresas em builds futuros.

**Exemplos práticos de como agrupar comandos RUN** para deixar a imagem leve, divido por gerenciadores de pacotes:

Usando **apt** (Debian / Ubuntu):

O **apt** é o mais verboso e costuma trazer mais dependências opcionais. Para mantê-lo limpo:

```dockerfile
FROM ubuntu:24.04

# Evita perguntas interativas durante a instalação de pacotes
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
```

Obs: O que foi feito: O **--no-install-recommends** impede a instalação de pacotes supérfluos, e o __rm -rf /var/lib/apt/lists/*__ apaga o catálogo de pacotes baixados pelo apt-get update, economizando dezenas de megabytes.

Criando uma imagem _Sem_ usar as melhores práticas do apt no RUN:
`docker build -t myapp-versao-apt:1.0.0 .`

Criando uma imagem _Usando_ as melhores práticas do apt no RUN:
`docker build -t myapp-versao-apt:2.0.0 .`

Os resultados dos testes foram que ao criar uma imagem do Ubuntu 24.04 sem as melhores práticas do APT no RUN ela ficou com 98.7MB, já utilizando as melhores práticas dentro do mesmo RUN a imagem ficou com 55.5MB.

--

Usando **dnf** (Red Hat / Rocky Linux / Fedora):

O dnf (sucessor do yum) também armazena caches pesados de metadados que precisam ser limpos explicitamente:

```dockerfile
FROM rockylinux:9

RUN dnf install -y \
    curl-minimal \
    git \
    && dnf clean all \
    && rm -rf /var/cache/dnf
```

Obs: O que foi feito: O dnf clean all limpa os dados gerados pelos repositórios e o rm -rf /var/cache/dnf garante que nenhum resíduo de cache persista na camada.

Criando uma imagem _Sem_ usar as melhores práticas do dnf no RUN:
`docker build -t myapp-versao-dnf:1.0.0 .`

Criando uma imagem _Usando_ as melhores práticas do dnf no RUN:
`docker build -t myapp-versao-dnf:2.0.0 .`

Os resultados dos testes foram que ao criar uma imagem do Rocky Linux 9 sem as melhores práticas do DNF no RUN ela ficou com 208MB, já utilizando as melhores práticas dentro do mesmo RUN a imagem ficou com 97.8MB.

--

Usando **apk** (Alpine Linux):

O apk é o gerenciador do Alpine (nativo de imagens super leves). Ele já é muito eficiente por padrão, mas possui uma flag fantástica para evitar salvar o índice localmente:

```dockerfile
FROM alpine:3.20

RUN apk add --no-cache \
    curl \
    git
```

Obs: O que foi feito: A flag **--no-cache** diz ao apk para atualizar o índice e instalar o pacote diretamente sem salvar o arquivo de cache localmente no disco, dispensando comandos extras de limpeza como rm -rf.

Criando uma imagem _Sem_ usar as melhores práticas do apk no RUN:
`docker build -t myapp-versao-apk:1.0.0 .`

Criando uma imagem _Usando_ as melhores práticas do apk no RUN:
`docker build -t myapp-versao-apk:2.0.0 .`

Os resultados dos testes foram que ao criar uma imagem do Alpine 3.20 sem as melhores práticas do APK no RUN ela ficou com 12.3MB, já utilizando as melhores práticas dentro do mesmo RUN a imagem ficou com 9.95MB.

---
