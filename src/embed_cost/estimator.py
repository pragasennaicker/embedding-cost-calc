from typing import Dict

# Default rates (USD per 1k tokens) as at 06 May 2025
MODEL_RATES: Dict[str, float] = {
    "text-embedding-3-small": 0.00002,
    "text-embedding-3-large": 0.00013,
    "text-embedding-ada-002": 0.00010,
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
        available = ", ".join(sorted(MODEL_RATES))
        raise ValueError(
            f"Unknown model: {model!r}. Available models: {list(available)}"
        )

    if precise:
        # TODO: precise logic
        avg_tokens = (
            chunk_size_chars / 4
        )  # fallback until tiktoken is integrated
    else:
        avg_tokens = chunk_size_chars / 4  # fallback heuristic

    total_tokens = num_chunks * avg_tokens
    cost = (total_tokens * rate_per_1k) / 1000

    return cost
