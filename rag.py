import os

def retrieve_docs(query):

    query = query.lower()

    docs = []

    keywords = {
        "refund": "refund.txt",
        "billing": "billing.txt",
        "subscription": "subscription.txt",
        "login": "login.txt",
        "password": "password_reset.txt",
        "account": "account_lock.txt",
        "api": "api_errors.txt",
        "security": "security.txt",
        "performance": "performance.txt"
    }

    for key, file in keywords.items():
        if key in query:
            docs.append(file)

    return docs

def get_context(docs):

    context = ""

    for doc in docs:

        path = os.path.join("docs", doc)

        if os.path.exists(path):

            with open(path, "r", encoding="utf-8") as f:
                context += f.read() + "\n\n"

    return context