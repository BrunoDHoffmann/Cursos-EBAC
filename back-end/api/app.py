from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
tarefas = []
    
class Tarefa(BaseModel):
    nome : str
    descricao : str
    concluida : Optional[bool] = False
    
@app.post("/adicionar")
async def adicionar_tarefa(tarefa: Tarefa):
    if any(t.nome == tarefa.nome for t in tarefas):
        raise HTTPException(status_code=400, detail="Essa tarefa já existe.")
    else:
        tarefas.append(tarefa)
        return {'message': 'Tarefa adicionada com sucesso.'}
    
@app.get("/tarefas")
async def ler_tarefas():
    if len(tarefas) == 0:
       return {'message': 'Não existe nenhuma tarefa.'}
    else:
        return {'Tarefas': tarefas} 

@app.put("/atualizar_status/{nome}")
async def atualizar_status(nome: str):
    tarefa = next((t for t in tarefas if t.nome == nome), None)
    if tarefa is None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada.')
    else:
        tarefa.concluida = True
        return {'message': 'Tarefa concluida.'}
    
@app.delete("/deletar/{nome}")
async def deletar_tarefa(nome: str):
    tarefa = next((t for t in tarefas if t.nome == nome), None)
    if tarefa is None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada.')
    else:
        tarefas.remove(tarefa)
        return {'message': 'Tarefa deletada com sucesso.'}