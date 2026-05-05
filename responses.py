def get_response(message):
    message = message.lower()

    # Greeting
    if any(word in message for word in ["hi", "hello", "hey", "salam"]):
        return "Hello 👋 Welcome to VELOUR! How can I help you today?\nYou can ask about pricing, sizing, delivery, or orders."

    # Pricing
    elif "price" in message or "cost" in message:
        return "Our prices:\nHoodies: PKR 4,200 – 5,500\nT-Shirts: PKR 1,800 – 2,200\nCargos: PKR 3,500 – 4,500"

    # Sizing
    elif "size" in message or "sizing" in message:
        return "Size Guide:\nXS: Chest 32-34\nS: 34-36\nM: 36-38\nL: 38-40\nXL: 40-42\nXXL: 42-44"

    # Delivery
    elif "delivery" in message or "shipping" in message:
        return "Delivery:\n2–3 days in major cities\n4–6 days in others\nFlat rate PKR 200\nFree above PKR 5000"

    # Payment
    elif "payment" in message or "cod" in message:
        return "We accept JazzCash, EasyPaisa, Bank Transfer, and Cash on Delivery."

    # Returns
    elif "return" in message or "exchange" in message:
        return "You can exchange within 7 days. Item must be unused with tags. Share order ID to proceed."

    # Order status
    elif "order" in message or "track" in message:
        return "Please share your Order ID so we can check your order status."

    # Fallback
    else:
        return "Thanks for your message! Our team will get back to you shortly. Follow @shopvelour for updates."