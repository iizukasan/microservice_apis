from datetime import datetime
from enum import Enum
from typing_extensions import Annotated
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, conint, conlist


class Size(Enum):
    small = "small"
    medium = "medium"
    large = "large"


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


type QuantityType = Annotated[int, conint(ge=1, strict=True)]


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[QuantityType] = 1


type OrderListType = Annotated[List, conlist(item_type=OrderItemSchema, min_length=1)]


class CreateOrderSchema(BaseModel):
    order: OrderListType


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum


class GetOrderSchema(BaseModel):
    orders: List[GetOrderSchema]
