def process_crypto(payment_data):
    # Simulate crypto processing (BTC, ETH, USDT, Valr)
    tx_id = "CRYPTO_TX_" + str(hash(str(payment_data)))
    return {"status": "success", "transaction_id": tx_id}
