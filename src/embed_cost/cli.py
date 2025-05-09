import click
from .estimator import estimate_embedding_cost, MODEL_RATES


@click.command(name="embed-cost")
@click.option(
    "--chunks", "-n",
    type=int,
    default=1,
    show_default=True,
    help="Number of chunks to estimate"
)
@click.option(
    "--chars", "-c",
    type=int,
    default=500,
    show_default=True,
    help="Average characters per chunk (fallback mode)"
)
@click.option(
    "--model", "-m",
    type=click.Choice(list(MODEL_RATES)),
    default="text-embedding-ada-002",
    show_default=True,
    help="Embedding model to use"
)
@click.option(
    "--precise/--no-precise",
    default=False,
    help="Use precise token counting via tiktoken"
)
@click.option(
    "--text", "-t",
    multiple=True,
    help=(
        "Text chunk(s) for precise mode; "
        "specify once per chunk (required if --precise)"
    )
)
def main(chunks, chars, model, precise, text):
    """
    Estimate OpenAI embedding costs.

    Rough mode (default) uses chars/4 heuristic.
    Precise mode uses tiktoken on provided --text chunks.
    """
    if precise:
        if not text:
            raise click.UsageError(
                "When --precise is set, you must pass at least one --text"
            )
        cost = estimate_embedding_cost(
            num_chunks=0,
            chunk_size_chars=chars,
            model=model,
            precise=True,
            chunk_texts=list(text),
        )
    else:
        cost = estimate_embedding_cost(
            num_chunks=chunks,
            chunk_size_chars=chars,
            model=model,
            precise=False,
        )

    click.echo(f"Estimated embedding cost: ${cost:.6f}")


if __name__ == "__main__":
    main()
