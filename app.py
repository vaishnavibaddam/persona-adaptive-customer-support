import streamlit as st

from persona import detect_persona
from rag import retrieve_docs, get_context
from escalation import check_escalation
from handoff import generate_handoff

st.set_page_config(
    page_title="Persona Adaptive Customer Support Agent",
    page_icon="🤖"
)

st.title("🤖 Persona Adaptive Customer Support Agent")

query = st.text_input(
    "Enter your support question"
)

if st.button("Submit"):

    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    # Persona Detection
    persona = detect_persona(query)

    st.subheader("Detected Persona")
    st.write(persona)

    # Retrieve Documents
    docs = retrieve_docs(query)

    st.subheader("Retrieved Sources")

    if docs:
        st.write(docs)
    else:
        st.write("No relevant documents found")

    # Get Knowledge Base Context
    context = get_context(docs)

    # Generate Persona-Based Response
    if docs:

        if persona == "Technical Expert":

            response = f"""
### Technical Analysis

{context}

Recommended Actions:
- Verify configuration settings
- Check logs for errors
- Validate authentication credentials
- Follow troubleshooting procedures
"""

        elif persona == "Frustrated User":

            response = f"""
I understand your frustration.

Based on our support documentation:

{context}

Please try the suggested troubleshooting steps. If the issue continues, contact support for further assistance.
"""

        else:

            response = f"""
### Business Summary

{context}

Please review the above information and take the appropriate action.
"""

    else:

        response = """
No relevant information was found in the knowledge base.

Recommendation:
Escalate this issue to a support representative.
"""

    st.subheader("Generated Response")
    st.write(response)

    # Escalation Check
    escalate = check_escalation(query)

    st.subheader("Escalation Status")

    if escalate:

        st.error(
            "Escalated to Human Support Agent"
        )

        summary = generate_handoff(
            persona,
            query,
            docs
        )

        st.subheader("Human Handoff Summary")
        st.json(summary)

    else:

        st.success(
            "Issue Resolved by AI Agent"
        )