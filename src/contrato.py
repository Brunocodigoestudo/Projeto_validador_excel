from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

"""Classe de contrato de daddos de vendas."""


class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


"""Arg:
    email: str
    Data: date 
    valor: Positive 
    Produto: str
    Quant: Positive
    categoria: str
"""


class Vendas(BaseModel):
    Email: EmailStr
    Data: datetime
    Valor: PositiveFloat
    Produto: str
    Quantidade: PositiveInt
    Categoria: CategoriaEnum

    @field_validator('Categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error
