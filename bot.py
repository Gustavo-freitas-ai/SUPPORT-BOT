def get_bot_response(message):
    message = message.lower()

    if "horario" in message or "horário" in message or "atendimento" in message or "horas" in message:
        return "Nosso atendimento é das 8h às 18h."

    elif "preco" in message or "preço" in message or "valor" in message:
        return "Nossos preços estão disponíveis na página de produtos."

    elif "suporte" in message or "ajuda" in message:
        return "Você pode falar com nosso suporte pelo e-mail suporte@empresa.com"

    elif "ola" in message or "oi" in message or "olá" in message:
        return "Olá! Como posso ajudar você hoje?"

    else:
        return "Desculpe, não entendi. Pode reformular?"