from typing import List

from pydantic import BaseModel


class MachineBase(BaseModel):
    nombre: str
    descripcion: str | None


class MachineCreate(MachineBase):
    pass


class Machine(MachineBase):
    id: int
    creador_id: int

    class Config:
        orm_mode = True


class UsuarioBase(BaseModel):
    documento: int
    nombre: str
    email: str


class UsuarioCreate(UsuarioBase):
    
    password: str


class Usuario(UsuarioBase):
    
    Machines: List[Machine] = []

    class Config:
        orm_mode = True