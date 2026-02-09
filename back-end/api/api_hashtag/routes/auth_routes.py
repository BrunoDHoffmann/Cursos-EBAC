from fastapi import APIRouter, Depends, HTTPException
import sys
import os
from main import bcrypt_context
from models.models import Usuario 
from routes.dependencies.dependencies import pegar_sessao
from schemas.schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session 

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

def criar_token(id_usuario):
    token = f"dioawndoiawhdohdo{id_usuario}"
    return token

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de autenticação."}

@auth_router.post("/create_account")
async def criar_conta(usuario_schema : UsuarioSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message" : "Sua conta foi criada com sucesso"}
    
@auth_router.post("/login")
async def login(login_schema : LoginSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Email não cadastrado.")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token" : access_token,
            "token_type" : "Bearer"
        }