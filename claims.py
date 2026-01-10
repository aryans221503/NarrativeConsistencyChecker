def extract_claims(backstory_text):
    """
    Very simple claim extraction.
    Splits backstory into sentences and treats them as claims.
    """

    # sentence split (simple)
    sentences = backstory_text.split(".")

    claims = []
    for s in sentences:
        s = s.strip()
        if len(s) > 20:  # ignore very small sentences
            claims.append(s)

    # limit claims (avoid noise)
    return claims[:5]
