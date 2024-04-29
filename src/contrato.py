from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

"""Classe de contrato de daddos de vendas."""


class CategoriaEnum(str, Enum):
    categoria1 = "A"
    categoria2 = "B"
    categoria3 = "C"


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
