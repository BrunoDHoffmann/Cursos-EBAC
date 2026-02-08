from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def auth():
    return {"messege": "Voce acessou a rota padrao de autenticação."}