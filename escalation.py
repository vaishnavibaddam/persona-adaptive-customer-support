def check_escalation(query):

    keywords = [
        "billing",
        "refund",
        "legal",
        "lawsuit"
    ]

    return any(word in query.lower()
               for word in keywords)