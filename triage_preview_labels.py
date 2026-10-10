"""A second small fixture for verifying PR ingestion in the Hutch preview."""


def display_rule_name(rule_name: str) -> str:
    """Normalize whitespace and give blank rule names a readable fallback."""
    return " ".join(rule_name.split()) or "Untitled rule"
