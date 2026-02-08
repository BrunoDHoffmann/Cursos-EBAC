from fastapi import APIRouter, Depends
from models.models import Usuario 
from dependencies.dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de autenticação."}

@auth_router.post("/criar_conta")
async def criar_conta(nome : str, email : str, senha : str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"message" : "Usuario já cadastrado"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"message" : "Sua conta foi criada com sucesso"}