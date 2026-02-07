from fastapi import FastAPI, HTTPException


app = FastAPI()
lib = {}

@app.get("/livros")
def ler_livros():
    if not lib:
       return {'messege': 'Não existe nenhum livro.'}
    else:
        return {'livros': lib} 
    
@app.post("/adicionar")
def adicionar_livro(id: int, titulo: str, autor: str, ano: int):
    if id in lib:
        raise HTTPException(status_code=400, detail="Esse livro já existe.")
    else:
        lib[id] = {'titulo': titulo, 'autor': autor, 'ano': ano}
        return {'messege': 'Livro adicionado com sucesso.'}

@app.put("/atualizar/{id}")
def atualizar_livro(id: int, titulo: str, autor: str, ano: int):
    if id not in lib:
        raise HTTPException(status_code=404, detail='Livro não encontrado.')
    else:
        if titulo:
            lib[id]['titulo'] = titulo
        if autor:
            lib[id]['autor'] = autor
        if ano:
            lib[id]['ano'] = ano
        return {'messege': 'Informações do livro atualizadas com sucesso.'}
    
@app.delete("/deletar/{id}")
def deletar_livro(id: int):
    if id not in lib:
        raise HTTPException(status_code=404, detail='Livro não encontrado.')
    else:
        del lib[id]
        return {'messege': 'Livro deletado com sucesso.'}