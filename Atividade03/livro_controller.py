from fastapi import FastAPI, HTTPException
from livro_model import LivroCreate
import livro_service
app = FastAPI()

@app.get("/")
def get_all_livros():
    return livro_service.get_all_livros()

@app.get("/{livro_id}")
def get_livro_by_id(livro_id: int):
    livro = livro_service.get_livro_by_id(livro_id)
    return livro

@app.post("/")
def create_livro(livro: LivroCreate):
    return livro_service.create_livro(livro)

@app.put("/{livro_id}")
def update_livro(livro_id: int, livro: LivroCreate):
    success = livro_service.update_livro(livro_id, livro)
    if not success:
        raise HTTPException(status_code=404, detail="Livro não encontrado para atualização")
    return {"message": "Livro atualizado com sucesso"}

@app.delete("/{livro_id}")
def delete_livro(livro_id: int):
    success = livro_service.delete_livro(livro_id)
    if not success:
        raise HTTPException(status_code=404, detail="Livro não encontrado para exclusão")
    return {"message": "Livro deletado com sucesso"}
