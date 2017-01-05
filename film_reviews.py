def review(source, review, in_french=False):
    tokens = review.split(",")
    if source == "filmsonline":
        review_score = int(tokens[2])
        if review_score > 50:
            if in_french:
                return "tres bon"
            else:
                return "good"

        if in_french:
            return "merde"
        else:
            return "bad"

    if source == "filmorama":
        review_score_str = tokens[3]
        if review_score_str.isdigit():
            if int(review_score_str) > 2:
                if in_french:
                    return "tres bon"
                else:
                    return "good"
        else:
            return "unknown"

        if in_french:
            return "merde"
        else:
            return "bad"

    review_score = len(tokens[0])
    reviewer = tokens[1]
    if reviewer == "warren bew":
        if review_score > 2:
            if in_french:
                return "tres bon"
            else:
                return "good"

    if review_score > 3:
        if in_french:
            return "tres bon"
        else:
            return "good"

    if in_french:
        return "merde"
    else:
        return "bad"

