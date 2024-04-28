import cProfile
import io
import logging
import pstats
import time
from contextlib import contextmanager
from functools import wraps
from typing import (
    Any,
    Callable,
    Generator,
)

from memory_profiler import profile

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s (%(levelname)s): %(message)s"
)
logger = logging.getLogger(__name__)


@contextmanager
def timer_block(block_name: str) -> Generator[None, None, None]:
    start = time.time()
    yield
    logger.info(f"{block_name} took {time.time() - start} seconds")


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.2f} seconds")
        return result

    return wrapper


def profile_and_save_stats(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("time")
        ps.print_stats()
        print(s.getvalue())

        return result

    return wrapper


# @profile
# def profile_train_bpe(input_path, vocab_size, special_tokens, name):
#     pr = cProfile.Profile()
#     pr.enable()

#     start_time = time.time()
#     # vocab, merges = tokenizer.from_file(input_path)
#     tokenizer = Tokenizer.train_from_file(input_path, vocab_size, special_tokens)
#     end_time = time.time()

#     pr.disable()

#     tokenizer.save("data/tokenizer", name)

#     s = io.StringIO()
#     ps = pstats.Stats(pr, stream=s).sort_stats("time")
#     ps.print_stats()
#     # print(s.getvalue())

#     training_time = end_time - start_time
#     print(f"Training time: {training_time:.2f} seconds")
