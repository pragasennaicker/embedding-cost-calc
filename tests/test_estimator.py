from pytest import approx
from embed_cost.estimator import estimate_embedding_cost


def test_rough_estimate_default_model():
    """
    10 chunks × (400 chars / 4) = 10 × 100 tokens = 1,000 tokens
    At $0.00010 per 1k tokens:
    expected cost = 1,000 * 0.00010 / 1000 = $0.00010
    """
    cost = estimate_embedding_cost(
        num_chunks=10, chunk_size_chars=400, precise=False
    )
    assert cost == approx(0.00010)
