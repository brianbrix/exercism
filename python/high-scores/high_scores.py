def latest(scores):
    if scores:
        return scores[-1]


def personal_best(scores):
    scores = sorted(scores)
    if scores:
        return scores[-1]


def personal_top_three(scores):
    scores = sorted(scores, reverse=True)
    if scores and len(scores) >= 3:
        return scores[:3]
    return scores

