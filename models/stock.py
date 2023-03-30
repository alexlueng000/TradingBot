from typing import Optional
from infra.base_object import MongoBaseModel
from pydantic import Field
from datetime import date


class StockModel(MongoBaseModel):
    # collection = 'stocks'
    id: int = Field(...)
    stock_code: str = Field(...)
    display_name: str = Field(...)
    name: str = Field(...)
    start_date: date = Field(...)
    end_date: date = Field(...)
    type: str = Field(...)
    history_data: Optional[list] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        # json_encoders = { ObjectId: str }
        schema_extra = {
            "example": {
                "stock_id": 0,
                "stock_code": "000001.XSHE",
                "display_name": "平安银行",
                "adj_name": "PAYH",
                "start_date": "2005-01-04",
                "end_date": "2020-12-31",
                "type": "stock"
            }
        }
    