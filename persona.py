def detect_persona(query):

    query = query.lower()

    technical_words = [
        "api",
        "error",
        "server",
        "authentication",
        "logs",
        "configuration"
    ]

    frustrated_words = [
        "frustrated",
        "angry",
        "nothing works",
        "tried everything",
        "issue"
    ]

    executive_words = [
        "business",
        "operations",
        "impact",
        "timeline",
        "resolved"
    ]

    if any(word in query for word in technical_words):
        return "Technical Expert"

    elif any(word in query for word in frustrated_words):
        return "Frustrated User"

    else:
        return "Business Executive"