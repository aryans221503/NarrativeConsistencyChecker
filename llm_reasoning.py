def llm_verdict(claim, evidence):
    text = (claim + " " + evidence).lower()

    if "never" in text or "refused" in text:
        return "CONTRADICT"

    return "UNCLEAR"
