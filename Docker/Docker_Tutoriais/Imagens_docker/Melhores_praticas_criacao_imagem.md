# Melhores Práticas na criação de imagens Docker

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como criar uma imagem Docker seguindo as melhores práticas.

Entre elas temos:

1. **Versionamento Semântico** (SemVer), pois evita o caos de nomes genéricos e diz exatamente o grau de impacto de uma atualização.
1.1. _Exemplo_:  
Imagine que sua API recebeu um novo endpoint de listagem que não quebra nada existente. Você sobe a versão de 1.2.0 para 1.3.0. Se você corrigiu apenas um bug crítico de conexão com o banco, vai para 1.2.1. Se mudou a estrutura de dados de forma que quebra a versão anterior, vai para 2.0.0.

2. **Evitar a tag ambígua latest** em produção, pois esta tag é um alvo móvel. Se você faz o deploy dela e ocorre um erro, você não sabe exatamente qual código está rodando, dificultando o rollback (reversão).
2.1. _Exemplo_:  
Em vez de usar `image: minha-api:latest` no seu _arquivo de manifesto do Kubernetes_ ou _Docker Compose_, aponte sempre para uma versão imutável e específica, como por exemplo `image: minha-api:1.0.0`

3. **Distinguir ambientes com clareza**,pois previne erros humanos, como mandar uma imagem de _testes_ direto para o servidor de _homologação_ ou _produção_.
3.1. _Exemplo_:  
- Versão de desenvolvimento/testes locais: minha-api:1.3.0-**rc1** (Release Candidate).
- Versão de homologação: minha-api:1.3.0-**staging**
- Versão de produção: minha-api:1.3.0-**prod**

4. **Limpeza regular de tags antigas** (Lifecycle / Prune), pois acumular centenas de versões de testes em um ambiente corporativo consome espaço de armazenamento desnecessariamente e polui a visualização do repositório.
4.1. _Exemplo_:
Configurar regras de retenção automática no seu Registry privado (como Nexus, Harbor ou GitLab Registry) para manter apenas as últimas 5 versões de staging e as últimas 10 versões de prod, apagando o restante automaticamente após 30 dias.

5. **Incluir metadados relevantes** (Datas ou Hashes do Git), pois ajuda a cruzar a imagem que está rodando em produção diretamente com o código exato no repositório.
5.1. _Exemplo_:
Você pode automatizar a criação da tag usando o hash curto do commit do Git em que o código foi compilado:

```bash
# Pegando os 7 primeiros caracteres do commit atual do Git
GIT_COMMIT=$(git rev-parse --short HEAD)
docker build -t minha-api:1.3.0-$GIT_COMMIT .
# A tag resultante será: minha-api:1.3.0-a1b2c3d
```

6. **Automatizar a rotulagem em pipelines de CI/CD**, pois os processos manuais geram erros de digitação e esquecimentos. O pipeline deve gerar a tag baseado na tag do Git criada pelo desenvolvedor.
6.1. _Exemplo_:
(Conceito em pipeline): Quando um desenvolvedor cria uma tag de release no Git (git tag v1.3.0), o GitHub Actions ou GitLab CI lê essa tag automaticamente e executa:

```yaml
script:
  - docker build -t registry.empresa.com/minha-api:${CI_COMMIT_TAG} .
  - docker push registry.empresa.com/minha-api:${CI_COMMIT_TAG}
```

---

### Prática

Agora será mostrado um exemplo completo e integrado de como aplicar essas melhores práticas, utilizando Docker Compose, Versionamento Semântico (SemVer) e automação com o hash do Git.

Como o Docker Compose por si só não calcula o hash do Git de forma nativa na linha de comando de maneira automática, a melhor abordagem no mundo real é usar uma variável de ambiente alimentada pelo terminal ou pelo seu pipeline de CI/CD.

1. O **Projeto** (Estrutura de Arquivos)
Imagine que você tem a seguinte estrutura para a sua API Python:

```txt
meu-projeto/
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── main.py
```

2. O **Dockerfile** (Multi-stage e Seguro)
Utilizamos um build otimizado, usuário não-root e sem dependências desnecessárias:

```dockerfile
# Estágio de Build
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
RUN python -m venv /opt/venv
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Estágio de Execução Final
FROM python:3.11-slim AS runner
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY . .

# Criando usuário não-root por segurança
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/sh appuser && \
    chown -R appuser:appgroup /app

USER appuser
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

3. O **compose.yaml** Dinâmico. Note que a propriedade image usa uma variável de ambiente (${APP_VERSION}). Isso permite que o Compose aponte exatamente para a versão gerada, fugindo completamente do perigo da tag latest.


```yaml
services:
  api:
    build: .
    image: minha-api-python:${APP_VERSION:-1.0.0}
    container_name: api-python-segura
    ports:
      - "8000:8000"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/')"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
```

4. Criando o **requirements.txt**, onde contém apenas as dependências essenciais e fixadas para manter a aplicação enxuta e segura:

```txt
fastapi==0.115.0
uvicorn[standard]==0.31.0
pydantic==2.9.2
```

5. Criando o **main.py**, que é o código principal da API utilizando o Pydantic para validação robusta de dados (garantindo que os campos e tipos cheguem corretos):

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Minha API Python Segura",
    version="1.0.0",
    description="API FastAPI conteinerizada com boas práticas de segurança."
)

# Modelo de dados esperado no POST (Validação automática via Pydantic)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Rota GET simples (Raiz)
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Python rodando no Docker de forma segura!"}

# Rota GET com parâmetro de caminho e de consulta (query)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Rota POST para criação de dados
@app.post("/items/")
def create_item(item: Item):
    return {
        "mensagem": "Item criado com sucesso!",
        "item": item
    }
```

6. Como construir e subir usando SemVer + Hash do Git na prática
Para unir a versão semântica (ex: 1.2.0) com o hash do commit atual do Git, você pode rodar os comandos diretamente no terminal combinando variáveis de ambiente.

Abra o terminal na pasta do projeto e execute:

```bash
# 1. Captura a versão semântica desejada
export VERSION="1.2.0"

# 2. Captura automaticamente os 7 primeiros caracteres do commit atual do Git
export GIT_COMMIT=$(git rev-parse --short HEAD)

# 3. Junta tudo em uma tag rica e rastreável (Ex: 1.2.0-a1b2c3d)
export APP_VERSION="${VERSION}-${GIT_COMMIT}"

echo "Gerando build para a versão: $APP_VERSION"

# 4. Faz o build informando essa tag para o Docker Compose
docker compose build --build-arg APP_VERSION=$APP_VERSION

# 5. Sobe o container baseado exatamente nessa tag versionada
docker compose up -d
```

Agora ao rodar `docker image ls`, verá que sua imagem foi gerada com uma tag profissional e rastreável (por exemplo: **minha-api-python:1.2.0-a1b2c3d**).

Se houver um bug em produção, você bate o olho na tag e sabe exatamente qual versão do código-fonte no repositório originou aquela imagem, bastando olhar o histórico do Git.

---
