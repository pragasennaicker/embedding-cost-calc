import pytest
from click.testing import CliRunner
from embed_cost import main


@pytest.fixture
def runner():
    return CliRunner()


def test_help_flag(runner):
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    # Basic usage line
    assert "Usage: embed-cost" in result.output
    # Options we expect
    for opt in ["--chunks", "--chars", "--model", "--help"]:
        assert opt in result.output


def test_default_invocation(runner):
    # 10 chunks × (400 chars / 4) = 1,000 tokens
    # Cost = 1000 * 0.00010 / 1000 = 0.00010 → "$0.000100"
    result = runner.invoke(main, ["--chunks", "10", "--chars", "400"])
    assert result.exit_code == 0
    assert result.output.strip() == "Estimated embedding cost: $0.000100"


def test_custom_model_invocation(runner):
    # 2 chunks × (100 chars / 4) = 50 tokens
    # text-embedding-3-small rate = 0.00002
    # cost = 50*0.00002/1000 = 0.000001 → "$0.000001"
    result = runner.invoke(
        main,
        ["--chunks", "2", "--chars", "100", "--model",
         "text-embedding-3-small",
         ]
    )
    assert result.exit_code == 0
    assert result.output.strip() == "Estimated embedding cost: $0.000001"


@pytest.mark.parametrize("chunks,chars", [
    ("0", "500"),  # invalid chunks
    ("5", "0"),    # invalid chars
])
def test_invalid_numeric_inputs(runner, chunks, chars):
    args = ["--chunks", chunks]
    # only add --chars if provided
    if chars is not None:
        args += ["--chars", chars]
    result = runner.invoke(main, args)
    assert result.exit_code != 0
    assert "must be a positive integer" in result.output
