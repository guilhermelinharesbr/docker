# Docker COMPOSE

### Sumário
- [Descrição](#descrição)
- [Instalação](#instalação)
- [docker-compose standalone (legado)](#docker-compose-standalone-legadoo)
- [Subcomandos](#subcomandos)
    - [compose down](Subcommands/docker_compose_down.md)
    - [compose up](Subcommands/docker_compose_up.md)
    - [compose version](Subcommands/docker_compose_version.md)

---

### Descrição

O **docker compose** é uma ferramenta para definir e executar aplicações com múltiplos contêineres. É a chave para uma experiência de desenvolvimento e implantação simplificada e eficiente.

O Compose simplifica o controle de toda a sua pilha de aplicações, facilitando o gerenciamento de serviços, redes e volumes em um único arquivo de configuração **YAML**. Em seguida, com um único comando, você cria e inicia todos os serviços a partir do seu arquivo de configuração.

O Compose funciona em todos os ambientes: produção, homologação, desenvolvimento, teste e fluxos de trabalho de CI. Ele também possui comandos para gerenciar todo o ciclo de vida da sua aplicação:

- Iniciar, parar e reconstruir serviços
- Visualizar o status dos serviços em execução
- Transmitir o log de saída dos serviços em execução
- Executar um comando único em um serviço

---

### Instalação

Instalando/atualizando o docker compose nos derivados do Debian:
```bash
sudo apt update
sudo apt install docker-compose-plugin
docker compose version
```

Instalando/atualizando o docker compose nos derivados do Red Hat:
```bash
sudo yum update
sudo yum install docker-compose-plugin
docker compose version
```

### docker-compose standalone (legado)

Por já estar deprecate é aconselhado a não ser mais instalado, nesta sessão do artigo serão mostrado mais informações sobre o docker-compose.

A **diferença** principal entre **docker-compose** (com hífen) e **docker compose** (sem hífen) está na arquitetura, versão e em quem desenvolveu a ferramenta:

**docker compose** (Versão 2 / Atual):
- O que é: É o plugin oficial moderno integrado diretamente ao Docker CLI.
- Como é chamado: Como um subcomando do Docker (docker compose).
- Tecnologia: Escrito em Go (a mesma linguagem do Docker Engine), o que traz muito mais performance, consumo eficiente de recursos e paridade total com os comandos nativos do Docker.
- Compatibilidade: É o padrão recomendado pela Docker em todas as versões modernas (Ubuntu 26.04, Docker Desktop recente, etc.).

**docker-compose** (Versão 1 / Legado)
- O que é: A versão antiga e clássica da ferramenta.
- Como é chamado: Como um comando separado e autônomo (docker-compose).
- Tecnologia: Escrito em Python.
- Status atual: Obsoleto (Deprecated). O suporte oficial e atualizações de segurança para essa versão legada foram encerrados.

---

### Subcomandos

O comando docker compose possui diversos subcomandos, que podem ser vistos na subpasta [Docker_Compose](Subcommands/) deste repositório.

---
