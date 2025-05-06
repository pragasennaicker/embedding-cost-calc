__all__ = ["estimate_embedding_cost", "MODEL_RATES", "main", "__version__"]

from .estimator import estimate_embedding_cost, MODEL_RATES # noqa: F401
from .cli import main # noqa: F401

__version__ = "0.1.0"
