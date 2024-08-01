from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter()

@router.get(
    "/companies/",
)
def get_all_companies():
    return {'message': 'companies'}
    