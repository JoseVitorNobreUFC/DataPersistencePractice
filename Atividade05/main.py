from fastapi import FastAPI
from database import create_db_and_tables
from controllers import (
    equipe_controller,
    membro_controller,
    projeto_controller,
    tarefa_controller,
    membership_controller
)

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(equipe_controller.router)
app.include_router(membro_controller.router)
app.include_router(projeto_controller.router)
app.include_router(tarefa_controller.router)
app.include_router(membership_controller.router)
