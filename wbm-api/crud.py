from sqlalchemy.orm import Session

import models, schemas


def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.documento == usuario_id).first()


def get_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    password = usuario.password
    db_usuario = models.Usuario(documento=usuario.documento, nombre=usuario.nombre, email=usuario.email, password=password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def get_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Machine).offset(skip).limit(limit).all()


def crear_machine_de_usuario(db: Session, machine: schemas.MachineCreate, usuario_id: int):
    db_machine = models.Machine(**machine.dict(), owner_id=usuario_id)
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine