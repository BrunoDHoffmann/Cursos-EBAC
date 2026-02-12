from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from pydantic import BaseModel
from typing import Optional
import secrets

app = FastAPI()
lib = {}

MY_USER = 'admin'
MY_PASSWORD = 'admin'

security = HTTPBasic()

class Livro(BaseModel):
    titulo : str
    autor : str
    ano : int
    

def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_user_correct = secrets.compare_digest(credentials.username, MY_USER)
    is_password_correct = secrets.compare_digest(credentials.username, MY_PASSWORD)
    
    if not (is_user_correct and is_password_correct):
        raise HTTPException(status_code=401, detail='Não autorizado', headers={'WWW-autenticate': 'basic'})


@app.get("/livros")
def ler_livros(credentials : HTTPBasicCredentials = Depends(autenticar_usuario)):
    if not lib:
       return {'messege': 'Não existe nenhum livro.'}
    else:
        return {'livros': lib} 

    
@app.post("/adicionar")
def adicionar_livro(id: int, livro: Livro, credentials : HTTPBasicCredentials = Depends(autenticar_usuario)):
    if id in lib:
        raise HTTPException(status_code=400, detail="Esse livro já existe.")
    else:
        lib[id] = livro.dict()
        return {'messege': 'Livro adicionado com sucesso.'}

@app.put("/atualizar/{id}")
def atualizar_livro(id: int, livro: Livro, credentials : HTTPBasicCredentials = Depends(autenticar_usuario)):
    if id not in lib:
        raise HTTPException(status_code=404, detail='Livro não encontrado.')
    else:
        lib[id] = livro.dict()
        return {'messege': 'Informações do livro atualizadas com sucesso.'}
    
@app.delete("/deletar/{id}")
def deletar_livro(id: int, credentials : HTTPBasicCredentials = Depends(autenticar_usuario)):
    if id not in lib:
        raise HTTPException(status_code=404, detail='Livro não encontrado.')
    else:
        del lib[id]
        return {'messege': 'Livro deletado com sucesso.'}