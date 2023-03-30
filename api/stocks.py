from typing import Tuple, List, Optional

from fastapi import APIRouter, Request, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.stock import StockModel
from models.response import ResponseModel, ErrorResponseModel
from datetime import datetime

router = APIRouter()

# student_collection = database.get_collection("students_collection")


# helpers


def stock_helper(stock) -> dict:

    # date_string = datetime.strptime(stock["date"], '%Y-%m-%dT%H:%M:%S').date()

    return {
        "id": str(stock["id"]),
        "close": stock["close"],
        "volume": stock["volume"],
        "date": stock["date"].date(),
    }



@router.get("/", response_description="List all stocks")
def list_stocks():

    # get all stock collections from the database

    return {"stocks": "List of all stocks"}



"""
response format 
{
    "id": 1,
    "stock_code": "000001.XSHE",
    "stock_name": "平安银行", 
    "history_price": [
        {
        "close": 12.00,
        "volume": 10000000,
        "date": "2021-01-01"
        },
        {
        "close": 12.00,
        "date": "2021-01-01"
        },
        {
        "close": 12.00,
        "date": "2021-01-01"
        },
        ...
    ]
}
"""
@router.get("/{stock_id}", response_description="Get a single stock")
async def get_one_stock_history_data(stock_id: str, request: Request):

    # get a single stock collection from the database and return the result to the user

    print(f"stock_id: {stock_id}")

    stock_info = await request.app.mongodb['stock_code'].find_one({"stock_code": stock_id})
    
    print(f"stock_info: {type(StockModel(**stock_info))}")

    # return ResponseModel("", "Stock data retrieved successfully")
    response_data = StockModel(**stock_info)
    
    stock_history_price_collection = request.app.mongodb.get_collection(stock_id)
    
    stock_prices = []
    async for price in stock_history_price_collection.find():
        stock_prices.append(stock_helper(price))
    
    response_data.history_data = stock_prices

    if stock_prices is not None:
        return jsonable_encoder(response_data)
    
    return HTTPException(status_code=404, detail=f"Stock {stock_id} not found")