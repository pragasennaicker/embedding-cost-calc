from pytest import approx, raises
import tiktoken
from embed_cost import estimate_embedding_cost, MODEL_RATES


def test_rough_mode_uses_chars_heuristic():
    # 3 chunks × (400 chars / 4) = 3 × 100 tokens = 300 tokens
    # Cost = 300 tokens × 0.0001 $/1k tokens ÷ 1000 = 0.00003
    cost = estimate_embedding_cost(
        num_chunks=3,
        chunk_size_chars=400,
        model="text-embedding-ada-002",
        precise=False
    )
    expected = 300 * MODEL_RATES["text-embedding-ada-002"] / 1000
    assert cost == approx(expected)


def test_precise_mode_counts_exact_tokens():
    chunks = ["hello world", "token test"]
    # Use the same encoder logic as in estimator
    try:
        encoder = tiktoken.encoding_for_model("text-embedding-ada-002")
    except Exception:
        encoder = tiktoken.get_encoding("cl100k_base")

    total_tokens = sum(len(encoder.encode(text)) for text in chunks)
    cost = estimate_embedding_cost(
        num_chunks=0,
        precise=True,
        model="text-embedding-ada-002",
        chunk_texts=chunks
    )
    expected = total_tokens * MODEL_RATES["text-embedding-ada-002"] / 1000
    assert cost == approx(expected)


def test_precise_mode_without_texts_raises():
    with raises(ValueError) as exc:
        estimate_embedding_cost(
            num_chunks=5,
            precise=True,
            model="text-embedding-ada-002",
            chunk_texts=None
        )
    assert "chunk_texts" in str(exc.value)


def test_unknown_model_raises_value_error():
    with raises(ValueError) as exc:
        estimate_embedding_cost(
            num_chunks=1,
            chunk_size_chars=100,
            model="nonexistent-model",
            precise=False
        )
    assert "Unknown model" in str(exc.value)
