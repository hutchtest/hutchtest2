"""A small fixture for checking pull request ingestion in the Triage preview."""


def normalize_rule_name(value: str) -> str:
    """Collapse whitespace in a sample rule name."""
    return " ".join(value.split())
