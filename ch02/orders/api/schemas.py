from datetime import datetime
from enum import Enum
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


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1


class CreateOrderSchema(BaseModel):
    order: conlist(item_type=OrderItemSchema, min_length=1)


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum


class GetOrderSchema(BaseModel):
    orders: List[GetOrderSchema]
