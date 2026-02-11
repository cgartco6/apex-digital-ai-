import React from "react";
import axios from "axios";

export default function Checkout() {
    const purchaseProduct = async (productName) => {
        const res = await axios.post("http://localhost:8000/payments/create_checkout_session", {
            product_name: productName,
            quantity: 1
        });
        window.location.href = res.data.url || "/";
    };

    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold">Checkout</h1>
            <button className="mt-4 px-4 py-2 bg-blue-600 text-white" onClick={() => purchaseProduct("Starter Tier")}>
                Buy Starter Tier
            </button>
        </div>
    );
      }
