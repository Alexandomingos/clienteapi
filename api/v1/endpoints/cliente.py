from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.cliente_model import Cliente
from core.deps import get_seession

router = APIRouter()

# POST CLIENTE
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Cliente)
async def post_cliente(cliente: Cliente, db:AsyncSession = Depends(get_seession)):
    novo_cliente = Cliente(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone)

    db.add(novo_cliente)
    await db.commit()

    return novo_cliente

# Get Clientes
@router.get('/', response_model=List[Cliente])
async def get_clientes(db: AsyncSession = Depends(get_seession)):
    async with db as session:
        query = select(Cliente)
        result = await session.execute(query)
        clientes: List[Cliente] = result.scalars().all()


        return clientes
    

# Get Cliente
@router.get('/{cliente_id}', response_model=Cliente, status_code=status.HTTP_200_OK)
async def get_cliente(cliente_id: int, db: AsyncSession = Depends(get_seession)):
    async with db as session:
        query = select(Cliente).filter(Cliente.id == cliente_id)
        result = await session.execute(query)
        cliente: Cliente = result.scalar_one_or_none()

        if cliente:
            return cliente
        else:
            raise HTTPException(detail='Cliente não encontrado', status_code=status.HTTP_404_NOT_FOUND)
