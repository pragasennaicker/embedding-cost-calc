from pytest import approx
from embed_cost import estimate_embedding_cost


def test_precise_counting():
    chunks = ["hello world", "token test"]
    # encode with cl100k_base:
    # "hello world" → 2 tokens, "token test" → 2 tokens (approx)
    cost = estimate_embedding_cost(
        num_chunks=0,           # ignored in precise mode
        precise=True,
        chunk_texts=chunks
    )
    # total_tokens ≈ 4, rate 0.0004/1k → cost ≈ 4*0.0004/1000
    assert cost == approx((4 * 0.00010) / 1000)
