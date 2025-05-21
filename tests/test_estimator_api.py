import pytest
from embed_cost.estimator import estimate_embedding_cost, MODEL_RATES


def test_rough_mode_keyword_only():
    """
    Calling with only num_chunks and chunk_size_chars exercises the
    rough (chars/4) heuristic.
    """
    num_chunks = 5
    chunk_size = 120
    # tokens = 5 * (120/4) = 5 * 30 = 150
    expected_tokens = num_chunks * (chunk_size / 4)
    expected_cost = expected_tokens * (
        MODEL_RATES["text-embedding-ada-002"] / 1000
    )

    cost = estimate_embedding_cost(
        num_chunks=num_chunks,
        chunk_size_chars=chunk_size
    )
    assert cost == pytest.approx(expected_cost)


def test_precise_mode_keyword_only(monkeypatch):
    """
    Calling with only chunk_texts exercises precise token counting.
    We simulate tiktoken to ensure determinism.
    """
    chunks = ["foo bar", "baz qux"]
    # Monkeypatch tiktoken to use a fake encoder:

    class FakeEncoder:
        def encode(self, text):
            # simple rule: one token per word
            return text.split()
    monkeypatch.setattr(
        "tiktoken.encoding_for_model",
        lambda model: FakeEncoder()
        )
    # Ensure fallback isn't triggered:
    monkeypatch.setattr("tiktoken.get_encoding", lambda name: FakeEncoder())

    # expected tokens = 2 words + 2 words = 4
    expected_tokens = sum(len(chunk.split()) for chunk in chunks)
    expected_cost = expected_tokens * (
        MODEL_RATES["text-embedding-ada-002"] / 1000
        )

    cost = estimate_embedding_cost(
        chunk_texts=chunks
    )
    assert cost == pytest.approx(expected_cost)


def test_missing_both_args_raises():
    """
    Calling with neither num_chunks nor chunk_texts should raise.
    """
    with pytest.raises(ValueError) as exc:
        estimate_embedding_cost()
    msg = str(exc.value)
    assert "num_chunks" in msg  # our error mentions num_chunks
