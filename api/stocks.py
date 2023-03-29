from typing import Tuple, List, Optional

from fastapi import APIRouter, Request, Body, status, HTTPException
# from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
# from models import CarBase

router = APIRouter()

# student_collection = database.get_collection("students_collection")


# helpers


def stock_helper(stock) -> dict:
    return {
        "id": str(stock["_id"]),
        "close": stock["close"],
        "date": stock["date"],
    }



@router.get("/", response_description="List all stocks")
def list_stocks():

    # get all stock collections from the database

    return {"stocks": "List of all stocks"}

@router.get("/{stock_id}", response_description="Get a single stock")
async def show_stock(stock_id: str, request: Request):

    # get a single stock collection from the database and return the result to the user

    print(f"stock_id: {stock_id}")
    
    stock_collection = request.app.mongodb.get_collection(stock_id)
    
    stock_prices = []
    async for stock in stock_collection.find():
        stock_prices.append(stock_helper(stock))
    

    if stock_prices is not None:
        return stock_prices
    
    return HTTPException(status_code=404, detail=f"Stock {stock_id} not found")