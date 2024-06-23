from datetime import datetime
from uuid import UUID

from starlette.responses import Response
from starlette import status

from orders.app import app

orders = {
    "id": "abcd-1234",
    "status": "delivered",
    "created": datetime.now(datetime.UTC),
    "order": {"product": "cappuccino", "size": "medium", "quantity": 1},
}


@app.get("/orders")
def get_orders():
    return {"orders": [orders]}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order():
    return orders


@app.get("/orders/{order_id}")
def get_order(order_id: UUID):
    return orders


@app.put("/orders/{order_id}")
def update_order(order_id: UUID):
    return orders


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/orders/{order_id}/cancel")
def cancel_order(order_id: UUID):
    return orders


@app.post("/orders/{order_id}/pay")
def pay_order(order_id: UUID):
    return orders
