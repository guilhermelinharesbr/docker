# --- Estágio 1: Build e instalação de dependências ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Instala dependências de sistema necessárias para compilar pacotes Python (se houver)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cria um ambiente virtual Python isolado para facilitar a cópia limpa depois
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia apenas o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências Python dentro do ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt


# --- Estágio 2: Imagem Final de Produção (Enxuta e Segura) ---
FROM python:3.11-slim AS runner

WORKDIR /app

# Copia o ambiente virtual pronto do estágio anterior
COPY --from=builder /opt/venv /opt/venv

# Configura o PATH para usar o ambiente virtual
ENV PATH="/opt/venv/bin:$PATH"

# Copia o restante do código da aplicação
COPY . .

# 1. Cria um grupo e um usuário do sistema sem privilégios root (UID/GID 1001)
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/sh appuser

# 2. Transfere a propriedade dos arquivos da aplicação para o usuário seguro
RUN chown -R appuser:appgroup /app

# 3. Muda o contexto de execução para o usuário não-root criado
USER appuser

EXPOSE 8000

# Comando para iniciar a aplicação (exemplo com uvicorn para FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
