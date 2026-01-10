def final_decision(claim_verdicts):
    """
    If any claim contradicts the novel → 0
    Else → 1
    """
    for v in claim_verdicts:
        if v == "CONTRADICT":
            return 0
    return 1
