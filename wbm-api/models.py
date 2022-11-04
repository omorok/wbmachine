from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    documento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    machines = relationship("Machine", back_populates="creador")

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    creador_id = Column(Integer, ForeignKey("usuarios.documento"))

    creador = relationship("Usuario", back_populates="machines")


