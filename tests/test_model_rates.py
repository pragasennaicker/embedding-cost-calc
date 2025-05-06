from pytest import approx
from embed_cost import MODEL_RATES


def test_default_model_rate():
    assert "test-embedding-ada-002" in MODEL_RATES
    assert MODEL_RATES["text-embedding-ada-002"] == approx(0.00010)
