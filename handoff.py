def generate_handoff(
        persona,
        issue,
        docs):

    return {
        "persona": persona,
        "issue": issue,
        "documents_used": docs,
        "actions_attempted":
            ["Knowledge Base Search"],
        "recommendation":
            "Human support review required"
    }