from pytest import approx
import tiktoken
from embed_cost import estimate_embedding_cost, MODEL_RATES


def test_precise_mode_encoder_fallback(monkeypatch):
    # Force encoding_for_model() to error out
    def broken_encoder(model_name):
        raise RuntimeError("simulated failure")

    monkeypatch.setattr(tiktoken, "encoding_for_model", broken_encoder)
    # Now call in precise mode; it should catch the exception
    text = "hello world"
    cost = estimate_embedding_cost(
        model="text-embedding-ada-002",
        chunk_texts=[text],
    )

    # Compute expected using the fallback encoder
    encoder = tiktoken.get_encoding("cl100k_base")
    expected_tokens = len(encoder.encode(text))
    rate_per_1k = MODEL_RATES["text-embedding-ada-002"]
    expected_cost = expected_tokens * rate_per_1k / 1000

    assert cost == approx(expected_cost)
