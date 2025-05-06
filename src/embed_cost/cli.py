import click
from .estimator import estimate_embedding_cost, MODEL_RATES


@click.command()
@click.option(
    "--chunks", "-n", type=int, required=True, help="Number of chunks"
)
@click.option(
    "--chars", "-c", type=int, default=500, help="Avg chars per chunk"
)
@click.option(
    "--model",
    "-m",
    type=click.Choice(list(MODEL_RATES)),
    default="text-embedding-ada-002",
    help="Embedding model to use",
)
@click.option(
    "--precise", "-p", is_flag=True, help="Use precise token counting"
)
def main(chunks, chars, model, precise):
    """CLI entry point for embedding cost estimate."""
    cost = estimate_embedding_cost(chunks, chars, model, precise)
    click.echo(f"Estimated cost for embeddings: ${cost:.6f}")


if __name__ == "__main__":
    main()
