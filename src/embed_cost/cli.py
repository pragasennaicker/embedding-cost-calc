import click
from .estimator import estimate_embedding_cost, MODEL_RATES


@click.command(name="embed-cost")
@click.option(
    "--chunks", "-n",
    type=int,
    default=1,
    show_default=True,
    help="Number of chunks for rough-calculation estimate"
)
@click.option(
    "--chars", "-c",
    type=int,
    default=500,
    show_default=True,
    help="Average characters per chunk"
)
@click.option(
    "--model", "-m",
    type=click.Choice(list(MODEL_RATES)),
    default="text-embedding-ada-002",
    show_default=True,
    help="Embedding model to use"
)
def main(chunks, chars, model):
    """
    Estimate OpenAI embedding cost using a simple chars/4 heuristic.
    """
    if chunks < 1:
        raise click.UsageError("`--chunks` must be a positive integer")
    if chars < 1:
        raise click.UsageError("`--chars` must be a positive integer")

    cost = estimate_embedding_cost(
        num_chunks=chunks,
        chunk_size_chars=chars,
        model=model,
        precise=False,
    )

    formatted = f"${cost:,.6f}"
    click.echo(f"Estimated embedding cost: {formatted}")


if __name__ == "__main__":
    main()
