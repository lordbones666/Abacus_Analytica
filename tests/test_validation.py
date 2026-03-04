from forecasting_engine.validation import (
    ValidationError,
    question_gate,
    validate_question_object,
    validate_source_record,
)


def test_question_validation_rejects_missing_resolution() -> None:
    payload = {
        "question_id": "C1",
        "wording": "Will X happen?",
        "time_window": {
            "opens_at": "2026-01-01T00:00:00Z",
            "closes_at": "2026-02-01T00:00:00Z",
            "timezone": "UTC",
        },
        "binary_criteria": {"yes_definition": "yes", "no_definition": "no"},
        "version": "v1",
    }

    try:
        validate_question_object(payload)
    except ValidationError:
        pass
    else:
        raise AssertionError("Expected ValidationError")


def test_question_gate_detects_missing_fields() -> None:
    ok, issues = question_gate({"wording": "test"})
    assert not ok
    assert "missing_resolution_authority" in issues


def test_source_record_requires_retrieval_fields() -> None:
    sr = validate_source_record(
        {
            "source_id": "sr1",
            "url": "https://example.com",
            "publisher": "example",
            "retrieved_at": "2026-01-01T00:00:00Z",
            "title": "Headline",
            "content_hash": "abc",
            "excerpt": "snippet",
        }
    )
    assert sr.url == "https://example.com"
