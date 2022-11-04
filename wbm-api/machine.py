from turtle import pd
from typing import List
from fastapi import FastAPI, Depends, HTTPException
#from pydantic import BaseModel
from sqlalchemy.orm import Session


import crud, schemas, models

from database import SessionLocal, engine



app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

""" class Machine(BaseModel):
    id: int
    name: str

my__db = {1:'La presentación',2:'Salazar2003'}
id = 2 """

@app.post("/usuarios/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):

    db_usuario = crud.get_usuario_por_email(db, usuario.email)
        
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Ya existe el correo")
    return crud.crear_usuario(db=db, usuario=usuario)

@app.get("/usuarios/", response_model=List[schemas.Usuario])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db)
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@app.post("/usuarios/{user_id}/machines/", response_model=schemas.Machine)
def crear_machine_por_usuario(
    usuario_id: int, machine: schemas.MachineCreate, db: Session = Depends(get_db)
):
    return crud.crear_machine_de_usuario(db=db, machine=machine, usuario_id=usuario_id)

@app.get("/machines/", response_model=List[schemas.Machine])
def get_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machines = crud.get_machines(db, skip=skip, limit=limit)
    return machines

""" 
@app.get("/machines/")
async def read_machines_all():
    return {"Machines: ": my__db}

@app.get("/machines/{machine_id}")
async def read_machine(machine_id: int):
    return {"Machine: ": my__db[machine_id]}

@app.post("/machines/{machine_name}")
async def create_machine(machine_name: str, id:int = id):
    id+=1
    my__db[id]=machine_name
    return {"Ingreso exitoso": my__db[id]}

@app.put("/machines/{machine_id}")
async def create_machine(machine: Machine):
    my__db[machine.id]=machine.name
    return {"Machine id": my__db[machine.id]}

@app.delete("/machines/{machine_id}")
async def create_machine(machine_id: int):
    my__db.pop(machine_id)
    return {"Machine id": my__db} """