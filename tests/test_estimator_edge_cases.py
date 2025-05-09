import pytest
from embed_cost import estimate_embedding_cost, MODEL_RATES


def test_zero_chunks_returns_zero_cost():
    # No chunks → zero tokens → zero cost
    cost = estimate_embedding_cost(
        num_chunks=0,
        chunk_size_chars=500,
        model="text-embedding-ada-002",
        precise=False
    )
    assert cost == pytest.approx(0.0)


def test_zero_chunk_size_returns_zero_cost():
    # Chunks of length 0 → zero tokens → zero cost
    cost = estimate_embedding_cost(
        num_chunks=5,
        chunk_size_chars=0,
        model="text-embedding-ada-002",
        precise=False
    )
    assert cost == pytest.approx(0.0)


@pytest.mark.parametrize("model_name", list(MODEL_RATES))
def test_rough_mode_all_models(model_name):
    # For each model: cost = num_chunks * (chars/4 tokens) * rate_per_1k / 1000
    num_chunks = 4
    chunk_size = 250
    expected_tokens = num_chunks * (chunk_size / 4)
    expected_cost = expected_tokens * MODEL_RATES[model_name] / 1000

    cost = estimate_embedding_cost(
        num_chunks=num_chunks,
        chunk_size_chars=chunk_size,
        model=model_name,
        precise=False
    )
    assert cost == pytest.approx(expected_cost)


def test_precise_mode_empty_string_chunk():
    # An empty string encodes to 0 tokens → zero cost
    cost = estimate_embedding_cost(
        num_chunks=0,  # ignored in precise mode
        precise=True,
        model="text-embedding-ada-002",
        chunk_texts=[""]
    )
    assert cost == pytest.approx(0.0)
