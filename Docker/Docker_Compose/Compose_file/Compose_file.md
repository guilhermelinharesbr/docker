# Compose File

### Sumário
- [Descrição](#descrição)
- [Instalação](#instalação)


---

### Descrição

Um **compose file** é um arquivo de texto estruturado no formato YAML utilizado pelo Docker Compose. Ele serve para definir e rodar aplicações multi-container de forma declarativa.

A nomenclatura padrão para um arquivo Compose é _**compose.yaml**_ _(preferencial)_ ou **compose.yml** localizado no diretório de trabalho. O Compose também suporta **docker-compose.yaml** e **docker-compose.yml** para compatibilidade com versões anteriores. Se ambos os arquivos existirem, o Compose dará _preferência ao compose.yaml_ canônico.

Em vez de precisar digitar comandos longos no terminal cheios de parâmetros para cada container, como ligar redes, portas, volumes e variáveis de ambiente separadamente, pode-se centraliza toda a arquitetura da sua aplicação em um único arquivo.

Pode-se definir dentro de um Compose File:
- Services (Serviços): Os containers que farão parte da sua aplicação (como um servidor web, um banco de dados e um cache).
- Networks (Redes): Redes virtuais privadas para que os containers consigam se comunicar entre si de forma segura usando apenas o nome do serviço.
- Volumes: Pastas e discos persistentes para garantir que os dados não sejam apagados caso o container seja destruído.
- Environment (Variáveis de ambiente): Configurações sensíveis ou parâmetros de inicialização, como senhas de banco de dados.



---
