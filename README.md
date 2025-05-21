[![PyPI version](https://img.shields.io/pypi/v/embed-cost-estimator.svg)](https://pypi.org/project/embed-cost-estimator/)
[![Build Status](https://github.com/pragasennaicker/embedding-cost-calc/actions/workflows/ci.yml/badge.svg)](https://github.com/pragasennaicker/embedding-cost-calc/actions)

# Embed Cost Estimator
A lightweight Python library and CLI to estimate OpenAI embedding costs.


## Installation
Install from PyPI:


```bash
pip install embed-cost-estimator
```

## Basic CLI Usage (Rough Estimate)
Run a quick rough estimate using a simple `chars/4` heuristic:

```bash
embed-cost --chunks <NUM_CHUNKS> --chars <AVG_CHARS_PER_CHUNK> [--model <MODEL>]

#--chunks, -n  Number of chunks (required)

#--chars, -c  Average characters per chunk (default: 500)

#--model, -m  Embedding model choice (default: text-embedding-ada-002)
```


## CLI Options

| Option       | Shortcut | Type     | Default                  | Description                                 |
|--------------|----------|----------|--------------------------|---------------------------------------------|
| `--chunks`   | `-n`     | integer  | _required_               | Number of chunks for rough estimate    |
| `--chars`    | `-c`     | integer  | `500`                    | Average characters per chunk                |
| `--model`    | `-m`     | choice   | `text-embedding-ada-002` | Embedding model to use (see `MODEL_RATES`)  |
| `--help`     | —        | flag     | —                        | Show this help message and exit             |



### Examples:
### 1. Default model, custom sizes
```bash
embed-cost --chunks 1000 --chars 500
#Estimated embedding cost: $0.050000
```

### 2. Using a different model
```bash
embed-cost --chunks 500 --chars 300 --model text-embedding-3-small
# Estimated embedding cost: $0.003000
```


## Python API
You can call `estimate_embedding_cost()` in two mutually-exclusive ways:

### 1. Rough estimate
Rough estimate using a simple `chars/4` heuristic

```python
from embed_cost import estimate_embedding_cost

cost = estimate_embedding_cost(
    num_chunks=250,
    chunk_size_chars=400,
    model="text-embedding-3-small",
)

print(f"Rough cost: ${cost:.6f}")
```

### 2. Precise mode (exact token counts via `tiktoken`):
For exact token counts via `tiktoken`, by passing your list of text chunks

```python
from embed_cost import estimate_embedding_cost

# your pre-chunked list of text segments
chunked_docs = [
    "First chunk of text…",
    "Second chunk of text…",
    # …etc…
]

cost = estimate_embedding_cost(
    chunk_texts=chunked_docs,
    model="text-embedding-ada-002",
)
print(f"Precise cost: ${cost:.6f}")
```
> [!NOTE]
> You must pass either `num_chunks` (for rough estimate) or `chunk_texts` (for precise), but not both. Omitting both or giving a non-positive `num_chunks` will raise a `ValueError`.


### Example

### 1. Exact Token Count in Code
```python
from embed_cost import estimate_embedding_cost

# assuming your document is already split:
chunked = ["Lorem ipsum…", "Dolor sit amet…", …]
cost = estimate_embedding_cost(
    chunk_texts=chunked,
)
print(cost)  # e.g. 0.000320
```

## Contributing

We welcome contributions!

1. Fork the repo and create a feature branch.

2. Run tests and lint locally:
```bash
poetry install            # or pip install -e .
poetry run pytest -q      # or pytest -q
poetry run flake8 src tests
poetry run black --check .

```
3. Open a pull request against `main`.

4. Maintain 100% test coverage for new code and adhere to Black/Flake8 style.

Please see CONTRIBUTING.md for more details.

## License
MIT © Pragasen Naicker