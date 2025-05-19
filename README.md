# Embed Cost Estimator
![CI](https://github.com/pragasennaicker/embedding-cost-calc/actions/workflows/ci.yml/badge.svg)


A lightweight Python library and CLI to estimate OpenAI embedding costs.

## Installation
Install from PyPI:

```bash
pip install embed-cost-estimator
```

## Basic CLI Usage
Run a quick rough estimate (chars/4 heuristic):

```bash
embed-cost --chunks <NUM_CHUNKS> --chars <AVG_CHARS_PER_CHUNK> [--model <MODEL>]

#--chunks, -n  Number of chunks (required)

#--chars, -c  Average characters per chunk (default: 500)

#--model, -m  Embedding model choice (default: text-embedding-ada-002)
```

## CLI Options

| Option       | Shortcut | Type     | Default                  | Description                                 |
|--------------|----------|----------|--------------------------|---------------------------------------------|
| `--chunks`   | `-n`     | integer  | _required_               | Number of chunks for rough-mode estimate    |
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

## Python API (Precise Mode)
For exact token counts via `tiktoken`, import and call directly:
```python
from embed_cost import estimate_embedding_cost

# your pre-chunked list of text segments
chunked_docs = [
    "First chunk of text…",
    "Second chunk of text…",
    # …etc…
]

cost = estimate_embedding_cost(
    num_chunks=0,               # ignored in precise mode
    model="text-embedding-ada-002",
    precise=True,
    chunk_texts=chunked_docs,
)
print(f"Precise cost: ${cost:.6f}")

```

### Examples

### 1. Exact Token Count in Code
```python
from embed_cost import estimate_embedding_cost

# assuming your document is already split:
chunked = ["Lorem ipsum…", "Dolor sit amet…", …]
cost = estimate_embedding_cost(
    num_chunks=0,
    precise=True,
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
3. Open a pull request against main.

4. Maintain 100% test coverage for new code and adhere to Black/Flake8 style.

Please see CONTRIBUTING.md (coming soon) for more details.

## License
MIT © Pragasen Naicker