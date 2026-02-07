from fastapi import FastAPI, HTTPException


app = FastAPI()
tarefas = []
    
@app.post("/adicionar")
def adicionar_tarefa(nome: str, descricao: str):
    if any(x['nome'] == nome for x in tarefas):
        raise HTTPException(status_code=400, detail="Essa tarefa já existe.")
    else:
        tarefas.append({'nome': nome, 'descricao': descricao, 'concluida': False})
        return {'messege': 'Tarefa adicionada com sucesso.'}
    
@app.get("/tarefas")
def ler_tarefas():
    if len(tarefas) == 0:
       return {'messege': 'Não existe nenhuma tarefa.'}
    else:
        return {'Tarefas': tarefas} 

@app.put("/atualizar_status/{nome}")
def atualizar_status(nome: str):
    tarefa = next((t for t in tarefas if t["nome"] == nome), None)
    if tarefa == None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada.')
    else:
        tarefa.update({'concluida': True})
        return {'messege': 'Tarefa concluida.'}
    
@app.delete("/deletar/{nome}")
def deletar_tarefa(nome: str):
    tarefa = next((t for t in tarefas if t["nome"] == nome), None)
    if tarefa == None:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada.')
    else:
        tarefas.remove(tarefa)
        return {'messege': 'Tarefa deletada com sucesso.'}