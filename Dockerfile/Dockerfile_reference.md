# Dockerfile

### Sumário
- [Descrição](#descrição)
- [Instruções](#instruções)
- [Formato](#formato)
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
| **`ARG`** | Usaa variáveis ​​de tempo de compilação(build-time) |
| **`CMD`** | Especifica comandos padrão. |
| **`COPY`** | Copia arquivos e diretórios. |
| **`ENTRYPOINT`** | Especifica o executável padrão. |
| **`ENV`** | Define variáveis ​​de ambiente. |
| **`EXPOSE`** | Descrever em quais portas a aplicação está escutando. |
| **`FROM`** | Criar um novo estágio de build a partir de uma imagem base. |
| **`HEALTHCHECK`** | Verificar a integridade/saúde de um container na inicialização. |
| **`LABEL`** | Adiciona metadados a uma imagem. |
| **`MAINTAINER`** | Especifica o autor de uma imagem. |
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


### Boas Práticas

Aqui serão listadas algumas boas práticas:

- A **instrução** não diferencia maiúsculas de minúsculas. No entanto, por convenção, ela deve ser escrita em MAIÚSCULAS para diferenciá-la mais facilmente dos **argumentos**;
- **Utilizar imagens base oficiais e leves**: Prefira versões slim ou alpines (ex: python:3.11-slim) para reduzir a superfície de ataque e o tamanho final da imagem.
- **Aproveitar o sistema de cache (Ordem das Instruções)**: O Docker executa as linhas em camadas e guarda o cache de cada uma. Coloque instruções que mudam com pouca frequência no topo (como instalação de dependências do sistema) e alteração de códigos-fonte mais abaixo. Assim, alterações no código não invalidam o cache das bibliotecas pesadas.
- **Agrupar comandos RUN**: Cada instrução RUN cria uma nova camada na imagem. Agrupar comandos usando **&&** e limpando caches temporários na mesma linha reduz o número de camadas e o tamanho do arquivo final.
- **Evitar usar o usuário root**: Por padrão, os containeres rodam com privilégios de root. Utilizar a instrução USER para criar e executar a aplicação com um usuário sem privilégios, aumentando a segurança.
- **Usar o arquivo .dockerignore**: Assim como o .gitignore, ele impede que arquivos desnecessários (como pastas locais de testes, logs, git ou ambientes virtuais) sejam enviados para o contexto de build, acelerando o processo e evitando vazamento de dados.

---
