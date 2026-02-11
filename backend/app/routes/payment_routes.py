from fastapi import APIRouter
import stripe

stripe.api_key = "sk_test_your_key"

router = APIRouter()

# Products / Tiers
PRODUCTS = {
    "Starter Tier": {"price": 299, "type": "subscription"},
    "Business Tier": {"price": 1299, "type": "subscription"},
    "Pro Tier": {"price": 3499, "type": "subscription"},
    "10 Credits Pack": {"price": 299, "type": "one_time"},
    "25 Credits Pack": {"price": 699, "type": "one_time"},
    "50 Credits Pack": {"price": 1299, "type": "one_time"},
    "100 Credits Pack": {"price": 2499, "type": "one_time"},
}

@router.post("/create_checkout_session")
async def create_checkout_session(product_name: str, quantity: int = 1):
    if product_name not in PRODUCTS:
        return {"error": "Invalid product"}
    product = PRODUCTS[product_name]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'zar',
                'product_data': {'name': product_name},
                'unit_amount': int(product["price"] * 100),
                'recurring': {'interval': 'month'} if product["type"]=="subscription" else None
            },
            'quantity': quantity,
        }],
        mode='subscription' if product["type"]=="subscription" else "payment",
        success_url="https://yourdomain.com/success",
        cancel_url="https://yourdomain.com/cancel"
    )
    return {"sessionId": session.id}
