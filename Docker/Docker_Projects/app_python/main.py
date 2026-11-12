from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="Minha API em Python",
    version="1.0.0",
    description="API de exemplo construída seguindo padrões modernos e seguros."
)

# Modelo de dados usando Pydantic para validação de entrada (Payload)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Rota raiz (Health Check / Boas-vindas)
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Python rodando no Docker com segurança!"}

# Rota de exemplo com parâmetro na URL
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query_param": q}

# Rota POST para receber dados validados
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item criado com sucesso!",
        "item_data": item
    }
