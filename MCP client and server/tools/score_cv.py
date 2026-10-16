# tools/score_cv.py
# MCP Tool 2: Score a CV against a job description via keyword matching

import json
import re


def score_cv(cv_text: str, job_description: str) -> str:
    """
    Score a CV against a job description using keyword matching.
    Returns a JSON report with a score out of 100 and feedback.

    Args:
        cv_text:         The full text of the candidate CV.
        job_description: The job description to match against.

    Returns:
        A JSON string with: score, matched_keywords, missing_keywords, feedback.
    """
    def tokenise(text):
        words = re.findall(r"[a-zA-Z0-9#+.-]+", text.lower())
        stop = {"a", "an", "the", "and", "or", "to", "of", "in", "for",
                "with", "on", "is", "are", "be", "you", "we", "our"}
        return {w for w in words if len(w) > 2 and w not in stop}

    jd_keywords = tokenise(job_description)
    cv_keywords  = tokenise(cv_text)

    matched = sorted(jd_keywords & cv_keywords)
    missing = sorted(jd_keywords - cv_keywords)
    score   = round(len(matched) / max(len(jd_keywords), 1) * 100, 1)

    if score >= 80:
        feedback = "Excellent match! The CV aligns very well with the job description."
    elif score >= 60:
        feedback = "Good match. Consider adding the missing keywords to improve your score."
    elif score >= 40:
        feedback = "Average match. Several important keywords are missing from the CV."
    else:
        feedback = "Poor match. The CV needs significant updates to align with this role."

    return json.dumps({
        "score":            score,
        "max_score":        100,
        "matched_keywords": matched[:20],
        "missing_keywords": missing[:20],
        "feedback":         feedback,
    }, indent=2)