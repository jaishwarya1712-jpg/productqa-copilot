def check_requirement_quality(requirement: str) -> dict:
    """
    Performs basic rule-based checks on a product requirement.
    """

    print("\n🛠 Requirement Quality Tool was called!")

    checks = {
        "mentions_failure_behavior": False,
        "mentions_limits_or_boundaries": False,
        "mentions_integrations": False,
    }

    requirement_lower = requirement.lower()

    # Failure behavior checks
    failure_keywords = [
        "fail",
        "failed",
        "failure",
        "error",
        "decline",
        "declined",
        "reject",
        "rejected",
        "invalid",
        "timeout",
        "timed out",
        "expire",
        "expired",
        "cancel",
        "cancelled",
        "unsuccessful",
        "unable",
        "retry",
    ]

    matched_failure_terms = [
        keyword
        for keyword in failure_keywords
        if keyword in requirement_lower
    ]

    if matched_failure_terms:
        checks["mentions_failure_behavior"] = True

    checks["matched_failure_terms"] = matched_failure_terms

    # Boundary / limit checks
    boundary_keywords = [
        "limit",
        "minimum",
        "maximum",
        "at least",
        "at most",
        "cannot exceed",
        "must not exceed",
        "greater than",
        "less than",
        "up to",
        "threshold",
        "per day",
        "per user",
        "per transaction",
    ]

    matched_boundary_terms = [
        keyword
        for keyword in boundary_keywords
        if keyword in requirement_lower
    ]

    if matched_boundary_terms:
        checks["mentions_limits_or_boundaries"] = True

    checks["matched_boundary_terms"] = matched_boundary_terms

    # Integration checks
    integration_keywords = [
        "api",
        "integration",
        "integrate",
        "third-party",
        "third party",
        "external service",
        "gateway",
        "webhook",
        "callback",
        "provider",
        "sdk",
    ]

    matched_integration_terms = [
        keyword
        for keyword in integration_keywords
        if keyword in requirement_lower
    ]

    if matched_integration_terms:
        checks["mentions_integrations"] = True

    checks["matched_integration_terms"] = matched_integration_terms

    return checks