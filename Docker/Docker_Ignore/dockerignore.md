# .dockerignore

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Prática](#prática)

---

### Descrição

O arquivo **.dockerignore** é um arquivo de texto usado para dizer ao Docker quais arquivos e pastas da máquina **não devem ser enviados** para dentro do BuildKit quando executar-se um build.

O funcionamento dele é muito parecido com o famoso _.gitignore_ do Git. Quando executa-se o comando docker build, o primeiro passo que o Docker Engine realiza é enviar todo o contexto da pasta do seu projeto (o diretório que é apontado no final do comando, como . ou ./) para o BuildKit (o daemon responsável por construir a imagem).

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
vim .dockerignore
```


```bash
# Ignora diretórios de controle de versão
.git
.gitignore

# Ignora pastas de dependências locais (que devem ser instaladas dentro do container)
node_modules
venv
.env

# Ignora arquivos de log e temporários
*.log
tmp/
*.tmp

# Ignora documentações ou arquivos do próprio projeto que não vão para a imagem
README.md
Dockerfile
compose.yaml
```

---
