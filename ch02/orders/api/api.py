from datetime import datetime, timezone
from uuid import UUID

from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import CreateOrderSchema, GetOrdersSchema, GetOrderSchema

orders = {
    "id": "abcd-1234",
    "status": "delivered",
    "created": datetime.now(timezone.utc),
    "order": {"product": "cappuccino", "size": "medium", "quantity": 1},
}


@app.get("/orders", response_model=GetOrdersSchema)
def get_orders():
    return {"orders": [orders]}


@app.post("/orders", status_code=status.HTTP_201_CREATED, response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    return orders


@app.get("/orders/{order_id}", response_model=GetOrderSchema)
def get_order(order_id: UUID):
    return orders


@app.put("/orders/{order_id}", response_model=GetOrderSchema)
def update_order(order_details: CreateOrderSchema):
    return orders


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/orders/{order_id}/cancel", response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    return orders


@app.post("/orders/{order_id}/pay", response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    return orders
