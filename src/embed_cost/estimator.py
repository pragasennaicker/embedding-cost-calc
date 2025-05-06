from typing import Dict

# Default rates (USD per 1k tokens)
MODEL_RATES: Dict[str, float] = {
    "text-embedding-ada-002",
    0.0004,
    # TODO: add more rates here
}


def estimate_embedding_cost(
    num_chunks: int,
    chunk_size_chars: int = 500,
    model: str = "text-embedding-ada-002",
    precise: bool = False,
) -> float:

    try:
        rate_per_1k = MODEL_RATES[model]
    except KeyError:
        raise ValueError(
            f"Unknown model: {model!r}. Available models: {list(MODEL_RATES)}"
        )

    if precise:
        # TODO: precise logic
        avg_tokens = chunk_size_chars / 4  # fallback until tiktoken is integrated
    else:
        avg_tokens = chunk_size_chars / 4

    total_tokens = num_chunks * avg_tokens
    cost = (total_tokens * rate_per_1k) / 1000

    return cost
