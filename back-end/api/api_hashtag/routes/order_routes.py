from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de pedidos."}