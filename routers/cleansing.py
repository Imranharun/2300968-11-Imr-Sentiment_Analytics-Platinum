import pandas as pd
from fastapi import APIRouter
from fastapi import Query
from fastapi import UploadFile
from services.cleansing import cleansing

router = APIRouter()

@router.get("/cleansing/text")
async def text_cleansing(
    sentence: str = Query(default = "")
):
    result = await cleansing(sentence)
    return result