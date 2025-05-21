from typing import Dict, List
import tiktoken


# Default rates (USD per 1k tokens) as at 06 May 2025
MODEL_RATES: Dict[str, float] = {
    "text-embedding-3-small": 0.00002,
    "text-embedding-3-large": 0.00013,
    "text-embedding-ada-002": 0.00010,
}


def estimate_embedding_cost(
    *,
    chunk_texts: List[str] | None = None,
    num_chunks: int | None = None,
    chunk_size_chars: int = 500,
    model: str = "text-embedding-ada-002",
) -> float:

    try:
        rate_per_1k = MODEL_RATES[model]
    except KeyError:
        available = ", ".join(sorted(MODEL_RATES))
        raise ValueError(
            f"Unknown model: {model!r}. Available models: {list(available)}"
        )

    if chunk_texts is not None:
        # Precise mode
        try:
            encoder = tiktoken.encoding_for_model(model)
        except Exception:
            encoder = tiktoken.get_encoding("cl100k_base")
        total_tokens = sum(
            len(encoder.encode(text)) for text in chunk_texts
            )
    else:
        # Rough mode
        if num_chunks is None or num_chunks < 1:
            raise ValueError(
                "`num_chunks` must be a positive integer when \
                    `chunk_texts` is not provided"
            )
        avg_tokens = chunk_size_chars / 4  # fallback heuristic
        total_tokens = num_chunks * avg_tokens

    cost = (total_tokens * rate_per_1k) / 1000

    return cost
